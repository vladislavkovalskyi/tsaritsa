from flask import Flask, render_template, request, jsonify, redirect


app = Flask(__name__)

chat_history = ""

@app.route("/")
def index():
    return render_template("index.html", chat_history=chat_history)


@app.route("/send_message", methods=["POST"])
def send_message():
    print(request.get_data())
    return redirect("/", 200)

