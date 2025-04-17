from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src import RestaurantRecommender

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
        return jsonify(recommendation_result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)