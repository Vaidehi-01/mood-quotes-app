from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

mood_emojis = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Tired": "😴",
    "Anxious": "😟",
    "Excited": "🤩",
    "Lonely": "🥺",
    "Inspired": "💪"
}

# Load quotes once when app starts
with open("quotes.json") as f:
    quotes = json.load(f)

def get_quote_by_mood(mood):
    mood = mood.capitalize()
    if mood in quotes:
        return random.choice(quotes[mood])
    else:
        return "Sorry, I don't have quotes for that mood yet."

@app.route("/", methods=["GET", "POST"])
def index():
    quote = ""
    selected_mood = ""
    emoji = ""

    if request.method == "POST":
        selected_mood = request.form.get("mood")
        quote = get_quote_by_mood(selected_mood)
        emoji = mood_emojis.get(selected_mood.capitalize(), "")
    
    return render_template("index.html", quote=quote, mood=selected_mood, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)
