
import os
import requests
from typing import List, Dict, Any

class FireCrawlClient:
    def __init__(self):
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        self.base_url = "https://api.firecrawl.dev/v1" # Using v1 as standard

    def search(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """
        Uses FireCrawl to search the web for the given query.
        Returns a list of results with title, content, and url.
        """
        if not self.api_key:
            print("FireCrawl API Key missing")
            return []

        url = f"{self.base_url}/search"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "query": query,
            "limit": limit,
            "scrapeOptions": {
                "formats": ["markdown"]
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                     # Data format: data['data'] is a list of results
                    return data.get("data", [])
            else:
                print(f"FireCrawl Error: {response.status_code} - {response.text}")
        except Exception as e:
             print(f"FireCrawl Exception: {e}")
        
        return []
