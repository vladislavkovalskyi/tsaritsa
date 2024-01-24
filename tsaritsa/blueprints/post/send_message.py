from flask import request, jsonify

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from tsaritsa.config import OPENAI_ACCESS_TOKEN, ORGANIZATION_ID
from tsaritsa.tools import llm
from . import send_message_blueprint

chat_sessions = {}


@send_message_blueprint.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.form["user_input"]
    session_id = request.cookies.get("session_id")

    # Создание сессии
    if session_id is None or session_id not in chat_sessions:
        session_id = str(hash(user_input + str(len(chat_sessions))))
        chat_sessions[session_id] = {"messages": []}

    session_messages = chat_sessions[session_id]["messages"]
    # Добавление ввода пользователя в список сообщений сессии
    chat_sessions[session_id]["messages"].append({"user": user_input})

    messages = [(role, message) for m in session_messages for role, message in m.items()]
    print(messages, user_input)

    response = llm.get_response(messages, user_input)

    # Добавление ответа от ассистента в список сообщений сессии
    chat_sessions[session_id]["messages"].append({"assistant": response})

    response = jsonify({"chat_history": chat_sessions[session_id]["messages"]})
    response.set_cookie("session_id", session_id)
    return response
