# Daloopa Target Personas — Detailed Profiles

---

## PERSONA 1: Long Short Hedge Fund Analyst / Associate
**AKA:** Multi-managers, Pods

**Description:** Analyst or associate at a fund/pod covering an entire sector. Maintains models for 50-80 companies with hundreds to thousands of rows. Trades very frequently, especially around earnings — must keep models very updated.

**Challenges:**
- Difficulty keeping earnings backlog updated during earnings season
- High number of models in the same sector = they all report around the same time
- Hard to maintain data quality and model complexity under time pressure
- Working very late doing data entry instead of making trading decisions

**Requirements:**
- Accurate and fast updating around quarterly earnings
- Comprehensive data
- Data available for the sector they cover

**Key Quote:**
> "I hate to admit it, but I dislike writing earnings previews and postviews. They take a long time, and are glorified summaries of what has happened. The faster I can get my model updated the faster I can write a postview."

**Current Customers:** Point72, Citadel/Surveyor/Ashler, Cadian

**Sample Prospects:** Millennium, Balyasny, ExodusPoint, Cinctive, Crestline

---

## PERSONA 2: Long Biased Hedge Fund Analyst / Associate
**AKA:** Tiger Global, Tiger Cubs, Tiger Seeds, Growth Investors

**Description:** Analyst or associate maintaining generally fewer than 80 models. Positions tend to be very concentrated with low turnover. Strive to know one company very well, including context on competitors. May build models that don't end up in portfolio. Often initiate new coverage to explore new companies.

**Challenges:**
- Building models as complex as preferred is painful because they're hard to update later
- Disorienting to update models across different industries
- Building new models is very time consuming and mind numbing
- Sometimes too tired from data input to actually think about the numbers
- Sellside or inherited models are annoying to update
- Need both easy model building AND easy updating of complicated models

**Requirements:**
- Comprehensive and detailed data
- Organized models to pull from
- Large model database
- Flexibility and easy integration into existing models

**Key Quote:**
> "I need to have a good understanding of an industry before I look at a business. Ideally I would have industry models built and maintained, but they take too long so I wait for the next quarter to do it…"

**Current Customers:** XN

**Sample Prospects:** Tiger Global, Lone Pine

---

## PERSONA 3: Mutual Fund Long Only Analyst

**Description:** Analyst at a mutual fund maintaining long-term positions. Models are not as intensive, often built on top of sell-side models. Research budget is significantly less than hedge funds.

**Challenges:**
- Maintaining work-life balance is very important
- Not focused on trading around earnings — longer term positions
- Analysis and models not as in depth
- Layers analysis on top of existing sell-side models
- Sell-side models can be complicated and painful to update

**Requirements:**
- Easy to use tool that works on complex sell-side models

**Key Quote:**
> "I always feel that the HFs get more resources than I do. The playing field isn't fair. I wish I had their armies of analysts."

**Current Customers:** Thrivent

**Sample Prospects:** Franklin Templeton, Fidelity, Vanguard, Invesco, Blackrock, Charles Schwab, Capital Group

---

## PERSONA 4: Equity Research / Sellside Analyst

> **NOTE: NOT IN SCOPE.** Daloopa's current outreach focuses exclusively on buy-side accounts. Sellside is excluded from all Apollo sequences and target account lists. Keeping this persona for reference only.

**Current Customers:** FTPartners

**Sample Prospects (out of scope):** JP Morgan, BoA, Goldman Sachs, Morgan Stanley, Jefferies

---

## PERSONA 5: Long Short PM / CIO / Director of Research

**Description:** PM/CIO/DoR at a trading-intense, high turnover, market neutral fund. Responsible for making sizing decisions off analyst input. Needs high trust in analyst work to avoid double-checking.

**Challenges:**
- Analysts spending too much time updating extensive models
- Running out of time for quick trading decisions
- Need faster work during earnings season
- Want decision making from analysts they can trust

**Requirements:**
- Verified data that updates quickly

**Key Quote:**
> "My analysts are good at tracking companies, but it is my job to track industry movements. I also need them to move faster through models so we can spend more time actually thinking about the companies and the space."

**Current Customers:** Point72, Citadel/Surveyor/Ashler, Cadian

---

## PERSONA 6: Long Biased PM / CIO / Director of Research

**Description:** PM/CIO/DoR at a highly concentrated, generally TMT-focused fund. Reviews analyst work and has final say on sizing. Wants analysts to spend time on fundamental research rather than data entry.

**Challenges:**
- Need analysts to build/modify models for new positions quickly before opportunity passes
- Positions take time to build, so speed matters
- Must trust the data given how significant holdings are and how hard it is to maneuver sizing
- Need analysts doing deep fundamental research (management calls, sellside experts, industry analysts) not data entry
- Want analysts familiar with competitors and their numbers

**Requirements:**
- Easy model building that can be trusted
- Idea generation

**Key Quote:**
> "I need to look good in front of LPs. Part of how I do that is to show off the level of technology, process, and sophistication of our product. My LPs love charts that tell a story, the more industry level charts I can put together and update, the better I look, the more money we raise."

**Current Customers:** XN

---

## PERSONA 7: Quantitative Researcher / Systematic Analyst
**AKA:** Quantitative Analyst, Quant Researcher, Data Scientist (at hedge fund), Quantitative PM, Systematic Trader, Macro Quant Strategist, Quantitative Developer

**Description:** Quantitative researchers at buy-side firms develop and backtest systematic trading strategies using mathematical models, ML, and statistical analysis. Unlike fundamental analysts who rely on qualitative judgment, quants systematically aggregate large datasets to identify predictive signals — all information must be structured, programmatic, and free from subjective interpretation. They combine fundamental data (earnings, financial statements, macro indicators) with technical signals to build multi-layered trading models deployed at scale.

**Challenges:**
- Point-in-time data integrity — vendors often backfill restatements, creating look-ahead bias that invalidates backtests and destroys model reliability
- SEC filing parsing and automation — manual extraction from 10-Ks, 10-Qs, and 8-Ks is error-prone; building internal EDGAR scrapers is resource-intensive and requires constant maintenance
- Data normalization across vendors — inconsistent taxonomies, field names, and calculation methodologies require extensive cleaning pipelines
- Latency in filing alerts — delays in new filing notifications cause missed systematic trading signals
- Any manual workflow breaks systematic strategies and introduces inconsistency
- Legacy platforms designed for terminal users (not API consumers) create friction for quant infrastructure integration

**Requirements:**
- API-first delivery with clean, documented endpoints (REST, Python, R compatible)
- Structured, normalized data with standardized taxonomy across all tickers and time periods
- Point-in-time snapshots — only information available at historical dates, no backfill contamination
- Real-time webhooks for new SEC filings and data updates
- Zero manual workflows — 100% automation from data ingestion to model deployment
- 99%+ accuracy to eliminate data quality as a source of alpha decay

**Key Quote:**
> "Look-ahead bias is the silent killer. If my backtest shows alpha but the vendor gave me information that wasn't available in 2019, I've wasted months on a model that will fail in production. I need point-in-time integrity, automated filing alerts, and API delivery — no spreadsheets, no guessing whether a restatement corrupted my training set."

**Current Alternatives:** Bloomberg API (expensive, terminal-centric), Capital IQ/Compustat (inconsistent point-in-time handling), FactSet APIs (comprehensive but costly), internal EDGAR scrapers (resource-intensive), WRDS academic datasets (limited real-time), custom Python parsers via sec-api.io

**Sample Prospects:** Two Sigma, D.E. Shaw, AQR Capital Management, Bridgewater Associates, Citadel (Quantitative Strategies), Man Group, Millennium (systematic pods), PDT Partners, Voleon Group, WorldQuant, Element Capital

**Daloopa Use Case:** API-first with 8 endpoints delivers structured data directly into Python/R pipelines. Webhook alerts on new SEC filings enable zero-latency signal generation. 1,200+ standardized taxonomy provides consistent field definitions across 5,000+ tickers. 99%+ accuracy and point-in-time data integrity eliminate look-ahead bias. MCP integration enables LLM-powered queries against structured fundamental data. Replaces the "scrape EDGAR → parse → clean → pray it's correct" workflow with a single API call.

---

## PERSONA 8: Head of AI / Head of Technology / Chief Data Officer
**AKA:** CTO, Chief Data Officer, Head of Data Science, VP of Technology, Head of Research Infrastructure, Head of Data Engineering, Head of Quantitative Technology, Director of Technology

**Description:** Technology and data infrastructure leaders who evaluate, build, and maintain the data/tech stack powering the investment team. They make build-vs-buy decisions for data pipelines, manage vendor relationships, oversee API integrations, and lead LLM/AI adoption for investment research workflows. They balance engineering resources between maintaining internal systems and integrating external tools.

**Challenges:**
- Build vs. buy decisions — evaluating whether to build internal data extraction pipelines or purchase vendor solutions; internal builds routinely expand from 6-month estimates to multi-year commitments due to edge cases in financial document parsing
- Data quality standards — ensuring point-in-time accuracy, eliminating look-ahead bias, maintaining 99%+ thresholds across thousands of companies
- Integration complexity — managing API integrations across Bloomberg, Capital IQ, FactSet, and custom systems with inconsistent schemas
- Data normalization burden — handling XBRL extensions and non-standard financial statement line items across industries
- Reducing engineering burden — teams constantly maintaining EDGAR scrapers, dealing with parsing failures on restatements, footnotes, and table formats
- LLM/AI adoption — enabling investment teams to leverage Claude/OpenAI for research while ensuring data accuracy (LLMs hallucinate financial data ~50% of the time without structured sources)
- Scaling infrastructure without proportional headcount increases

**Requirements:**
- API-first architecture with comprehensive documentation, SDK support, and clear versioning
- Structured, standardized output — consistent taxonomy across companies, machine-readable JSON/CSV
- Data quality guarantees — published accuracy rates (99%+), QA processes, validation checks
- Point-in-time data — no look-ahead bias for backtesting integrity
- Real-time webhooks — instant notifications on new filings, no polling required
- LLM/AI readiness — MCP support for Claude/OpenAI, native agentic workflow integration
- Clear ROI vs. internal build cost — pricing that justifies replacing 2-3 FTE of scraper maintenance

**Key Quote:**
> "We've looked at building this ourselves three times. Each time, the edge cases around non-standard table formats and restatements push it from a 6-month project to a multi-year engineering commitment. At some point you have to ask whether maintaining an internal EDGAR scraper is really where our engineering talent should spend their time."

**Current Alternatives:** Internal engineering teams building custom EDGAR scrapers, Bloomberg Terminal API (expensive per-seat), Capital IQ feeds (significant normalization needed), FactSet via API (integration overhead), open-source NLP projects for parsing 10-Ks (high maintenance, accuracy issues), XBRL direct from SEC (free but requires extensive parsing infrastructure)

**Sample Prospects:** Point72, Citadel, Two Sigma, Millennium Management, Balyasny Asset Management, Bridgewater Associates, Man Group / AHL, Marshall Wace, ExodusPoint, Squarepoint Capital, D.E. Shaw, Schonfeld Strategic Advisors

**Daloopa Use Case:** Replaces months/years of internal engineering — no more maintaining EDGAR parsers or debugging extraction failures on edge cases. API-first with 8 endpoints reduces integration time from months to weeks. MCP integration enables agentic research workflows with Claude/OpenAI without custom connector development. 1,200+ taxonomy eliminates normalization work. Webhooks feed event-driven architectures. 99%+ accuracy reduces QA burden. Clear ROI: typically replaces 2-3 FTE of data engineering ($300K-$600K annually) plus analyst time savings of ~2 days per analyst per earnings season.

---

## Apollo Targeting Summary by Persona

| Persona | Job Titles to Search | Sequence |
|---|---|---|
| L/S HF Analyst | Analyst, Research Analyst, Senior Analyst, Associate, Senior Associate | **Sequence 1A (L/S Analyst)** |
| Long Biased HF Analyst | Analyst, Research Analyst, Senior Analyst, Associate | **Sequence 1B (Long Biased Analyst)** |
| Mutual Fund Analyst | Analyst, Research Analyst, Associate | **Sequence 1C (Mutual Fund Analyst)** |
| Sellside / ER Analyst | ~~OUT OF SCOPE~~ | N/A |
| L/S PM / CIO / DoR | Portfolio Manager, CIO, Director of Research, Partner, Principal | Sequence 2 (PM) / Sequence 3 (DoR) |
| Long Biased PM / CIO / DoR | Portfolio Manager, CIO, Director of Research, Partner | Sequence 2 (PM) / Sequence 3 (DoR) |
| Quant / Macro | Quantitative Analyst, Quant Researcher, Macro Strategist, Systematic Trader, Data Scientist | Sequence 5 (Quant/Macro) |
| Head of AI / Tech | Head of AI, CTO, CDO, Head of Data, Head of Technology, VP Technology, Head of Data Engineering | Sequence 4 (Head of AI) |
