from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src import RestaurantRecommender
import json

app = Flask(__name__)
CORS(app)
load_dotenv()

# Initialize recommender
recommender = RestaurantRecommender()

@app.route('/restaurants', methods=['POST'])
def restaurants():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        recommendation_result = recommender.process_prompt(prompt)
        print("===========")
        print(recommendation_result)
        print(type(recommendation_result))
        return json.dumps(recommendation_result)
        # return recommendation_result
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)