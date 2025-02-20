from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Get the Gemini API Key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Fixed URL for the Gemini API (replace with the actual API endpoint)
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"


@app.route('/generate-story', methods=['POST'])
def generate_story():
    # Greeting message
    greeting = "Welcome to the Nameless Teller! What kind of horrors do you want today?"


    # Get request data
    data = request.json
    theme = data.get('theme', 'horror')
    location = data.get('location', 'unknown')
    initial_clue = data.get('initial_clue', 'mysterious event')

    # Create the prompt for the Gemini API
    prompt = (f"Create a horror story in the style of H.P. Lovecraft and Agatha Christie. Theme: {theme}. Location: {location}."
              f" Initial clue: {initial_clue}. The story should include an engaging title, an investigative introduction, "
              f"plot development with subtle clues, a striking ending, and optionally a hook for continuations.")

    # Make a request to the Gemini API
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 800
        }
    }

    response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Format the response with paragraphs
        story = response.json()
        # Extrai a resposta corretamente do campo "candidates"
        story_text = story.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text",
                                                                                                   "No story generated.")

        formatted_response = {
            "greeting": greeting,
            "story": story_text  # Retorna a história completa
        }

        return jsonify(formatted_response)
    else:
        return jsonify({"error": "Failed to generate the story", "details": response.text}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=False)
