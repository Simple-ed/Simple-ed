"""
Apollo.io API Client
Used for prospecting and enriching lead data
"""

import os
import requests
from typing import Optional

class ApolloClient:
    BASE_URL = "https://api.apollo.io/v1"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("APOLLO_API_KEY")
        if not self.api_key:
            raise ValueError("Apollo API key required. Set APOLLO_API_KEY env var.")
        self.headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }

    def _request(self, method: str, endpoint: str, data: dict = None) -> dict:
        """Make API request to Apollo."""
        url = f"{self.BASE_URL}/{endpoint}"
        payload = {"api_key": self.api_key}
        if data:
            payload.update(data)

        response = requests.request(method, url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_people(
        self,
        person_titles: list[str] = None,
        person_seniorities: list[str] = None,
        organization_num_employees_ranges: list[str] = None,
        organization_locations: list[str] = None,
        q_organization_domains: list[str] = None,
        page: int = 1,
        per_page: int = 25
    ) -> dict:
        """
        Search for people matching criteria.

        Args:
            person_titles: Job titles ["CEO", "Founder", "VP Sales"]
            person_seniorities: ["owner", "founder", "c_suite", "vp", "director", "manager"]
            organization_num_employees_ranges: ["1,10", "11,50", "51,200"]
            organization_locations: ["United States"]
            q_organization_domains: Search specific domains
            page: Page number
            per_page: Results per page (max 100)

        Returns:
            Dict with 'people' list and pagination info
        """
        data = {
            "page": page,
            "per_page": per_page
        }

        if person_titles:
            data["person_titles"] = person_titles
        if person_seniorities:
            data["person_seniorities"] = person_seniorities
        if organization_num_employees_ranges:
            data["organization_num_employees_ranges"] = organization_num_employees_ranges
        if organization_locations:
            data["organization_locations"] = organization_locations
        if q_organization_domains:
            data["q_organization_domains"] = "\n".join(q_organization_domains)

        return self._request("POST", "mixed_people/search", data)

    def enrich_person(self, email: str = None, linkedin_url: str = None) -> dict:
        """
        Enrich a person's data by email or LinkedIn URL.

        Args:
            email: Person's email address
            linkedin_url: Person's LinkedIn profile URL

        Returns:
            Dict with enriched person data
        """
        data = {}
        if email:
            data["email"] = email
        if linkedin_url:
            data["linkedin_url"] = linkedin_url

        return self._request("POST", "people/match", data)

    def enrich_company(self, domain: str) -> dict:
        """
        Enrich company data by domain.

        Args:
            domain: Company domain (e.g., "apollo.io")

        Returns:
            Dict with enriched company data
        """
        return self._request("POST", "organizations/enrich", {"domain": domain})

    def get_email_status(self, email: str) -> dict:
        """
        Verify an email address.

        Args:
            email: Email to verify

        Returns:
            Dict with email verification status
        """
        # Apollo includes email verification in their enrichment
        return self._request("POST", "people/match", {"email": email})


def export_for_instantly(people: list[dict], campaign_name: str) -> list[dict]:
    """
    Format Apollo people data for Instantly import.

    Args:
        people: List of people from Apollo search
        campaign_name: Name for the campaign

    Returns:
        List of dicts formatted for Instantly CSV import
    """
    instantly_format = []

    for person in people:
        instantly_format.append({
            "email": person.get("email"),
            "first_name": person.get("first_name"),
            "last_name": person.get("last_name"),
            "company_name": person.get("organization", {}).get("name"),
            "title": person.get("title"),
            "linkedin_url": person.get("linkedin_url"),
            "website": person.get("organization", {}).get("website_url"),
            "campaign": campaign_name,
            # Custom variables for personalization
            "company_industry": person.get("organization", {}).get("industry"),
            "company_size": person.get("organization", {}).get("estimated_num_employees"),
        })

    return instantly_format


# Example usage
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    client = ApolloClient()

    # Search for startup founders
    results = client.search_people(
        person_titles=["Founder", "CEO", "Co-Founder"],
        person_seniorities=["owner", "founder", "c_suite"],
        organization_num_employees_ranges=["1,10", "11,50"],
        organization_locations=["United States"],
        per_page=10
    )

    print(f"Found {results.get('pagination', {}).get('total_entries', 0)} people")

    # Export for Instantly
    if results.get("people"):
        instantly_data = export_for_instantly(results["people"], "startup_founders_q1")
        print(f"Exported {len(instantly_data)} contacts for Instantly")
