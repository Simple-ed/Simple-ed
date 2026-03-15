"""
Parsing strategies for school district staff directories.

Strategy order per district:
  1. Finalsite JSON API  — fast, structured data
  2. Generic HTML parser — BeautifulSoup pattern matching
  3. Fallback            — returns a single "needs manual review" row
"""

import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# --- helpers -----------------------------------------------------------------

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4})")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; SchoolDirectoryBot/1.0; "
        "+https://github.com/Simple-ed/Simple-ed)"
    )
}


def _get(url: str, timeout: int = 12) -> requests.Response | None:
    """GET with retry (once), returns None on failure."""
    for attempt in range(2):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout)
            if resp.status_code == 200:
                return resp
        except requests.RequestException:
            pass
        if attempt == 0:
            time.sleep(2)
    return None


def _split_name(full_name: str) -> tuple[str, str]:
    """Split 'First Last' → ('First', 'Last'). Handles middle names."""
    parts = full_name.strip().split()
    if len(parts) == 0:
        return ("", "")
    if len(parts) == 1:
        return (parts[0], "")
    return (parts[0], " ".join(parts[1:]))


def _make_row(
    first="", last="", email="", phone="", title="", school="", district=""
) -> dict:
    return {
        "first_name": first.strip(),
        "last_name": last.strip(),
        "email": email.strip().lower(),
        "phone": phone.strip(),
        "title": title.strip(),
        "school": school.strip(),
        "district": district.strip(),
        "age": "",            # not publicly available
        "years_at_school": "",  # not publicly available
    }


# --- Strategy 1: Finalsite JSON API ------------------------------------------

def parse_finalsite(district: dict) -> list[dict]:
    """
    Finalsite CMS exposes a people search API.
    Try multiple known endpoint patterns.
    """
    base = district["base_url"].rstrip("/")
    district_name = district["name"]
    rows = []

    api_patterns = [
        f"{base}/fs/cms/API/people?departmentId=0&searchString=&siteId=4",
        f"{base}/fs/cms/API/people?departmentId=0&searchString=",
        f"{base}/fs/cms/API/people",
        f"{base}/api/people",
    ]

    for url in api_patterns:
        resp = _get(url)
        if resp is None:
            continue
        try:
            data = resp.json()
        except ValueError:
            continue

        # Finalsite returns {"People": [...]} or a list directly
        people = data if isinstance(data, list) else data.get("People", [])
        if not people:
            people = data.get("people", [])

        for person in people:
            name = (
                person.get("Name")
                or person.get("name")
                or f"{person.get('FirstName','')} {person.get('LastName','')}".strip()
            )
            email = person.get("Email") or person.get("email", "")
            phone = person.get("Phone") or person.get("phone", "")
            title = (
                person.get("Title")
                or person.get("title")
                or person.get("JobTitle", "")
            )
            school = person.get("School") or person.get("school", "")
            first, last = _split_name(name)
            rows.append(
                _make_row(first, last, email, phone, title, school, district_name)
            )

        if rows:
            return rows

    return []


# --- Strategy 2: Generic HTML parser -----------------------------------------

def _extract_from_table(table, district_name: str) -> list[dict]:
    rows = []
    headers = [th.get_text(strip=True).lower() for th in table.find_all("th")]

    col_map = {}
    for i, h in enumerate(headers):
        if any(k in h for k in ("name", "staff", "employee")):
            col_map["name"] = i
        elif "email" in h or "e-mail" in h:
            col_map["email"] = i
        elif "phone" in h or "ext" in h:
            col_map["phone"] = i
        elif "title" in h or "position" in h or "role" in h:
            col_map["title"] = i
        elif "school" in h or "building" in h:
            col_map["school"] = i

    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["td", "th"])
        if not cells:
            continue

        text_cells = [c.get_text(" ", strip=True) for c in cells]
        all_text = " ".join(text_cells)

        # Pull email via regex (most reliable)
        email_match = EMAIL_RE.search(all_text)
        email = email_match.group(0) if email_match else ""

        # Pull phone
        phone_match = PHONE_RE.search(all_text)
        phone = phone_match.group(0) if phone_match else ""

        name = ""
        title = ""
        school = ""

        if "name" in col_map and col_map["name"] < len(text_cells):
            name = text_cells[col_map["name"]]
        if "title" in col_map and col_map["title"] < len(text_cells):
            title = text_cells[col_map["title"]]
        if "school" in col_map and col_map["school"] < len(text_cells):
            school = text_cells[col_map["school"]]

        # Fall back: first cell is usually the name
        if not name and text_cells:
            name = text_cells[0]

        if not name and not email:
            continue

        first, last = _split_name(name)
        rows.append(_make_row(first, last, email, phone, title, school, district_name))

    return rows


def _extract_name_from_plain_text(text: str, email: str, phone: str) -> tuple[str, str]:
    """
    Given a plain-text block like "Amanda Ratliff Long-Term Substitute Teacher ...",
    try to isolate the person's name at the start before any title/role words.
    """
    # Strip the email and phone from the text first
    clean = text
    if email:
        clean = clean.replace(email, " ")
    if phone:
        clean = clean.replace(phone, " ")
    clean = re.sub(r"\s+", " ", clean).strip()

    # Common role/title keywords that signal end of name
    ROLE_KEYWORDS = re.compile(
        r"\b(teacher|aide|principal|director|secretary|nurse|counselor|"
        r"coordinator|supervisor|administrator|assistant|bus|driver|"
        r"substitute|custodian|clerk|librarian|coach|dean|social|"
        r"psychologist|therapist|specialist|technician|manager|"
        r"long[\-\s]term|part[\-\s]time|full[\-\s]time|"
        r"elementary|middle|high|school|district|special|outreach|"
        r"information|technology|guidance|support|office|services|"
        r"department|learning|resource|academic|physical|education)\b",
        re.IGNORECASE,
    )

    # Split on the first occurrence of a role keyword
    match = ROLE_KEYWORDS.search(clean)
    name_part = clean[: match.start()].strip() if match else clean.strip()

    # Validate: a real name is 2–4 Title Case words, no digits
    words = name_part.split()
    if 1 <= len(words) <= 4 and not re.search(r"\d", name_part):
        first = words[0]
        # Build last name from remaining words, excluding any that look like role/title words
        last_parts = []
        for w in words[1:]:
            if ROLE_KEYWORDS.match(w):
                break
            last_parts.append(w)
            if len(last_parts) == 2:  # cap at 2 words
                break
        last = " ".join(last_parts)
        return (first, last)
    return ("", "")


def _extract_from_cards(soup, district_name: str) -> list[dict]:
    """
    Parse staff 'card' layouts — common in Finalsite HTML pages and WordPress themes.
    Looks for divs with class names containing staff/person/employee/faculty/directory.
    Also handles plain-text contact blocks (e.g. div.contact-box).
    """
    rows = []
    card_selectors = [
        "[class*='contact-box']",
        "[class*='contact_box']",
        "[class*='staff']",
        "[class*='person']",
        "[class*='employee']",
        "[class*='faculty']",
        "[class*='directory']",
        "[class*='member']",
        "article",
        ".vcard",
    ]

    cards = []
    for sel in card_selectors:
        found = soup.select(sel)
        # Only use this selector if it returns a reasonable number of items
        # and each card isn't the entire page
        if found and len(found) <= 500:
            cards = found
            break

    for card in cards:
        text = card.get_text(" ", strip=True)
        if len(text) < 5:
            continue

        email_match = EMAIL_RE.search(text)
        email = email_match.group(0) if email_match else ""

        phone_match = PHONE_RE.search(text)
        phone = phone_match.group(0) if phone_match else ""

        # Try to find name in heading tags first
        name = ""
        for tag in ["h1", "h2", "h3", "h4", "strong", "b"]:
            el = card.find(tag)
            if el:
                candidate = el.get_text(strip=True)
                # Avoid using headers that are clearly section titles (> 4 words)
                if candidate and len(candidate.split()) <= 5:
                    name = candidate
                    break

        # Title: look for <span class="*title*"> or <p class="*title*">
        title = ""
        for el in card.find_all(True):
            cls = " ".join(el.get("class", []))
            if any(k in cls.lower() for k in ("title", "position", "role", "job")):
                title = el.get_text(strip=True)
                break

        # If no name found from tags, try extracting from plain text block
        if not name:
            first, last = _extract_name_from_plain_text(text, email, phone)
            if first or last:
                name = f"{first} {last}".strip()

        if not name and not email:
            continue

        first, last = _split_name(name)
        rows.append(_make_row(first, last, email, phone, title, "", district_name))

    return rows


def _extract_emails_from_page(html_text: str, district_name: str) -> list[dict]:
    """
    Last-resort: extract all email addresses visible on the page
    and try to pair them with nearby text (possible name/title).
    Uses a wider context window (300 chars before email) to find names.
    """
    rows = []
    seen_emails: set[str] = set()

    for match in EMAIL_RE.finditer(html_text):
        email = match.group(0)
        if email in seen_emails:
            continue
        seen_emails.add(email)

        # Wide context before the email — strip tags
        start = max(0, match.start() - 300)
        end = min(len(html_text), match.end() + 100)
        context = re.sub(r"<[^>]+>", " ", html_text[start:end])
        context = re.sub(r"\s+", " ", context).strip()

        phone_match = PHONE_RE.search(context)
        phone = phone_match.group(0) if phone_match else ""

        # Strategy A: extract name using role-keyword boundary detection
        first, last = _extract_name_from_plain_text(context, email, phone)

        # Strategy B: fallback to Title Case bigram/trigram pattern
        if not first and not last:
            name_candidates = re.findall(
                r"([A-Z][a-z]+ [A-Z][a-z]+(?:\s[A-Z][a-z]+)?)", context
            )
            name = name_candidates[0] if name_candidates else ""
            first, last = _split_name(name)

        rows.append(_make_row(first, last, email, phone, "", "", district_name))

    return rows


def parse_html(district: dict, extra_urls: list[str] | None = None) -> list[dict]:
    """
    Generic HTML scraper. Tries the district's staff_url first,
    then optional extra URL candidates.
    """
    district_name = district["name"]
    base = district["base_url"].rstrip("/")
    urls_to_try = [district["staff_url"]] + (extra_urls or [])

    for url in urls_to_try:
        resp = _get(url)
        if resp is None:
            continue

        soup = BeautifulSoup(resp.text, "lxml")

        # Remove nav, footer, script, style noise
        for tag in soup(["nav", "footer", "script", "style", "header"]):
            tag.decompose()

        rows = []

        # Try table parsing
        for table in soup.find_all("table"):
            rows.extend(_extract_from_table(table, district_name))

        # Try card/div parsing
        if not rows:
            rows.extend(_extract_from_cards(soup, district_name))

        # Last resort: email harvest from raw HTML
        if not rows:
            rows.extend(_extract_emails_from_page(resp.text, district_name))

        # Deduplicate by email
        seen = set()
        unique = []
        for r in rows:
            key = r["email"] or f"{r['first_name']}|{r['last_name']}"
            if key and key not in seen:
                seen.add(key)
                unique.append(r)

        if unique:
            return unique

    return []


# --- Strategy 3: Fallback ----------------------------------------------------

def fallback_row(district: dict) -> list[dict]:
    """Return a placeholder row so the district appears in the output."""
    return [
        _make_row(
            first="",
            last="",
            email="",
            phone="",
            title="NEEDS MANUAL REVIEW",
            school="",
            district=district["name"],
        )
    ]


# --- Public entry point -------------------------------------------------------

def scrape_district(district: dict) -> list[dict]:
    """
    Try all strategies in order and return whatever rows are found.
    Always sleeps 1.5 s between district requests to be respectful.
    """
    time.sleep(1.5)

    rows = []

    if district.get("cms") in ("finalsite",):
        rows = parse_finalsite(district)

    if not rows:
        from districts import STAFF_PATH_CANDIDATES
        extra = [district["base_url"].rstrip("/") + p for p in STAFF_PATH_CANDIDATES]
        rows = parse_html(district, extra_urls=extra)

    if not rows:
        rows = fallback_row(district)

    return rows
