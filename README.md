# Nameless Teller - Horror Story Generator

Nameless Teller is a Flask-based API that generates horror stories in the style of **H.P. Lovecraft** and **Agatha Christie**, powered by Google's **Gemini AI**. The user provides a **theme**, **location**, and an **initial clue**, and the AI crafts an eerie, investigative horror story.

## 🚀 Features
- Generates **Lovecraftian & Agatha Christie-style** horror stories.
- Uses **Google Gemini AI** for high-quality storytelling.
- Accepts **custom themes, locations, and clues** for unique stories.
- Returns a fully formatted JSON response with the complete horror tale.

## 📌 Requirements
- Python 3.8+
- Flask
- Requests
- dotenv

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/braga-gustavo/Nameless-Teller.git
   cd Nameless-Teller
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 🔥 Running the API

Start the Flask server:
```bash
python app.py
```

By default, the API runs on `http://127.0.0.1:8080`.

## 📡 API Usage

### **Endpoint:**
`POST /generate-story`

### **Request Body (JSON):**
```json
{
  "theme": "ancient curse",
  "location": "remote village",
  "initial_clue": "a series of unexplained disappearances"
}
```

### **Response Example:**
```json
{
  "greeting": "Welcome to the Nameless Teller! What kind of horrors do you want today?",
  "story": "It was a quiet night in the remote village when the first disappearance occurred..."
}
```

## 🛠️ Deployment (Optional)
To deploy on a cloud service like **Heroku, AWS, or Render**, ensure you configure environment variables correctly.

## 📝 License
This project is licensed under the **MIT License**.

## 🙌 Contributions
Feel free to submit **issues**, **feature requests**, or **pull requests**!

---

🔮 **Created with chills and mystery by Gustavo Braga.**

