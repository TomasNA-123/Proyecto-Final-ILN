import os
from dotenv import load_dotenv

load_dotenv()

# Foursquare API configuration
FOURSQUARE_API_KEY = os.getenv('FOURSQUARE_API_KEY')
FOURSQUARE_BASE_URL = "https://api.foursquare.com/v3"
FOURSQUARE_RESTAURANTS_CATEGORY = "4d4b7105d754a06374d81259"

# GEMINI API configuration
GEMINI_API_KEY = os.getenv('GEMINI-API-KEY')

# NLP Models configuration
SENTIMENT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
RATING_MODEL = "nlptown/bert-base-multilingual-uncased-sentiment"
GEMINI_MODEL = "gemini-1.5-flash"