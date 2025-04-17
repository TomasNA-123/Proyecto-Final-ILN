from .nlp_utils import (
    detect_language,
    get_nlp_pipeline,
    extract_locations,
    extract_nouns,
    analyze_sentiment,
    analyze_ratings,
    remove_special_characters
)
from .foursquare_client import FoursquareClient

class RestaurantService:
    def __init__(self):
        self.foursquare_client = FoursquareClient()

    def process_prompt(self, prompt):
        """Process a user prompt and return restaurant recommendations."""
        # Detect language and get appropriate NLP pipeline
        lang = detect_language(prompt)
        nlp = get_nlp_pipeline(lang)
        
        # Process the prompt with Stanza
        doc = nlp(prompt)
        
        # Extract relevant information
        locations = extract_locations(doc)
        nouns = extract_nouns(doc)
        sort_order = analyze_sentiment(prompt)
        
        # Search for places
        search_results = self.foursquare_client.search_places(nouns, locations, sort_order)
        
        # Process results and get tips
        restaurants_with_tips = self._process_search_results(search_results)
        
        return restaurants_with_tips

    def _process_search_results(self, search_results):
        """Process search results and gather tips for each restaurant."""
        restaurants = []
        
        for item in search_results.get("results", []):
            fsq_id = item["fsq_id"]
            name = item["name"]

            # print(item)
            
            # Get location information
            location = item.get("location", {})
            address = location.get("address", "")
            locality = location.get("locality", "")
            country = location.get("country", "")
            
            # Create formatted location string
            formatted_location = f"{address}, {locality}, {country}" if address and locality and country else ""
            
            # Get tips for the restaurant
            tips_response = self.foursquare_client.get_place_tips(fsq_id)
            tips = [remove_special_characters(tip["text"]) for tip in tips_response]
            
            # Calculate average rating from tips
            avg_rating = analyze_ratings(tips)
            
            restaurants.append({
                "name": name,
                "location": formatted_location,
                "tips": tips,
                "rating": avg_rating
            })
        
        # Sort restaurants by rating
        restaurants.sort(key=lambda x: x["rating"], reverse=True)

        return restaurants 