from flask import Flask, request
from html import escape

from main import handler

app = Flask(__name__)


@app.route("/")
def home():
    return "AnimalSay is running."


@app.route("/animalsay")
def browser_test():
    text = request.args.get("text", "")
    return f"<pre>{escape(handler(text))}</pre>"


@app.route("/slack/animalsay", methods=["POST"])
def slack_animalsay():
    try:
        text = request.form.get("text", "")

        return {
            "response_type": "in_channel",
            "text": f"```{handler(text)}```"
        }
    except Exception as e:
        return {
            "response_type": "ephemeral",
            "text": f"Error: {e}"
        }


if __name__ == "__main__":
    app.run(debug=True)