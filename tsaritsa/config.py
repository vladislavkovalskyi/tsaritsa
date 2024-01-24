from envparse import env

env.read_envfile(".env")

OPENAI_ACCESS_TOKEN = env.str("OPENAI_ACCESS_TOKEN")
ORGANIZATION_ID = env.str("ORGANIZATION_ID")
