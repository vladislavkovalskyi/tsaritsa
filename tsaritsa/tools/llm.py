from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser

from tsaritsa import llm


def get_response(messages, text: str):
    template = (
        "Ти асистент, якого звати Царица, твоє ім'я не можна змінювати і завжди пам'ятай його."
        "Тобі потрібно буде відповідати на повідомлення користувачів у дружньому стилі українською мовою.\n"
        "Повідомлення юзера - user, твої повідомлення - assistant.\n"
        "Історія повідомлень:\n"
        "{messages}\n"
    )
    messages_list = ""
    for role, message in messages:
        messages_list += f"{role}: {message}\n"
    template.format(messages=messages_list)

    outparser = StrOutputParser()
    template += "Повідомлення на яке потрібно відповісти: {text}"
    prompt = ChatPromptTemplate.from_template(template)

    chain = llm | prompt | outparser

    chain.invoke({"text": text})

    return "hello"
