# Prospecting Playbook — Buy-Side Outbound

---

## Account Qualification

### Target Account Criteria:
- **Fund Type:** Hedge Fund, Asset Manager, Mutual Fund (buy-side only — no sellside)
- **Named Account:** Yes (from target_accounts.csv)
- **Has ADV/Website:** Prioritize accounts with ADV brochure and domain in broker_adv_links.csv — these can be personalized

### Account Tiering:
| Tier | Definition | Examples | Action |
|------|-----------|----------|--------|
| **Tier 1** | Existing customer relationships, warm intro possible, or known pain point | Point72, Citadel, Cadian, XN, Thrivent | Multi-thread aggressively — analyst + PM + DoR |
| **Tier 2** | Named accounts with 10+ contacts, ADV/website available | Millennium, Balyasny, ExodusPoint, Tiger Global, Lone Pine | Full sequence enrollment with personalization |
| **Tier 3** | Named accounts with fewer contacts or limited research available | Smaller funds on target list | Standard sequence, lighter personalization |

---

## Contact Targeting

### Job Titles by Sequence:

| Sequence | Titles to Search | Fund Type Filter |
|----------|-----------------|-----------------|
| **1A (L/S Analyst)** | Analyst, Research Analyst, Senior Analyst, Associate, Senior Associate | Multi-manager, L/S equity, market neutral |
| **1B (Long Biased Analyst)** | Analyst, Research Analyst, Senior Analyst, Associate | Concentrated, long-biased, growth (Tiger Cubs) |
| **1C (Mutual Fund Analyst)** | Analyst, Research Analyst, Associate | Mutual funds, long-only asset managers |
| **2 (PM)** | Portfolio Manager, CIO, Partner, Principal | All buy-side |
| **3 (DoR)** | Director of Research, Head of Research | All buy-side |
| **4 (Head of AI)** | Head of AI, CTO, CDO, VP Technology, Head of Data, Head of Data Engineering | All buy-side (especially multi-strat, quant-adjacent) |
| **5 (Quant/Macro)** | Quantitative Analyst, Quant Researcher, Macro Strategist, Systematic Trader, Data Scientist | Systematic, quant, macro funds |

### Exclusion Rules:
- Any title containing **"Quant"** or **"Macro"** → Sequence 5 ONLY (never 1A-4)
- Any title containing **"Head of AI"**, **"CTO"**, **"CDO"**, **"Head of Data"** → Sequence 4 ONLY (even at quant funds)
- **Sellside** → Do not enroll (out of scope)

---

## Contact Priority — Who to Reach First

### 1. Senior Analyst (Champion)
- **Why first:** They feel the pain daily. They're the end user. If they want it, they pull the PM in.
- **What to find out:** Sector coverage, model count, how they handle earnings updates, what tools they use today
- **Sequence:** 1A, 1B, or 1C depending on fund type
- **Goal:** Get them into a demo on their own coverage names

### 2. Portfolio Manager (Decision Maker)
- **Why second:** Controls budget and team resources. Not the end user, but signs off.
- **What to find out:** Team size, coverage breadth, analyst throughput concerns
- **Sequence:** 2 (PM)
- **Goal:** Frame around analyst output and headcount efficiency — not product features

### 3. Director of Research (Budget Holder)
- **Why third:** Central budget, compliance, vendor management. Growing trend: consolidating vendors and cutting costs.
- **What to find out:** Current vendor stack, coverage gaps, headcount constraints
- **Sequence:** 3 (DoR)
- **Goal:** Frame around expanding coverage without adding headcount

### 4. Head of AI / CTO (Technical Evaluator)
- **Why:** Evaluates data infrastructure. Makes build-vs-buy decisions. Leads AI/LLM adoption.
- **What to find out:** Current data pipeline (internal scrapers vs. vendors), AI/LLM initiatives, integration requirements
- **Sequence:** 4 (Head of AI)
- **Goal:** Technical conversation — API, MCP, taxonomy, webhook architecture

### 5. Quant / Systematic Researcher (Specialist)
- **Why:** Completely different workflow from fundamental analysts. Needs API-first, point-in-time, no look-ahead bias.
- **What to find out:** Current data sources, backtesting infrastructure, filing parser status
- **Sequence:** 5 (Quant/Macro)
- **Goal:** Technical conversation — sample API output on a ticker they cover

---

## Multi-Threading Strategy

For Tier 1 and Tier 2 accounts, enroll multiple contacts simultaneously:

| Account Type | Thread 1 | Thread 2 | Thread 3 |
|-------------|----------|----------|----------|
| **L/S Pod (Millennium, Balyasny)** | Senior Analyst (1A) | PM (2) | Head of Data/AI if available (4) |
| **Concentrated Fund (Tiger Global, Lone Pine)** | Senior Analyst (1B) | PM (2) | DoR (3) |
| **Mutual Fund (Fidelity, Invesco)** | Analyst (1C) | PM (2) | DoR (3) |
| **Quant/Systematic Fund (Two Sigma, AQR)** | Quant Researcher (5) | Head of AI/CTO (4) | — |

**Rules:**
- Never enroll more than 3 contacts at the same firm at the same time
- Stagger enrollment by 2-3 days so emails don't land on the same morning
- If one contact replies, pause sequences for other contacts at that account — coordinate from there

---

## Pre-Enrollment Research Checklist

Before adding any contact to a sequence, complete this:

- [ ] **ADV Brochure** (from broker_adv_links.csv) — AUM, strategy, team size, sector focus
- [ ] **Company Website** (from broker_adv_links.csv) — investment philosophy, portfolio focus, tech signals
- [ ] **LinkedIn** — role, tenure, previous firms (former customer?), sector coverage, recent activity
- [ ] **Apollo custom variables populated:**
  - `{{custom1}}` = Sector coverage or strategy
  - `{{custom2}}` = Specific observation from research
  - `{{custom3}}` = AUM or team size
  - `{{custom4}}` = Previous firm or mutual connection

**If you can't fill custom1 and custom2, the prospect isn't researched enough to enroll.**

---

## Objection Routing

| Objection | Route To |
|-----------|---------|
| "We already use Bloomberg / CapIQ / FactSet" | Not a replacement — we cover data they don't extract (KPIs, segments, footnotes, non-GAAP). Complementary. |
| "We built our own internal scraper" | Build vs. buy conversation. Edge cases in tables, footnotes, and restatements make internal builds a multi-year commitment. Route to Head of AI sequence (4). |
| "Our analysts are fine with manual updates" | Ask how earnings season goes. Ask about error rates. The analyst knows the pain even if management doesn't. |
| "We don't have budget right now" | Plant the seed. Breakup email (Step 5) leaves the door open. Re-engage next quarter. |
| "Send me more information" | Don't send a deck. Offer a 15-minute live demo on a ticker they cover. Information requests that don't convert to meetings are dead leads. |
| "I need to check with my PM / data team" | Offer to include them on the demo. Multi-thread if not already. |

---

## Weekly Prospecting Cadence

| Day | Activity |
|-----|----------|
| **Monday** | Review Apollo replies from weekend sends. Follow up on warm leads. Do NOT send new cold emails on Monday AM. |
| **Tuesday-Thursday** | Primary cold email send days. Enroll new contacts. Make calls 11 AM - 2 PM ET. |
| **Friday** | LinkedIn connection requests. Call attempts (analysts are looser on Fridays). Prep weekend sends. |
| **Saturday 8-10 AM** | Schedule email sends (analysts checking email during earnings season) |
| **Sunday 6-8 PM** | Schedule email sends (analysts prepping for the week) |

---

## Metrics to Track

| Metric | Target | Measured At |
|--------|--------|------------|
| **Open Rate** | >50% (subject line health) | Per sequence, per subject variant |
| **Reply Rate** | >5% (body copy + targeting health) | Per sequence, per body variant |
| **Positive Reply Rate** | >2% (interested, meeting booked, referral) | Per sequence |
| **Meeting Booked Rate** | >1.5% of enrolled contacts | Per sequence |
| **Contacts Enrolled / Week** | 50-75 (with personalization) | Weekly |

After 200+ sends per variant, compare reply rates and kill losing variants. Scale winners.
