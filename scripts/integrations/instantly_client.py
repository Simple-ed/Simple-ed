"""
Instantly.ai API Client
Used for cold email campaigns and tracking
"""

import os
import requests
from typing import Optional

class InstantlyClient:
    BASE_URL = "https://api.instantly.ai/api/v1"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("INSTANTLY_API_KEY")
        if not self.api_key:
            raise ValueError("Instantly API key required. Set INSTANTLY_API_KEY env var.")
        self.headers = {
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None) -> dict:
        """Make API request to Instantly."""
        url = f"{self.BASE_URL}/{endpoint}"

        # API key goes in params
        if params is None:
            params = {}
        params["api_key"] = self.api_key

        response = requests.request(
            method,
            url,
            params=params,
            json=data,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json() if response.text else {}

    # ==================== CAMPAIGNS ====================

    def list_campaigns(self, skip: int = 0, limit: int = 100) -> list:
        """
        List all campaigns.

        Returns:
            List of campaign objects
        """
        return self._request("GET", "campaign/list", params={"skip": skip, "limit": limit})

    def get_campaign(self, campaign_id: str) -> dict:
        """Get campaign details."""
        return self._request("GET", "campaign/get/status", params={"campaign_id": campaign_id})

    def get_campaign_summary(self, campaign_id: str) -> dict:
        """
        Get campaign analytics summary.

        Returns:
            Dict with sent, opened, replied, bounced counts
        """
        return self._request("GET", "analytics/campaign/summary", params={"campaign_id": campaign_id})

    # ==================== LEADS ====================

    def add_leads_to_campaign(self, campaign_id: str, leads: list[dict]) -> dict:
        """
        Add leads to a campaign.

        Args:
            campaign_id: Campaign to add leads to
            leads: List of lead dicts with at least 'email' field
                   Can include: email, first_name, last_name, company_name,
                   personalization, phone, website, custom variables

        Returns:
            Dict with upload status
        """
        data = {
            "campaign_id": campaign_id,
            "leads": leads
        }
        return self._request("POST", "lead/add", data=data)

    def get_lead_status(self, email: str, campaign_id: str = None) -> dict:
        """
        Get status of a specific lead.

        Args:
            email: Lead's email
            campaign_id: Optional campaign filter

        Returns:
            Dict with lead status and activity
        """
        params = {"email": email}
        if campaign_id:
            params["campaign_id"] = campaign_id
        return self._request("GET", "lead/get", params=params)

    def list_leads(self, campaign_id: str, skip: int = 0, limit: int = 100) -> list:
        """List leads in a campaign."""
        return self._request("GET", "lead/list", params={
            "campaign_id": campaign_id,
            "skip": skip,
            "limit": limit
        })

    # ==================== ANALYTICS ====================

    def get_campaign_analytics(self, campaign_id: str, start_date: str = None, end_date: str = None) -> dict:
        """
        Get detailed campaign analytics.

        Args:
            campaign_id: Campaign ID
            start_date: Optional start date (YYYY-MM-DD)
            end_date: Optional end date (YYYY-MM-DD)

        Returns:
            Dict with detailed analytics
        """
        params = {"campaign_id": campaign_id}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return self._request("GET", "analytics/campaign/summary", params=params)

    def get_replied_leads(self, campaign_id: str) -> list:
        """Get all leads who replied in a campaign."""
        return self._request("GET", "lead/list/replied", params={"campaign_id": campaign_id})

    def get_opened_leads(self, campaign_id: str) -> list:
        """Get all leads who opened emails in a campaign."""
        return self._request("GET", "lead/list/opened", params={"campaign_id": campaign_id})


def format_leads_from_apollo(apollo_leads: list[dict]) -> list[dict]:
    """
    Convert Apollo export to Instantly lead format.

    Args:
        apollo_leads: Leads exported from Apollo

    Returns:
        List formatted for Instantly API
    """
    instantly_leads = []

    for lead in apollo_leads:
        if not lead.get("email"):
            continue

        instantly_leads.append({
            "email": lead["email"],
            "first_name": lead.get("first_name", ""),
            "last_name": lead.get("last_name", ""),
            "company_name": lead.get("company_name", ""),
            "personalization": lead.get("title", ""),  # Use title as personalization
            "website": lead.get("website", ""),
            # Custom variables for email templates
            "variables": {
                "title": lead.get("title", ""),
                "industry": lead.get("company_industry", ""),
                "company_size": str(lead.get("company_size", "")),
                "linkedin": lead.get("linkedin_url", "")
            }
        })

    return instantly_leads


# Example usage
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    client = InstantlyClient()

    # List campaigns
    campaigns = client.list_campaigns()
    print(f"Found {len(campaigns)} campaigns")

    for campaign in campaigns[:5]:
        print(f"  - {campaign.get('name')}: {campaign.get('id')}")

        # Get campaign stats
        stats = client.get_campaign_summary(campaign["id"])
        print(f"    Sent: {stats.get('sent', 0)}, Opened: {stats.get('opened', 0)}, Replied: {stats.get('replied', 0)}")
