from .gemini_client import GeminiClient
from .restaurant_service import RestaurantService
from .nlp_utils import detect_language
import json
import re

class RestaurantRecommender:
    def __init__(self):
        self.gemini_client = GeminiClient()
        self.restaurant_service = RestaurantService()
    
    def process_prompt(self, prompt: str) -> list:
        # Check if the language is supported
        lang = detect_language(prompt)
        if lang not in ['es', 'en']:
            raise ValueError(f"El idioma detectado '{lang}' no está soportado. Por favor, use español o inglés.")
            
        # First get restaurant recommendations
        restaurant_results = self.restaurant_service.process_prompt(prompt)
        
        if not restaurant_results:
            return []
            
        # Then analyze tips with Gemini
        try:
            tips_analysis = self.gemini_client.analyze_restaurant_tips(prompt, restaurant_results)
            
        except Exception as e:
            print(f"Error al analizar los tips: {str(e)}")
            raise ValueError(f"Error al analizar los tips: {str(e)}")

        # Combine the results
        
        final_results = []
        for restaurant in restaurant_results:
            # Find the corresponding tips analysis
            analysis = next(
                (item["tips_analysis"] for item in tips_analysis 
                 if item["fsq_id"] == restaurant["fsq_id"]),
                "No analysis available."
            )
            
            final_results.append({
                "name": restaurant["name"],
                "location": restaurant["location"],
                "tips_analysis": analysis,
                "rating": restaurant["rating"],
                "photos": restaurant["photos"]
            })
            
        return final_results 