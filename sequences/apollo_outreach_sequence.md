# Daloopa Outreach Sequences — Investment Firms
## Target Personas: Analyst, PM, Director of Research, Head of AI, Quant/Macro (separate)

> **Important:** Quant and Macro personas are EXCLUDED from the standard fundamental sequences below.
> They require a differentiated approach — see SEQUENCE 5 at the bottom.
> Per internal playbook: any title containing "Quant" or "Macro" goes to the Quant/Macro sequence only.

---

## Personalization Research (Do This BEFORE Enrolling)

For every prospect, gather the following before they enter a sequence:

### From ADV Brochure (SEC filing — links in broker_adv_links.csv):
- **AUM** — reference their scale ("managing $X billion")
- **Investment strategy** — long/short equity, event-driven, multi-strat, etc.
- **Sector focus** — if disclosed (tech, healthcare, industrials, etc.)
- **Team size** — number of investment professionals listed
- **Fee structure** — gives you a sense of sophistication and willingness to pay for tools

### From Company Website (domains in broker_adv_links.csv):
- **Portfolio focus areas** or stated investment philosophy
- **Recent news, blog posts, or thought leadership**
- **Tech stack signals** (do they mention data, AI, quantitative approaches?)

### From LinkedIn (prospect-level):
- **Current role and tenure** — how long at this firm
- **Previous firms** — did they come from a Daloopa customer? (Point72, Citadel, Cadian, XN, Thrivent, FTPartners)
- **Education** — finance vs. CS/engineering background shapes messaging
- **Recent posts or activity** — anything to reference as an opener
- **Sector coverage** — often listed in their headline or summary
- **Connections in common** — warm intro opportunity

### Custom Apollo Variables:
| Variable | Description | Example |
|---|---|---|
| `{{first_name}}` | Contact's first name | Sarah |
| `{{company}}` | Company name | Aristeia Capital |
| `{{title}}` | Job title | Senior Analyst |
| `{{sender_first_name}}` | Your first name | Edward |
| `{{custom1}}` | Sector coverage or strategy (from ADV/LinkedIn) | healthcare equities |
| `{{custom2}}` | Specific observation (from LinkedIn/ADV/website) | your TMT coverage |
| `{{custom3}}` | AUM or team size (from ADV) | $2.4B AUM |
| `{{custom4}}` | Previous firm or mutual connection | Point72 alum |

---

## A/B/C Subject Line Testing

For every **Step 1** (opening email), test three subject line variants:

- **Subject A:** Curiosity / context-driven (personalized to prospect's situation)
- **Subject B:** `Meeting Request | {{sender_first_name}} // {{first_name}}` (direct, professional, pattern-interrupt)
- **Subject C:** Internal camo — 2 words, Title Case, looks like an internal email (Lavender data: 60% more opens)

### Research-Backed Subject Line Rules (from Lavender, Berman, Braun, Coleman, 2025 data):
- **2 words is optimal** — 60% more opens than 5-word subjects (Lavender, millions of emails analyzed)
- **Title Case** outperforms lowercase by 30% (Lavender)
- **No questions** in subject lines — hurts open rate by 56% (Lavender)
- **No numbers** in subject lines — hurts open rate by 46% (Lavender)
- **No punctuation** — hurts open rate by 36% (Lavender)
- **First name in subject is debated** — Lavender says -12% replies, but 2025 aggregated data says +31% opens. Test both.
- **"Internal camo"** — make subject look like it came from inside their company, not a sales email (Lavender)
- **First line of body matters more than subject** for reply rates (Berman)
- **Best send time:** Thursday 9-11 AM ET = 44% open rate (2025 data)
- **"voicemail"** as a subject gets 40% response when paired with an actual voicemail left (Braun)

---

## A/B Email Body Testing

For every **Step 1** email, test two body styles:

- **Body Style A: "Problem-Agitate-Solve" (PAS)** — 4-6 sentences. Opens with personalized observation, names the pain, presents solution, asks for meeting. Establishes credibility and context. Best for prospects who need to understand *why* before they engage.

- **Body Style B: "3-Line Sniper"** — 3 sentences max, under 50 words total. Personalized opener → one-line value prop → soft CTA. No bullet points, no explanation. Creates curiosity gap — the prospect has to reply or take the meeting to learn more. Based on Lavender/Berman data: emails under 75 words get 2x reply rates.

Split 50/50 in Apollo. After 200+ sends per variant, compare **reply rates** (not just opens). Kill the loser, scale the winner.

**Rules for both styles:**
- First sentence must be personalized (ADV, LinkedIn, or website research) — never generic
- Never open with "I" — open with "you" or their name or an observation about their firm
- One CTA only — never give two asks
- No "I hope this email finds you well" or any throat-clearing
- Sign off with first name only — no title, no company, no phone number in the body

---

## SEQUENCE 1: Analysts

### Step 1 — Auto Email (Day 1)
**Subject A:** {{first_name}}, quick question about your models
**Subject B:** Meeting Request | {{sender_first_name}} // {{first_name}}
**Subject C:** Model Updates

**Body Style A (PAS):**

{{first_name}} — saw you're covering {{custom1}} at {{company}}.

Curious how you handle model updates after earnings. Most analysts I talk to at similar firms spend their Monday mornings manually pulling data from Friday's filings into Excel. Some are updating 50-80 models a quarter and losing hours to copy-paste.

We built something that automates that entirely — structured data from SEC filings, earnings, and supplements flows directly into your existing Excel models. No reformatting, no manual entry.

Worth a 15-minute look?

{{sender_first_name}}

**Body Style B (3-Line Sniper):**

{{first_name}} — saw you're covering {{custom1}} at {{company}}.

We automate the model update workflow after earnings — structured data from filings flows directly into your existing Excel models, no manual entry.

Open to a 15-minute walkthrough?

{{sender_first_name}}

### Step 2 — Auto Email (Day 3)
**Subject:** re: your {{custom1}} models

{{first_name}} — quick follow-up.

Here's what it looks like in practice:
- Earnings come out → your model updates automatically
- 10-K/10-Q filed → new data flows into your existing templates
- No copy-paste, no manual errors, no lag

Happy to show you a live demo on one of your current coverage names. Would that be useful?

{{sender_first_name}}

### Step 3 — LinkedIn Connection Request (Day 5)
Hi {{first_name}} — saw you're covering {{custom1}} at {{company}}. I work with analysts at funds like yours on automating the tedious parts of model maintenance. Would love to connect.

### Step 4 — Auto Email (Day 8)
**Subject:** the monday morning earnings backlog

{{first_name}} — most analysts I talk to describe the same problem: earnings season hits, and suddenly you're buried in filings across your entire coverage universe, updating models one-by-one.

We cover 4,000+ public companies. Structured data delivered into Excel in whatever format your models already use. You sit down Monday morning and everything is current.

If model maintenance is eating into your analysis time, I'd love to show you how we fix that.

{{sender_first_name}}

### Step 5 — Manual Email (Day 14)
**Subject:** one more thought

{{first_name}} — if automating model updates ever becomes a priority at {{company}}, I'm an easy person to reach.

{{sender_first_name}}

---

## SEQUENCE 2: Portfolio Managers (PMs)

### Step 1 — Auto Email (Day 1)
**Subject A:** your analysts' time
**Subject B:** Meeting Request | {{sender_first_name}} // {{first_name}}
**Subject C:** Analyst Capacity

**Body Style A (PAS):**

{{first_name}} — looked at {{company}}'s ADV. With {{custom3}}, your team is covering a lot of ground.

Curious how much of your analysts' week goes to model maintenance vs. actual analysis. At most funds I talk to, the answer is uncomfortable — analysts spending 30-40% of their time pulling data from filings into Excel instead of generating insight.

We automate that entirely. Structured fundamental data from SEC filings, earnings, and supplements delivered directly into your team's existing models. No reformatting. Your analysts get that time back for the work that actually moves the needle.

Would a quick call make sense?

{{sender_first_name}}

**Body Style B (3-Line Sniper):**

{{first_name}} — looked at {{company}}'s ADV. With {{custom3}}, your team is covering serious ground.

We help funds like yours give analysts back the 30-40% of their week currently lost to pulling filing data into models manually.

Open to a quick call to see if it's relevant?

{{sender_first_name}}

### Step 2 — Auto Email (Day 4)
**Subject:** re: your analysts' time

{{first_name}} — following up briefly.

The math is simple:
- Your analysts spend less time on maintenance, more on insight
- Model data is updated faster after filings — no lag, no errors
- Coverage breadth can expand without adding headcount

Would it make sense to loop in whoever runs the models for a quick demo?

{{sender_first_name}}

### Step 3 — Phone Call Task (Day 7)
**Call Script:**
Hi {{first_name}}, this is {{sender_first_name}} from Daloopa. I sent a couple of emails about your team's workflow around model updates. We work with investment teams to eliminate the manual data pull from filings and earnings — the goal is to give your analysts more time for actual analysis rather than data entry. Would you have 15 minutes this week to see how it works?

### Step 4 — Auto Email (Day 10)
**Subject:** quick question

{{first_name}} — curious how your team currently handles model updates after earnings.

If it's still largely manual, there's a way to get that time back for your analysts. Happy to do a no-pressure walkthrough with whoever runs the models.

{{sender_first_name}}

### Step 5 — LinkedIn Message (Day 14)
Hi {{first_name}} — I work with PMs at funds like {{company}} to help their analysts spend less time on model maintenance and more on generating ideas. Worth a quick chat?

### Step 6 — Manual Email (Day 18)
**Subject:** leaving the door open

{{first_name}} — if your team ever wants to explore automating the model update workflow, happy to pick this back up.

{{sender_first_name}}

---

## SEQUENCE 3: Directors of Research

### Step 1 — Auto Email (Day 1)
**Subject A:** expanding coverage without adding headcount
**Subject B:** Meeting Request | {{sender_first_name}} // {{first_name}}
**Subject C:** Research Coverage

**Body Style A (PAS):**

{{first_name}} — been looking at {{company}}'s setup. Running a research team always comes down to the same tradeoff: depth of analysis vs. breadth of coverage. And model maintenance is usually what tips the scale.

We automate the extraction and delivery of fundamental data from SEC filings, earnings, and supplements directly into your team's Excel models. Your analysts spend less time on data entry and more time doing the work they were hired for.

Firms in a similar position to {{company}} have expanded coverage without adding analysts. Would a 15-minute demo be worth exploring?

{{sender_first_name}}

**Body Style B (3-Line Sniper):**

{{first_name}} — noticed {{company}} is running a lean research team relative to your coverage universe.

We help research teams expand coverage without adding headcount by automating the model update workflow after filings and earnings.

Worth 15 minutes to see how it works?

{{sender_first_name}}

### Step 2 — Auto Email (Day 3)
**Subject:** re: expanding coverage

{{first_name}} — to make it concrete: after an earnings release, updated financials flow into your team's models automatically. No manual pulling from filings, no copy-paste errors, no lag.

We cover 4,000+ public companies across all major sectors.

Would it help to see this in action on a name your team currently covers?

{{sender_first_name}}

### Step 3 — Phone Call Task (Day 6)
**Call Script:**
Hi {{first_name}}, this is {{sender_first_name}} from Daloopa. We help research teams at investment firms automate their financial model updates — structured data from filings and earnings delivered directly into Excel. Directors of research I've spoken with say it's freed up significant analyst capacity. Do you have 15 minutes to see a quick demo?

### Step 4 — Auto Email (Day 9)
**Subject:** what {{company}}'s workflow could look like

{{first_name}} — imagine this: earnings drop, and within hours your models are updated. No analyst time spent.

I'd love to show you how it could fit into your team's workflow. Would you or someone on your team have time for a brief walkthrough?

{{sender_first_name}}

### Step 5 — LinkedIn Message (Day 12)
Hi {{first_name}} — I help research leaders at investment firms scale coverage using AI-powered data automation. Thought it might be relevant given what you're building at {{company}}.

### Step 6 — Manual Email (Day 16)
**Subject:** one last thought

{{first_name}} — if expanding coverage or reducing model maintenance time is ever on the roadmap at {{company}}, happy to pick this back up.

{{sender_first_name}}

---

## SEQUENCE 4: Heads of AI / Technology

### Step 1 — Auto Email (Day 1)
**Subject A:** {{company}}'s data infrastructure
**Subject B:** Meeting Request | {{sender_first_name}} // {{first_name}}
**Subject C:** Data Pipeline

**Body Style A (PAS):**

{{first_name}} — saw your background. Given your role at {{company}}, I'm guessing your team is either building or evaluating AI tools for the investment workflow.

We've built something that sits at that intersection: machine learning that extracts and structures fundamental data from SEC filings, earnings, and supplements. Clean, standardized data available via:
- API (8 endpoints + real-time Webhooks)
- MCP — lets your LLMs query our data natively through Claude or OpenAI, no custom connectors
- 1,200+ standardized Taxonomy metrics for cross-company analysis

If you're evaluating data infrastructure for the research team, this could save significant engineering time. Worth a conversation?

{{sender_first_name}}

**Body Style B (3-Line Sniper):**

{{first_name}} — saw your background at {{company}}. Guessing you're either building or evaluating AI tools for the investment workflow.

We provide structured fundamental data via API and MCP — your LLMs can query 4,000+ tickers of filing data natively, no custom connectors or internal parsing needed.

Worth a technical conversation?

{{sender_first_name}}

### Step 2 — Auto Email (Day 4)
**Subject:** re: data infrastructure

{{first_name}} — quick follow-up with specifics.

Under the hood:
- NLP extraction from 10-K, 10-Q, earnings transcripts, and supplements
- Structured output mapped to 1,200+ standardized Taxonomy metrics
- 4,000+ company coverage with historical data
- 8 API endpoints + real-time Webhooks for automated pipeline updates
- MCP integration — your Claude or OpenAI agents can query our data natively
- Keyword Search across filings (beta)

If your team is building AI-powered research tools or data pipelines, this could replace months of engineering work.

{{sender_first_name}}

### Step 3 — LinkedIn Connection Request (Day 7)
Hi {{first_name}} — saw your work at {{company}} on the data/AI side. We're building ML-powered financial data extraction that integrates via API and MCP. Thought it'd be relevant to connect.

### Step 4 — Auto Email (Day 11)
**Subject:** build vs. buy

{{first_name}} — most firms I talk to have considered building their own extraction pipeline for financial data. Some do — but most find the edge cases (tables, footnotes, non-standard formats) make it far more complex than expected.

We've spent years solving those edge cases across 4,000+ tickers. If your team is evaluating this space, I'd welcome a technical conversation.

{{sender_first_name}}

### Step 5 — Manual Email (Day 16)
**Subject:** open invite

{{first_name}} — if AI-driven data infrastructure is ever a priority at {{company}}, happy to do a technical deep-dive whenever it makes sense.

{{sender_first_name}}

---

## SEQUENCE 5: Quant / Macro (Differentiated Approach)

> **Why separate?** Quant and Macro professionals don't build bottom-up fundamental models the way traditional L/S equity analysts do. They care about structured data feeds, API access, signal generation, and systematic integration — not Excel model updates. The messaging must reflect their workflow.

### Step 1 — Auto Email (Day 1)
**Subject A:** replacing your internal filing parser
**Subject B:** Meeting Request | {{sender_first_name}} // {{first_name}}
**Subject C:** Filing Parser

**Body Style A (PAS):**

{{first_name}} — most quant teams I talk to at firms like {{company}} have either built or are maintaining an internal pipeline for extracting fundamental data from SEC filings. And it's a constant headache.

We provide a clean, structured fundamental data feed extracted from filings, earnings, and supplements using AI:
- Point-in-time accurate (no look-ahead bias)
- 1,200+ standardized metrics via Taxonomy — consistent field names across companies
- API (8 endpoints) with Webhooks that notify you the moment new actuals publish
- Direct pipeline integration — no manual downloads

If your team ingests fundamental data for factor models, signals, or systematic strategies, this could replace a meaningful chunk of internal infrastructure.

Worth a quick technical conversation?

{{sender_first_name}}

**Body Style B (3-Line Sniper):**

{{first_name}} — guessing {{company}} has either built or is maintaining an internal parser for SEC filings. Most quant teams I talk to say it's a constant headache.

We provide point-in-time fundamental data via API — 1,200+ standardized metrics, real-time Webhooks, no look-ahead bias. Plugs directly into your pipeline.

Worth a quick technical chat to compare?

{{sender_first_name}}

### Step 2 — Auto Email (Day 4)
**Subject:** re: your data pipeline

{{first_name}} — following up with specifics.

What systematic teams typically use us for:
- Alternative to building internal NLP pipelines for financial document parsing
- Point-in-time fundamental data for backtesting without survivorship or look-ahead bias
- 1,200+ standardized Taxonomy metrics — fetch comparable datapoints across companies
- Real-time Webhooks — get notified the moment we publish new actuals
- 8 API endpoints — programmatic access to all data points, metadata, and source documents
- MCP integration — for teams building LLM/AI-powered research tools

Teams spending engineering resources on parsing 10-Ks and earnings supplements get significant time back by plugging in instead.

Would it help to see sample API output? I can pull a TSLA example to show the format.

{{sender_first_name}}

### Step 3 — LinkedIn Connection Request (Day 7)
Hi {{first_name}} — I work with quant teams on structured fundamental data feeds. AI-extracted, point-in-time, API-delivered. Thought it might be relevant to what you're building at {{company}}.

### Step 4 — Auto Email (Day 10)
**Subject:** the edge case problem

{{first_name}} — most quant firms I talk to have tried building their own parser for SEC filings. The challenge is always the same: edge cases in tables, footnotes, restatements, and non-standard formats make it a multi-year engineering project.

We've been solving those edge cases across 4,000+ tickers. Our data is used by both fundamental and systematic teams.

If your team is evaluating data infrastructure for fundamental inputs, I'd welcome a technical deep-dive.

{{sender_first_name}}

### Step 5 — Auto Email (Day 14)
**Subject:** sample output for your team

{{first_name}} — rather than more emails, I can send over:
- Sample API output for a ticker your team covers
- Data schema and field mappings
- Point-in-time data methodology documentation

If any of that would be useful, just let me know a ticker and I'll pull it together.

{{sender_first_name}}

### Step 6 — Manual Email (Day 19)
**Subject:** open door

{{first_name}} — if {{company}} ever evaluates external fundamental data feeds for systematic strategies, happy to pick this back up.

{{sender_first_name}}

---

## Apollo Filter Notes for Quant/Macro Sequence

When adding contacts to this sequence in Apollo, use these filters:
- **Job Title CONTAINS:** Quant, Quantitative, Macro, Systematic, Data Scientist, Data Engineer, Quant Researcher, Quant Developer, Quantitative Analyst, Quantitative PM
- **EXCLUDE from** Sequences 1-4 (Analyst, PM, Director of Research, Head of AI)
- These contacts should ONLY go into this Quant/Macro sequence

---

## Apollo Setup Instructions

### Step 1: Create Sequences
1. Go to **Engage → Sequences → + New Sequence**
2. Create **5 sequences** (one per persona above)
3. For each sequence, create **2 variants** of Step 1 (Body Style A and Body Style B)
4. Name them accordingly

### Step 2: Add Steps
For each sequence, add steps matching the templates above:
- **Automatic Email** — sends automatically on schedule
- **Manual Email** — creates a task for you to review before sending
- **Phone Call** — creates a call task with the script
- **LinkedIn** — creates a LinkedIn task (connection request or message)

Set wait days between steps as noted (Day 1, Day 3, Day 5, etc.)

**Timing:**
- **Emails:** Schedule for 7:00-8:30 AM ET or 6:00-7:00 PM ET
- **Call tasks:** 11:00 AM - 2:00 PM ET (analyst downtime window). Fridays are bonus.
- **LinkedIn:** Before 8:30 AM or after 6:00 PM — analysts don't browse LinkedIn at their desk.

### Step 3: Personalize Before Enrolling
**This is critical.** Before adding any contact to a sequence:
1. Pull their firm's **ADV brochure** (links in `broker_adv_links.csv`) — get AUM, strategy, team size
2. Check their **company website** (domains in `broker_adv_links.csv`) — investment philosophy, sector focus
3. Check their **LinkedIn** — sector coverage, tenure, previous firms, recent activity
4. Populate `{{custom1}}` through `{{custom4}}` in Apollo with this research

### Step 4: Add Contacts via Apollo Search
Search for contacts at your target accounts using:
- **Job Titles:** Analyst, Research Analyst, Senior Analyst, Associate, Portfolio Manager, Director of Research, Head of AI, CTO, Head of Data
- **Company domains:** from `broker_adv_links.csv`
- **EXCLUDE** any title containing Quant or Macro from sequences 1-4

### Step 5: Activate & Measure
- Split A/B evenly on Step 1 body copy (Style A vs Style B)
- Split A/B/C on subject lines
- After 200+ sends per variant, compare **reply rates**
- Kill losers, scale winners
- Review and assign to your mailbox, then activate each sequence.
