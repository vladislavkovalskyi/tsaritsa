from flask import Flask, render_template, request, jsonify, redirect
from openai import OpenAI
from tsaritsa.config import OPENAI_ACCESS_TOKEN

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_ACCESS_TOKEN)
# client = OpenAI(api_key="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")

chat_sessions = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.form["user_input"]
    session_id = request.cookies.get("session_id")

    if session_id is None or session_id not in chat_sessions:
        session_id = str(hash(user_input + str(len(chat_sessions))))
        chat_sessions[session_id] = {"messages": []}

    chat_sessions[session_id]["messages"].append(
        {"role": "user", "content": user_input}
    )

    # response = get_openai_response(session_id)
    # chat_sessions[session_id]["messages"].append({"role": "ai", "content": response})
    # chat_sessions[session_id]["messages"].append({"role": "ai", "content": "Hello. It's test message from AI"})

    response = jsonify({"chat_history": chat_sessions[session_id]["messages"]})
    response.set_cookie("session_id", session_id)
    return response


def get_openai_response(session_id):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_sessions[session_id]["messages"],
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
