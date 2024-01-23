from envparse import env

env.read_envfile(".env")

OPENAI_ACCESS_TOKEN = env.str("OPENAI_ACCESS_TOKEN")

print(OPENAI_ACCESS_TOKEN)