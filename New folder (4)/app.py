"""Flask entry point for the chatbot web app."""

import os
import sys
import tempfile
from pathlib import Path

from flask import Flask, jsonify, render_template, request


ROOT_DIR = Path(__file__).resolve().parent
CHATBOT_DIR = ROOT_DIR / "chatbot.py"
WEB_DIR = ROOT_DIR.parent / "New folder (3)"

if os.environ.get("VERCEL"):
    temp_dir = Path(tempfile.gettempdir())
    os.environ.setdefault("CHATBOT_DB_PATH", str(temp_dir / "chatbot.db"))
    os.environ.setdefault("CHATBOT_MODEL_CACHE_DIR", str(temp_dir / "chatbot_model_cache"))

sys.path.insert(0, str(CHATBOT_DIR))

import main as chatbot_main  # noqa: E402


chatbot_namespace = chatbot_main._load_all(run_name="chatbot_app")
ChatBot = chatbot_namespace["ChatBot"]


app = Flask(
    __name__,
    template_folder=str(WEB_DIR / "templates"),
    static_folder=str(WEB_DIR / "static"),
)
bot = ChatBot()


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "message must be a non-empty string"}), 400

    try:
        reply = bot.respond(message.strip())
    except Exception:
        app.logger.exception("Chatbot request failed")
        return jsonify({"error": "The chatbot could not process that message"}), 500

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)