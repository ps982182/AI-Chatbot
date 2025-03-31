<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API configuration
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handle POST requests for chatbot interaction."""
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    if not API_KEY:
        return jsonify({"error": "Missing API key"}), 500

    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-4",  # 🔥 Switch to a valid model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 200
        }

        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

        if response.status_code == 200:
            # Improved response parsing with error handling
            json_response = response.json()
            
            # Check if 'choices' field exists
            if "choices" in json_response and len(json_response["choices"]) > 0:
                ai_response = json_response["choices"][0].get("message", {}).get("content", "No content.")
                return jsonify({"response": ai_response})
            else:
                return jsonify({"error": "Unexpected response format.", "details": json_response}), 500
        else:
            return jsonify({"error": "API request failed", "status_code": response.status_code, "details": response.text}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API configuration
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handle POST requests for chatbot interaction."""
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    if not API_KEY:
        return jsonify({"error": "Missing API key"}), 500

    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "openai/gpt-4",  # 🔥 Switch to a valid model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 200
        }

        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

        if response.status_code == 200:
            # Improved response parsing with error handling
            json_response = response.json()
            
            # Check if 'choices' field exists
            if "choices" in json_response and len(json_response["choices"]) > 0:
                ai_response = json_response["choices"][0].get("message", {}).get("content", "No content.")
                return jsonify({"response": ai_response})
            else:
                return jsonify({"error": "Unexpected response format.", "details": json_response}), 500
        else:
            return jsonify({"error": "API request failed", "status_code": response.status_code, "details": response.text}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> ad3b3e92fd78806f5ddcb89150b2121613268e62
