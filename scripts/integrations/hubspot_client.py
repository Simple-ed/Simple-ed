"""
HubSpot API Client
Used for CRM management and deal tracking
"""

import os
import requests
from typing import Optional
from datetime import datetime

class HubSpotClient:
    BASE_URL = "https://api.hubapi.com"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("HUBSPOT_API_KEY")
        if not self.api_key:
            raise ValueError("HubSpot API key required. Set HUBSPOT_API_KEY env var.")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _request(self, method: str, endpoint: str, data: dict = None, params: dict = None) -> dict:
        """Make API request to HubSpot."""
        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.request(
            method,
            url,
            json=data,
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json() if response.text else {}

    # ==================== CONTACTS ====================

    def create_contact(
        self,
        email: str,
        first_name: str = None,
        last_name: str = None,
        company: str = None,
        job_title: str = None,
        phone: str = None,
        linkedin_url: str = None,
        lead_source: str = "Cold Outbound",
        custom_properties: dict = None
    ) -> dict:
        """
        Create a new contact in HubSpot.

        Returns:
            Dict with created contact data including ID
        """
        properties = {
            "email": email,
            "hs_lead_status": "NEW"
        }

        if first_name:
            properties["firstname"] = first_name
        if last_name:
            properties["lastname"] = last_name
        if company:
            properties["company"] = company
        if job_title:
            properties["jobtitle"] = job_title
        if phone:
            properties["phone"] = phone
        if linkedin_url:
            properties["linkedin_url"] = linkedin_url
        if lead_source:
            properties["hs_lead_source"] = lead_source
        if custom_properties:
            properties.update(custom_properties)

        return self._request("POST", "crm/v3/objects/contacts", data={"properties": properties})

    def get_contact_by_email(self, email: str) -> dict:
        """Get contact by email address."""
        return self._request(
            "POST",
            "crm/v3/objects/contacts/search",
            data={
                "filterGroups": [{
                    "filters": [{
                        "propertyName": "email",
                        "operator": "EQ",
                        "value": email
                    }]
                }]
            }
        )

    def update_contact(self, contact_id: str, properties: dict) -> dict:
        """Update contact properties."""
        return self._request(
            "PATCH",
            f"crm/v3/objects/contacts/{contact_id}",
            data={"properties": properties}
        )

    def update_lead_status(self, contact_id: str, status: str) -> dict:
        """
        Update contact's lead status.

        Common statuses: NEW, OPEN, IN_PROGRESS, OPEN_DEAL, UNQUALIFIED,
                        ATTEMPTED_TO_CONTACT, CONNECTED, BAD_TIMING
        """
        return self.update_contact(contact_id, {"hs_lead_status": status})

    # ==================== DEALS ====================

    def create_deal(
        self,
        deal_name: str,
        pipeline: str = "default",
        stage: str = "appointmentscheduled",
        amount: float = None,
        contact_id: str = None,
        close_date: str = None
    ) -> dict:
        """
        Create a new deal.

        Args:
            deal_name: Name of the deal
            pipeline: Pipeline ID (use 'default' for default pipeline)
            stage: Deal stage ID
            amount: Deal value
            contact_id: Associated contact ID
            close_date: Expected close date (YYYY-MM-DD)

        Returns:
            Dict with created deal data
        """
        properties = {
            "dealname": deal_name,
            "pipeline": pipeline,
            "dealstage": stage
        }

        if amount:
            properties["amount"] = str(amount)
        if close_date:
            properties["closedate"] = close_date

        deal = self._request("POST", "crm/v3/objects/deals", data={"properties": properties})

        # Associate contact with deal if provided
        if contact_id and deal.get("id"):
            self.associate_contact_to_deal(deal["id"], contact_id)

        return deal

    def associate_contact_to_deal(self, deal_id: str, contact_id: str) -> dict:
        """Associate a contact with a deal."""
        return self._request(
            "PUT",
            f"crm/v3/objects/deals/{deal_id}/associations/contacts/{contact_id}/deal_to_contact",
            data={}
        )

    def update_deal_stage(self, deal_id: str, stage: str) -> dict:
        """Update deal stage."""
        return self._request(
            "PATCH",
            f"crm/v3/objects/deals/{deal_id}",
            data={"properties": {"dealstage": stage}}
        )

    # ==================== NOTES ====================

    def add_note_to_contact(self, contact_id: str, note_body: str) -> dict:
        """Add a note to a contact."""
        # Create the note
        note = self._request(
            "POST",
            "crm/v3/objects/notes",
            data={
                "properties": {
                    "hs_note_body": note_body,
                    "hs_timestamp": datetime.now().isoformat()
                }
            }
        )

        # Associate with contact
        if note.get("id"):
            self._request(
                "PUT",
                f"crm/v3/objects/notes/{note['id']}/associations/contacts/{contact_id}/note_to_contact",
                data={}
            )

        return note

    # ==================== PIPELINES ====================

    def get_pipelines(self) -> dict:
        """Get all deal pipelines and stages."""
        return self._request("GET", "crm/v3/pipelines/deals")


def sync_instantly_reply_to_hubspot(hubspot: HubSpotClient, lead_data: dict, reply_content: str = None):
    """
    Sync a replied lead from Instantly to HubSpot.

    Args:
        hubspot: HubSpot client instance
        lead_data: Lead data from Instantly
        reply_content: Optional reply message content

    Returns:
        Dict with contact and deal info
    """
    email = lead_data.get("email")

    # Check if contact exists
    existing = hubspot.get_contact_by_email(email)

    if existing.get("results"):
        # Update existing contact
        contact_id = existing["results"][0]["id"]
        hubspot.update_lead_status(contact_id, "CONNECTED")
    else:
        # Create new contact
        contact = hubspot.create_contact(
            email=email,
            first_name=lead_data.get("first_name"),
            last_name=lead_data.get("last_name"),
            company=lead_data.get("company_name"),
            lead_source="Cold Outbound - Instantly"
        )
        contact_id = contact["id"]
        hubspot.update_lead_status(contact_id, "CONNECTED")

    # Add note about the reply
    if reply_content:
        hubspot.add_note_to_contact(
            contact_id,
            f"📧 Replied to cold email:\n\n{reply_content}"
        )

    return {"contact_id": contact_id, "status": "synced"}


# Example usage
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    client = HubSpotClient()

    # Get pipelines
    pipelines = client.get_pipelines()
    print("Deal Pipelines:")
    for pipeline in pipelines.get("results", []):
        print(f"  - {pipeline.get('label')}: {pipeline.get('id')}")
        for stage in pipeline.get("stages", []):
            print(f"      Stage: {stage.get('label')} ({stage.get('id')})")
