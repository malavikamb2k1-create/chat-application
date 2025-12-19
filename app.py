from flask import Flask, render_template, request, jsonify

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

# IMPORTANT: do NOT use debug=True on Render
if __name__ == "__main__":
    app.run()
