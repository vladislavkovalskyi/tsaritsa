from flask import Flask
from langchain_openai import ChatOpenAI

from tsaritsa.config import *

app = Flask(__name__)
llm = ChatOpenAI(api_key=OPENAI_ACCESS_TOKEN, organization=ORGANIZATION_ID, model="gpt-3.5-turbo")


from tsaritsa.blueprints import index_blueprint, send_message_blueprint
