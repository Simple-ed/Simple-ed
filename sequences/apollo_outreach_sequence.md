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

## SEQUENCE 1: Analysts

### Step 1 — Auto Email (Day 1)
**Subject:** {{first_name}}, quick question about your models

Hi {{first_name}},

I noticed you're covering {{custom1}} at {{company}} — curious how your team handles model updates after earnings.

Most analysts I talk to at similar firms spend their Monday mornings manually pulling data from Friday's filings into Excel. Some are updating 50-80 models a quarter and losing hours to copy-paste.

We built something that automates that entirely — structured data from SEC filings, earnings, and supplements flows directly into your existing Excel models. No reformatting, no manual entry.

Worth a 15-minute look?

Best,
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

{{first_name}},

I'll keep this short — most analysts I talk to describe the same problem: earnings season hits, and suddenly you're buried in filings across your entire coverage universe, updating models one-by-one.

We cover 4,000+ public companies. Structured data delivered into Excel in whatever format your models already use. You sit down Monday morning and everything is current.

If model maintenance is eating into your analysis time, I'd love to show you how we fix that.

{{sender_first_name}}

### Step 5 — Manual Email (Day 14)
**Subject:** one more thought

{{first_name}},

I'll leave it here — but if automating model updates ever becomes a priority at {{company}}, I'm an easy person to reach.

All the best,
{{sender_first_name}}

---

## SEQUENCE 2: Portfolio Managers (PMs)

### Step 1 — Auto Email (Day 1)
**Subject:** your analysts' time

Hi {{first_name}},

I looked at {{company}}'s ADV — with {{custom3}}, your team is covering a lot of ground. Curious how much of your analysts' week goes to model maintenance vs. actual analysis.

At most funds I talk to, the answer is uncomfortable. Analysts are spending 30-40% of their time pulling data from filings into Excel instead of generating insight.

We automate that entirely. Structured fundamental data from SEC filings, earnings, and supplements delivered directly into your team's existing models. No reformatting. Your analysts get that time back for the work that actually moves the needle.

Would a quick call make sense?

Best,
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

{{first_name}},

Curious — how does your team currently handle model updates after earnings? If it's still largely manual, there's a way to get that time back for your analysts.

Happy to do a no-pressure walkthrough with whoever runs the models.

{{sender_first_name}}

### Step 5 — LinkedIn Message (Day 14)
Hi {{first_name}} — I work with PMs at funds like {{company}} to help their analysts spend less time on model maintenance and more on generating ideas. Worth a quick chat?

### Step 6 — Manual Email (Day 18)
**Subject:** leaving the door open

{{first_name}},

I understand timing matters. If your team ever wants to explore automating the model update workflow, happy to pick this back up.

{{sender_first_name}}

---

## SEQUENCE 3: Directors of Research

### Step 1 — Auto Email (Day 1)
**Subject:** expanding coverage without adding headcount

Hi {{first_name}},

I've been looking at {{company}}'s setup — running a research team always comes down to the same tradeoff: depth of analysis vs. breadth of coverage. And model maintenance is usually what tips the scale.

We automate the extraction and delivery of fundamental data from SEC filings, earnings, and supplements directly into your team's Excel models. The result: your analysts spend less time on data entry and more time doing the work they were hired for.

Firms in a similar position to {{company}} have expanded coverage without adding analysts. Would a 15-minute demo be worth exploring?

Best,
{{sender_first_name}}

### Step 2 — Auto Email (Day 3)
**Subject:** re: expanding coverage

{{first_name}},

To make it concrete — after an earnings release, updated financials flow into your team's models automatically. No manual pulling from filings, no copy-paste errors, no lag.

We cover 4,000+ public companies across all major sectors.

Would it help to see this in action on a name your team currently covers?

{{sender_first_name}}

### Step 3 — Phone Call Task (Day 6)
**Call Script:**
Hi {{first_name}}, this is {{sender_first_name}} from Daloopa. We help research teams at investment firms automate their financial model updates — structured data from filings and earnings delivered directly into Excel. Directors of research I've spoken with say it's freed up significant analyst capacity. Do you have 15 minutes to see a quick demo?

### Step 4 — Auto Email (Day 9)
**Subject:** what {{company}}'s workflow could look like

{{first_name}},

Imagine this: earnings drop, and within hours your models are updated — no analyst time spent.

I'd love to show you how it could fit into your team's workflow. Would you or someone on your team have time for a brief walkthrough?

{{sender_first_name}}

### Step 5 — LinkedIn Message (Day 12)
Hi {{first_name}} — I help research leaders at investment firms scale coverage using AI-powered data automation. Thought it might be relevant given what you're building at {{company}}.

### Step 6 — Manual Email (Day 16)
**Subject:** one last thought

{{first_name}},

If expanding coverage or reducing model maintenance time is ever on the roadmap at {{company}}, happy to pick this back up.

All the best,
{{sender_first_name}}

---

## SEQUENCE 4: Heads of AI / Technology

### Step 1 — Auto Email (Day 1)
**Subject:** {{company}}'s data infrastructure

Hi {{first_name}},

I saw your background — given your role at {{company}}, I'm guessing your team is either building or evaluating AI tools for the investment workflow.

We've built something that sits at that intersection: machine learning that extracts and structures fundamental data from SEC filings, earnings, and supplements. The output is clean, standardized data available via:
- **API** (8 endpoints + real-time Webhooks)
- **MCP** — lets your LLMs query our data natively through Claude or OpenAI, no custom connectors needed
- **1,200+ standardized Taxonomy metrics** for cross-company analysis

If you're evaluating data infrastructure for the research team, this could save significant engineering time. Worth a conversation?

Best,
{{sender_first_name}}

### Step 2 — Auto Email (Day 4)
**Subject:** re: data infrastructure

{{first_name}} — quick follow-up with specifics.

Under the hood:
- NLP extraction from 10-K, 10-Q, earnings transcripts, and supplements
- Structured output mapped to 1,200+ standardized Taxonomy metrics
- 4,000+ company coverage with historical data
- **8 API endpoints** + **real-time Webhooks** for automated pipeline updates
- **MCP integration** — your Claude or OpenAI agents can query our data natively, no hallucinated financials
- Keyword Search across filings (beta)

If your team is building AI-powered research tools or data pipelines, this could replace months of engineering work.

{{sender_first_name}}

### Step 3 — LinkedIn Connection Request (Day 7)
Hi {{first_name}} — saw your work at {{company}} on the data/AI side. We're building ML-powered financial data extraction that integrates via API and MCP. Thought it'd be relevant to connect.

### Step 4 — Auto Email (Day 11)
**Subject:** build vs. buy

{{first_name}},

Most firms I talk to have considered building their own extraction pipeline for financial data. Some do — but most find the edge cases (tables, footnotes, non-standard formats) make it far more complex than expected.

We've spent years solving those edge cases across 4,000+ tickers. If your team is evaluating this space, I'd welcome a technical conversation.

{{sender_first_name}}

### Step 5 — Manual Email (Day 16)
**Subject:** open invite

{{first_name}},

If AI-driven data infrastructure is ever a priority at {{company}}, I'd welcome the conversation. Happy to do a technical deep-dive whenever it makes sense.

{{sender_first_name}}

---

## SEQUENCE 5: Quant / Macro (Differentiated Approach)

> **Why separate?** Quant and Macro professionals don't build bottom-up fundamental models the way traditional L/S equity analysts do. They care about structured data feeds, API access, signal generation, and systematic integration — not Excel model updates. The messaging must reflect their workflow.

### Step 1 — Auto Email (Day 1)
**Subject:** replacing your internal filing parser

Hi {{first_name}},

I'm reaching out because most quant teams I talk to at firms like {{company}} have either built or are maintaining an internal pipeline for extracting fundamental data from SEC filings — and it's a constant headache.

We provide a clean, structured fundamental data feed extracted from filings, earnings, and supplements using AI:
- Point-in-time accurate (no look-ahead bias)
- 1,200+ standardized metrics via Taxonomy — consistent field names across companies for factor and comp analysis
- API (8 endpoints) with Webhooks that notify you the moment new actuals are published
- Direct pipeline integration — no manual downloads

If your team ingests fundamental data for factor models, signals, or systematic strategies, this could replace a meaningful chunk of internal infrastructure.

Worth a quick technical conversation?

Best,
{{sender_first_name}}

### Step 2 — Auto Email (Day 4)
**Subject:** re: your data pipeline

{{first_name}} — following up with specifics.

What systematic teams typically use us for:
- **Alternative to building internal NLP pipelines** for financial document parsing
- **Point-in-time fundamental data** for backtesting without survivorship or look-ahead bias
- **1,200+ standardized Taxonomy metrics** — fetch comparable datapoints across companies for factor and comp analysis
- **Real-time Webhooks** — get notified the moment we publish new actuals, so your pipelines update automatically
- **8 API endpoints** — programmatic access to all data points, metadata, and source documents
- **MCP integration** — for teams building LLM/AI-powered research tools

Teams spending engineering resources on parsing 10-Ks and earnings supplements get significant time back by plugging in instead.

Would it help to see sample API output or discuss data schema? I can pull a TSLA example to show the format.

{{sender_first_name}}

### Step 3 — LinkedIn Connection Request (Day 7)
Hi {{first_name}} — I work with quant teams on structured fundamental data feeds. AI-extracted, point-in-time, API-delivered. Thought it might be relevant to what you're building at {{company}}.

### Step 4 — Auto Email (Day 10)
**Subject:** the edge case problem

{{first_name}},

Most quant firms I talk to have at some point tried to build their own parser for SEC filings. The challenge is always the same — edge cases in tables, footnotes, restatements, and non-standard formats make it a multi-year engineering project.

We've been solving those edge cases across 4,000+ tickers. Our data is used by both fundamental and systematic teams.

If your team is evaluating data infrastructure for fundamental inputs, I'd welcome a technical deep-dive.

{{sender_first_name}}

### Step 5 — Auto Email (Day 14)
**Subject:** sample output for your team

{{first_name}},

Rather than more emails — I can send over:
- Sample API output for a ticker your team covers
- Our data schema and field mappings
- Point-in-time data methodology documentation

If any of that would be useful, just let me know a ticker and I'll pull it together.

{{sender_first_name}}

### Step 6 — Manual Email (Day 19)
**Subject:** open door

{{first_name}},

If {{company}} ever evaluates external fundamental data feeds for systematic strategies, happy to pick this back up. Clean extraction, standardized output, API delivery, point-in-time accuracy.

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
3. Name them accordingly

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

### Step 5: Activate
Review, assign to your mailbox, and activate each sequence.
