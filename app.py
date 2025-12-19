from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_msg = request.form["message"]
    messages.append({"sender": "User", "text": user_msg})

    bot_reply = f"You said: {user_msg}"
    messages.append({"sender": "Bot", "text": bot_reply})

    return jsonify(messages=messages)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
