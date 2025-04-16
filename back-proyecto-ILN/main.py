from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai



app = Flask(__name__)
CORS(app)

load_dotenv()

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/gemini', methods=['POST'])
def gemini():

    data = request.get_json()
    consulta = data.get("consulta")

    GEMINI_API_KEY = os.getenv('GEMINI-API-KEY')

    genai.configure(api_key = GEMINI_API_KEY)


    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    response = model.generate_content(consulta)

    return {"response": response.text}

if __name__ == '__main__':
    app.run(debug=True)