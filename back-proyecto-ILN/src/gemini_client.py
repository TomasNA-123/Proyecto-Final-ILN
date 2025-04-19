import google.generativeai as genai
import json
from .config import GEMINI_API_KEY, GEMINI_MODEL
from .nlp_utils import detect_language

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
    
    def analyze_restaurant_tips(self, original_prompt: str, restaurants_data: list) -> dict:
        """Analyzes restaurant tips based on the user's original prompt"""
        # Create the analysis prompt
        analysis_prompt = self._create_analysis_prompt(original_prompt, restaurants_data)

        try:
            response = self.model.generate_content(analysis_prompt)

            response_split = response.text.split(" | ")
            json_output = ""

            for item in response_split:
                json_output += f"{{{item}}},"
            
            json_output = f"[{json_output[:-1]}]"

            json_output = json.loads(json_output)

            try:            

                return json_output
            except json.JSONDecodeError:
                raise Exception("Error parsing Gemini's response as JSON")
        except Exception as e:
            raise Exception(f"Error analyzing tips with Gemini: {str(e)}")
    
    def _create_analysis_prompt(self, original_prompt: str, restaurants_data: list) -> str:
        # Detect the language of the original prompt
        prompt_lang = detect_language(original_prompt)
        
        prompt_template = f"""
            Analyze the following restaurant tips based on this user request: "{original_prompt}"
            The user's request is in {prompt_lang} language, so please provide your analysis in {prompt_lang} language.
            For each restaurant, provide a brief analysis (maximum two sentences) focusing on aspects relevant to the user's request.

            In the format:
            "fsq_id": "<restaurant_id>" , "tips_analysis": "<your maximum two-sentence analysis in {prompt_lang} language> | ..."

            If you quote a text use ' instead of "
            Only return the plain text result
        """
        
        # Add each restaurant's data to the prompt
        for restaurant in restaurants_data:
            prompt_template += f"\nRestaurant ID: {restaurant.get('fsq_id', 'unknown')}\n"
            prompt_template += f"Tips:\n"
            for tip in restaurant.get('tips', []):
                prompt_template += f"- {tip}\n"
        
        # prompt_template += "\nProvide ONLY the JSON response, no additional text."
        return prompt_template 