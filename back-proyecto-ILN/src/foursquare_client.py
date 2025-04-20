import requests
from urllib.parse import quote
from .config import (
    FOURSQUARE_API_KEY,
    FOURSQUARE_BASE_URL,
    FOURSQUARE_RESTAURANTS_CATEGORY
)

class FoursquareClient:
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": FOURSQUARE_API_KEY
        }

    def search_places(self, query_terms, locations):
        """Search for places using the Foursquare API."""
        query_string = ", ".join(query_terms)
        query_encoded = quote(query_string)
        
        location_string = ", ".join(locations)
        location_encoded = quote(location_string)
        
        url = f"{FOURSQUARE_BASE_URL}/places/search"
        params = {
            "query": query_encoded,
            "categories": FOURSQUARE_RESTAURANTS_CATEGORY,
            "near": location_encoded
        }
        
        response = requests.get(url, headers=self.headers, params=params)

        return response.json()

    def get_place_tips(self, fsq_id):
        """Get tips for a specific place."""
        url = f"{FOURSQUARE_BASE_URL}/places/{fsq_id}/tips"
        response = requests.get(url, headers=self.headers)
        return response.json() 