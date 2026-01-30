# Daloopa Outreach System

Sales outreach playbook, Apollo sequences, and target account data for Daloopa's buy-side prospecting.

---

## Repo Structure

```
/accounts/                 Target account data
  target_accounts.csv        150+ buy-side investment firms (contacts, opportunities, billing state)
  broker_adv_links.csv       Company domains, CRD numbers, SEC ADV brochure URLs

/sequences/                Apollo outreach sequences
  apollo_outreach_sequence.md   7 sequences with A/B/C subject lines + A/B body copy

/playbook/                 Sales playbook and reference docs
  personas.md                8 personas (6 active, 1 out of scope, detailed profiles)
  prospecting_playbook.md    Target criteria, job titles, contact priority framework
  analyst_schedule_and_timing.md  Analyst workday, earnings season timing, channel strategy
  product_core.md            Daloopa product overview (Excel Add-In, Hub, accuracy)
  product_api_taxonomy.md    API endpoints, Webhooks, 1,200+ Taxonomy metrics
  product_mcp.md             MCP (Model Context Protocol) for LLM integration
```

---

## 7 Apollo Sequences

| # | Sequence | Target | Key Angle |
|---|----------|--------|-----------|
| 1A | L/S HF Analyst | Pod analysts, multi-managers | Speed + volume during earnings, 50-80 models, PM wants postview yesterday |
| 1B | Long Biased Analyst | Tiger Cubs, concentrated funds | Deep model builds, new coverage initiation, complexity without update penalty |
| 1C | Mutual Fund Analyst | Long-only asset managers | Resource gap vs. HFs, sell-side model updates, leveling the playing field |
| 2 | Portfolio Manager | PMs / CIOs | Analyst throughput without adding headcount |
| 3 | Director of Research | DoRs | Expanding coverage without adding analysts |
| 4 | Head of AI / Tech | CTOs, CDOs, Head of Data | Build vs. buy, API + MCP, replace internal EDGAR scrapers |
| 5 | Quant / Macro | Quant researchers, systematic traders | Point-in-time data, no look-ahead bias, API-first, webhook signals |

All sequences include A/B/C subject line testing and A/B body copy testing (PAS vs 3-Line Sniper).

---

## Personas

| # | Persona | Status | Sequence |
|---|---------|--------|----------|
| 1 | L/S HF Analyst | Active | 1A |
| 2 | Long Biased HF Analyst | Active | 1B |
| 3 | Mutual Fund Analyst | Active | 1C |
| 4 | Sellside / ER Analyst | **Out of Scope** | N/A |
| 5 | L/S PM / CIO / DoR | Active | 2 / 3 |
| 6 | Long Biased PM / CIO / DoR | Active | 2 / 3 |
| 7 | Quant / Macro | Active | 5 |
| 8 | Head of AI / Tech | Active | 4 |

---

## Key Rules

- **Buy-side only** -- sellside is excluded from all sequences and targeting
- **No Daloopa branding in subject lines** -- use curiosity, internal camo, or Meeting Request format
- **Weekends over Monday mornings** -- Saturday 8-10 AM, Sunday 6-8 PM during earnings season
- **Quant/Macro is separate** -- any title containing "Quant" or "Macro" goes to Sequence 5 only
- **Personalize before enrolling** -- ADV brochure, company website, LinkedIn research required
