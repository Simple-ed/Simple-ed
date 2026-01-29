# Personalization Framework

## Why Personalize

Generic cold emails get 1-3% reply rates. Personalized emails get 8-15%+. Every email should have at least one element that proves you did your research.

---

## The 3-Layer Personalization Model

### Layer 1: Firm-Level (minimum -- every email should have this)

Research the prospect's firm and reference something specific:

- **Coverage sectors**: "I know {{firm_name}} covers enterprise software..."
- **Recent fund activity**: "Congrats on the new fund raise..."
- **Firm size / growth**: "With {{firm_name}} growing the team..."
- **Investment style**: "Given your fundamental, bottom-up approach..."

**Where to find this:**
- Firm website (About / Team pages)
- LinkedIn company page
- SEC 13F filings (shows holdings)
- News / press releases

---

### Layer 2: Role-Level (recommended -- makes the email feel targeted)

Reference something specific to their role or responsibilities:

- **Sector coverage**: "Since you cover {{sector}}, you're probably deep in filings for {{company}} right now..."
- **Seniority-specific pain**: For junior analysts: "I know model maintenance eats into your analysis time..." For directors: "Keeping data consistent across your team's models..."
- **Recent activity**: "Saw your note on {{company}} -- the segment breakdown must have been tedious to model..."

**Where to find this:**
- LinkedIn profile (title, experience, posts)
- Firm's team page
- Published research notes (if sell-side)
- Conference speaker lists

---

### Layer 3: Individual-Level (highest impact -- use when possible)

Reference something unique to the person:

- **LinkedIn posts/activity**: "Saw your post about {{topic}} -- interesting take..."
- **Career background**: "Given your background at {{previous_firm}}..."
- **Shared connections**: "{{mutual_connection}} suggested I reach out..."
- **Published content**: "Read your piece on {{topic}}..."
- **Conference appearances**: "Saw you're speaking at {{conference}}..."

**Where to find this:**
- LinkedIn activity feed
- Google search: "{{name}} {{firm}}"
- Twitter/X
- Industry conference agendas

---

## Personalization by Persona

### Hedge Fund Analyst
- Reference their specific sector coverage
- Mention a company they likely cover (check 13F for the firm's holdings)
- Tie to recent earnings for a name in their coverage

### PE Associate
- Reference a recent deal their firm announced
- Mention their sector focus
- Tie to portfolio company monitoring if the firm has public holdings

### Investment Banker
- Reference a recent deal their group worked on
- Mention their industry group
- Tie to pitch/deal cycle timing

### Research Director
- Reference team size or recent hiring
- Mention firm-wide efficiency rather than individual productivity
- Tie to vendor review cycles or budget season

---

## Personalization Merge Fields Reference

| Field | Description | Source |
|-------|-------------|--------|
| `{{first_name}}` | Prospect's first name | CRM / LinkedIn |
| `{{firm_name}}` | Firm name | CRM / LinkedIn |
| `{{prospect_coverage_sector}}` | Sector(s) they cover | LinkedIn / firm website |
| `{{relevant_company}}` | A company in their coverage | 13F filings / research |
| `{{recent_deal}}` | A recent deal the firm worked on | News / press releases |
| `{{new_hire_name}}` | Recent hire at the firm | LinkedIn |
| `{{mutual_connection}}` | Shared connection | LinkedIn |
| `{{current_quarter}}` | e.g., "Q1 2026" | Calendar |
| `{{sender_name}}` | Your name | -- |
| `{{day}}` | Suggested meeting day | Calendar |

---

## Do's and Don'ts

**Do:**
- Keep personalization in the first 1-2 sentences
- Make it natural -- don't force it
- Use personalization that connects to Daloopa's value prop
- Update personalization research before each campaign

**Don't:**
- Over-personalize to the point of seeming creepy
- Use stale information (check dates on news/posts)
- Fake familiarity ("Love what you're doing at {{firm}}!")
- Use personalization that has no connection to why you're reaching out
