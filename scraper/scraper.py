#!/usr/bin/env python3
"""
Chautauqua County, NY — School District Staff Directory Scraper
==============================================================
Scrapes publicly available staff directories from all 18 Chautauqua County
public school district websites and writes results to teachers_chautauqua.csv.

Usage:
    python3 scraper.py

Output:
    ../teachers_chautauqua.csv   (importable directly into Google Sheets)

Columns:
    first_name, last_name, email, phone, title, school, district,
    age, years_at_school

Notes:
    - 'age' and 'years_at_school' are NOT published on public staff directories
      and will be blank — fill these in manually if needed.
    - Rows with title == "NEEDS MANUAL REVIEW" indicate districts where
      automatic scraping returned no results; visit those sites manually.
    - Rate-limited to ~1.5 s per district request; full run takes ~1-2 minutes.
"""

import csv
import os
import sys
import time

# Allow running from the scraper/ subdirectory
sys.path.insert(0, os.path.dirname(__file__))

from districts import DISTRICTS
from parsers import scrape_district

CSV_COLUMNS = [
    "first_name",
    "last_name",
    "email",
    "phone",
    "title",
    "school",
    "district",
    "age",
    "years_at_school",
]

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "teachers_chautauqua.csv")

# Strings that indicate a row is not a real person (case-insensitive)
NOT_A_PERSON = ["therapy dog", "district office", "building", "website@", "webmaster"]


def _is_valid_person(row: dict) -> bool:
    combined = " ".join([row["first_name"], row["last_name"], row["email"], row["title"]]).lower()
    return not any(flag in combined for flag in NOT_A_PERSON)


def main():
    all_rows: list[dict] = []
    summary: list[tuple[str, int, str]] = []  # (district, count, status)

    print(f"\n{'='*60}")
    print("  Chautauqua County School Staff Directory Scraper")
    print(f"{'='*60}\n")

    for district in DISTRICTS:
        name = district["name"]
        print(f"  Scraping: {name} ...", end="", flush=True)

        rows = scrape_district(district)
        rows = [r for r in rows if _is_valid_person(r) or r["title"] == "NEEDS MANUAL REVIEW"]

        needs_review = any(r["title"] == "NEEDS MANUAL REVIEW" for r in rows)
        count = 0 if needs_review else len(rows)
        status = "NEEDS MANUAL REVIEW" if needs_review else f"{count} records"

        print(f" {status}")

        all_rows.extend(rows)
        summary.append((name, count, status))

        # Small pause between districts (respectful crawling)
        time.sleep(0.5)

    # Write CSV
    output_path = os.path.abspath(OUTPUT_FILE)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(all_rows)

    total = sum(c for _, c, _ in summary)
    manual = sum(1 for _, _, s in summary if s == "NEEDS MANUAL REVIEW")

    print(f"\n{'='*60}")
    print(f"  Done! {total} staff records written to:")
    print(f"  {output_path}")
    print(f"\n  {manual} district(s) need manual review (0 records found).")
    print(f"{'='*60}\n")

    print("  Summary by district:")
    print(f"  {'District':<30} {'Records':>8}  Status")
    print(f"  {'-'*30} {'-'*8}  {'-'*22}")
    for dname, count, status in summary:
        flag = " ⚠" if status == "NEEDS MANUAL REVIEW" else ""
        print(f"  {dname:<30} {count:>8}  {status}{flag}")

    print(f"\n  To import into Google Sheets:")
    print("    File → Import → Upload → select teachers_chautauqua.csv")
    print("    Choose 'Replace spreadsheet' or 'Insert new sheet'\n")


if __name__ == "__main__":
    main()
