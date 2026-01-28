# Leadwave Automation Scripts

Automation scripts for Apollo → Instantly → HubSpot workflow.

## Setup

### 1. Install Dependencies

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy the example env file
cp ../.env.example ../.env

# Edit with your API keys
nano ../.env
```

**Where to get your API keys:**

| Tool | How to get API key |
|------|--------------------|
| Apollo | Settings → Integrations → API |
| Instantly | Settings → Integrations → API |
| HubSpot | Settings → Integrations → Private Apps → Create |

## Usage

### Workflow CLI

The main workflow script provides a CLI for common operations:

```bash
# Search Apollo and preview leads (dry run)
python workflow.py prospect \
  --campaign "your-instantly-campaign-id" \
  --titles "CEO" "Founder" "VP Sales" \
  --seniorities "owner" "founder" "c_suite" \
  --company-size "1,10" "11,50" \
  --max-leads 50

# Actually add leads to Instantly (remove dry run)
python workflow.py prospect \
  --campaign "your-campaign-id" \
  --titles "CEO" "Founder" \
  --execute

# Sync replied leads to HubSpot
python workflow.py sync --campaign "your-campaign-id"

# Get campaign report
python workflow.py report --campaign "your-campaign-id"

# Export campaign leads to CSV
python workflow.py export --campaign "your-campaign-id"
```

### Using as a Library

```python
from integrations import ApolloClient, InstantlyClient, HubSpotClient

# Apollo: Search for prospects
apollo = ApolloClient()
results = apollo.search_people(
    person_titles=["CEO", "Founder"],
    organization_num_employees_ranges=["1,10", "11,50"],
    per_page=25
)

# Instantly: Get campaign stats
instantly = InstantlyClient()
stats = instantly.get_campaign_summary("campaign-id")
print(f"Open rate: {stats['opened'] / stats['sent'] * 100}%")

# HubSpot: Create contact from reply
hubspot = HubSpotClient()
hubspot.create_contact(
    email="lead@company.com",
    first_name="John",
    company="Acme Inc",
    lead_source="Cold Outbound"
)
```

## Integrations

### Apollo Client (`integrations/apollo_client.py`)
- `search_people()` - Search for prospects by criteria
- `enrich_person()` - Enrich person data by email/LinkedIn
- `enrich_company()` - Get company data by domain
- `export_for_instantly()` - Format results for Instantly import

### Instantly Client (`integrations/instantly_client.py`)
- `list_campaigns()` - List all campaigns
- `add_leads_to_campaign()` - Add leads to campaign
- `get_campaign_summary()` - Get campaign analytics
- `get_replied_leads()` - Get leads who replied
- `get_lead_status()` - Check individual lead status

### HubSpot Client (`integrations/hubspot_client.py`)
- `create_contact()` - Create CRM contact
- `update_lead_status()` - Update lead status
- `create_deal()` - Create deal from qualified lead
- `add_note_to_contact()` - Log activity notes

## Workflow Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Apollo    │────▶│  Instantly  │────▶│   HubSpot   │
│ (Prospect)  │     │  (Outreach) │     │    (CRM)    │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
 Search ICPs         Send emails         Track deals
 Enrich data         Track opens         Manage pipeline
 Verify emails       Get replies         Close revenue
```

## Future Enhancements

- [ ] Auto-personalization with AI-generated first lines
- [ ] Slack notifications for hot leads/replies
- [ ] Daily/weekly automated reports
- [ ] Lead scoring based on engagement
- [ ] Intent signal monitoring
