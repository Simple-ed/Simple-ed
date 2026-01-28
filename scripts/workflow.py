#!/usr/bin/env python3
"""
Leadwave Main Workflow Script
Orchestrates Apollo → Instantly → HubSpot pipeline
"""

import os
import csv
import json
from datetime import datetime
from dotenv import load_dotenv

from integrations import (
    ApolloClient,
    InstantlyClient,
    HubSpotClient,
    export_for_instantly,
    format_leads_from_apollo,
    sync_instantly_reply_to_hubspot
)


def prospect_to_campaign(
    search_criteria: dict,
    campaign_id: str,
    max_leads: int = 100,
    dry_run: bool = True
):
    """
    Full workflow: Search Apollo → Add to Instantly campaign.

    Args:
        search_criteria: Dict with Apollo search parameters
        campaign_id: Instantly campaign ID to add leads to
        max_leads: Maximum leads to add
        dry_run: If True, don't actually add leads (just preview)

    Returns:
        Dict with results summary
    """
    load_dotenv()

    apollo = ApolloClient()
    instantly = InstantlyClient()

    print(f"🔍 Searching Apollo with criteria: {search_criteria}")

    # Search Apollo
    results = apollo.search_people(**search_criteria)
    people = results.get("people", [])
    total_found = results.get("pagination", {}).get("total_entries", 0)

    print(f"📊 Found {total_found} total matches, retrieved {len(people)}")

    # Convert to Instantly format
    instantly_leads = format_leads_from_apollo(
        export_for_instantly(people, campaign_id)
    )

    # Filter out leads without emails
    valid_leads = [l for l in instantly_leads if l.get("email")]
    print(f"✅ {len(valid_leads)} leads with valid emails")

    if dry_run:
        print("\n🏃 DRY RUN - Not adding to Instantly")
        print("Sample leads:")
        for lead in valid_leads[:3]:
            print(f"  - {lead.get('first_name')} {lead.get('last_name')} <{lead.get('email')}> @ {lead.get('company_name')}")
        return {"status": "dry_run", "leads_found": len(valid_leads)}

    # Add to Instantly
    print(f"\n📤 Adding {len(valid_leads)} leads to campaign {campaign_id}")
    result = instantly.add_leads_to_campaign(campaign_id, valid_leads[:max_leads])

    print(f"✅ Added to Instantly: {result}")

    return {
        "status": "success",
        "leads_found": total_found,
        "leads_added": min(len(valid_leads), max_leads),
        "campaign_id": campaign_id
    }


def sync_replies_to_hubspot(campaign_id: str):
    """
    Sync all replied leads from Instantly campaign to HubSpot.

    Args:
        campaign_id: Instantly campaign ID

    Returns:
        Dict with sync results
    """
    load_dotenv()

    instantly = InstantlyClient()
    hubspot = HubSpotClient()

    print(f"📬 Fetching replies from campaign {campaign_id}")

    # Get replied leads
    replied_leads = instantly.get_replied_leads(campaign_id)
    print(f"Found {len(replied_leads)} replied leads")

    synced = 0
    errors = []

    for lead in replied_leads:
        try:
            result = sync_instantly_reply_to_hubspot(hubspot, lead)
            print(f"  ✅ Synced {lead.get('email')}")
            synced += 1
        except Exception as e:
            print(f"  ❌ Error syncing {lead.get('email')}: {e}")
            errors.append({"email": lead.get("email"), "error": str(e)})

    return {
        "status": "complete",
        "total_replies": len(replied_leads),
        "synced": synced,
        "errors": errors
    }


def get_campaign_report(campaign_id: str):
    """
    Generate a report for an Instantly campaign.

    Args:
        campaign_id: Instantly campaign ID

    Returns:
        Dict with campaign metrics
    """
    load_dotenv()

    instantly = InstantlyClient()

    print(f"📊 Generating report for campaign {campaign_id}")

    summary = instantly.get_campaign_summary(campaign_id)

    sent = summary.get("sent", 0)
    opened = summary.get("opened", 0)
    replied = summary.get("replied", 0)
    bounced = summary.get("bounced", 0)

    open_rate = (opened / sent * 100) if sent > 0 else 0
    reply_rate = (replied / sent * 100) if sent > 0 else 0
    bounce_rate = (bounced / sent * 100) if sent > 0 else 0

    report = {
        "campaign_id": campaign_id,
        "generated_at": datetime.now().isoformat(),
        "metrics": {
            "sent": sent,
            "opened": opened,
            "replied": replied,
            "bounced": bounced
        },
        "rates": {
            "open_rate": f"{open_rate:.1f}%",
            "reply_rate": f"{reply_rate:.1f}%",
            "bounce_rate": f"{bounce_rate:.1f}%"
        },
        "benchmarks": {
            "open_rate": "40%+ is good",
            "reply_rate": "5%+ is good",
            "bounce_rate": "<5% is healthy"
        }
    }

    print("\n" + "="*50)
    print(f"Campaign Report - {campaign_id}")
    print("="*50)
    print(f"Emails Sent:    {sent}")
    print(f"Opened:         {opened} ({open_rate:.1f}%)")
    print(f"Replied:        {replied} ({reply_rate:.1f}%)")
    print(f"Bounced:        {bounced} ({bounce_rate:.1f}%)")
    print("="*50)

    return report


def export_leads_to_csv(campaign_id: str, output_file: str = None):
    """
    Export leads from Instantly campaign to CSV.

    Args:
        campaign_id: Instantly campaign ID
        output_file: Output file path (default: leads_{campaign_id}.csv)

    Returns:
        Path to exported file
    """
    load_dotenv()

    instantly = InstantlyClient()

    if not output_file:
        output_file = f"leads_{campaign_id}_{datetime.now().strftime('%Y%m%d')}.csv"

    print(f"📥 Exporting leads from campaign {campaign_id}")

    leads = instantly.list_leads(campaign_id, limit=1000)
    print(f"Found {len(leads)} leads")

    if not leads:
        print("No leads to export")
        return None

    # Write to CSV
    fieldnames = ["email", "first_name", "last_name", "company_name", "status"]

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)

    print(f"✅ Exported to {output_file}")
    return output_file


# CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Leadwave Workflow CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Prospect command
    prospect_parser = subparsers.add_parser("prospect", help="Search Apollo and add to Instantly")
    prospect_parser.add_argument("--campaign", required=True, help="Instantly campaign ID")
    prospect_parser.add_argument("--titles", nargs="+", help="Job titles to search")
    prospect_parser.add_argument("--seniorities", nargs="+", help="Seniority levels")
    prospect_parser.add_argument("--company-size", nargs="+", help="Company size ranges (e.g., '1,10' '11,50')")
    prospect_parser.add_argument("--locations", nargs="+", default=["United States"], help="Locations")
    prospect_parser.add_argument("--max-leads", type=int, default=100, help="Max leads to add")
    prospect_parser.add_argument("--execute", action="store_true", help="Actually add leads (default is dry run)")

    # Sync command
    sync_parser = subparsers.add_parser("sync", help="Sync Instantly replies to HubSpot")
    sync_parser.add_argument("--campaign", required=True, help="Instantly campaign ID")

    # Report command
    report_parser = subparsers.add_parser("report", help="Get campaign report")
    report_parser.add_argument("--campaign", required=True, help="Instantly campaign ID")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export campaign leads to CSV")
    export_parser.add_argument("--campaign", required=True, help="Instantly campaign ID")
    export_parser.add_argument("--output", help="Output file path")

    args = parser.parse_args()

    if args.command == "prospect":
        criteria = {
            "per_page": min(args.max_leads, 100)
        }
        if args.titles:
            criteria["person_titles"] = args.titles
        if args.seniorities:
            criteria["person_seniorities"] = args.seniorities
        if args.company_size:
            criteria["organization_num_employees_ranges"] = args.company_size
        if args.locations:
            criteria["organization_locations"] = args.locations

        prospect_to_campaign(
            criteria,
            args.campaign,
            max_leads=args.max_leads,
            dry_run=not args.execute
        )

    elif args.command == "sync":
        sync_replies_to_hubspot(args.campaign)

    elif args.command == "report":
        get_campaign_report(args.campaign)

    elif args.command == "export":
        export_leads_to_csv(args.campaign, args.output)

    else:
        parser.print_help()
