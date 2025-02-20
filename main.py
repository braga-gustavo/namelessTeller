from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"


@app.route('/generate-story', methods=['POST'])
def generate_story():
    greeting = "Welcome to the Nameless Teller! What kind of horrors do you want today?"

    data = request.json
    theme = data.get('theme', 'horror')
    location = data.get('location', 'unknown')
    initial_clue = data.get('initial_clue', 'mysterious event')

    prompt = (
        f"Create a horror story in the style of H.P. Lovecraft and Agatha Christie. Theme: {theme}. Location: {location}."
        f" Initial clue: {initial_clue}. The story should include an engaging title, an investigative introduction, "
        f"plot development with subtle clues, a striking ending, and optionally a hook for continuations.")

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

    if response.status_code == 200:

        story = response.json()

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
