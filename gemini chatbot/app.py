import flask
from flask import Flask, render_template, request, jsonify
import vertexai

# Load environment variables from separate file (recommended)
from dotenv import load_dotenv
env_path = 'D:\PROJECTS GITHUB\.gemini chatbot\.env'  # Replace with your actual path
load_dotenv(env_path)

import os

# Retrieve credentials securely
API_KEY = os.getenv('API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')
CODE_CHAT_MODEL = os.getenv('CODE_CHAT_MODEL')

# Create the Flask app
app = Flask(__name__)

# Chat model initialization (use correct method and generation config)
chat_model = vertexai.CodeChatModel(project_id=PROJECT_ID, location=LOCATION, model_name=CODE_CHAT_MODEL, api_key=API_KEY)
generation_config = {
    # Add parameters relevant to your model and use case
    # Example: 'temperature': 0.7, 'max_tokens': 50
}

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/get", methods=['POST'])
def get_bot_response():
    # Handle both GET and POST requests for flexibility
    if request.method == 'POST':
        user_text = request.json.get('msg')  # Access message from JSON payload
    else:
        user_text = request.args.get('msg')  # Fallback for GET requests

    if user_text:
        try:
            response = chat_model.predict(text=user_text, features=generation_config)
            return jsonify({'response': response.text})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Please provide a message to send to the bot.'})

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development
