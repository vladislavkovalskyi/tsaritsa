from openai import OpenAI

client = OpenAI(api_key="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")

data = client.completions.create(model="gpt-3.5-turbo", prompt="hi")
print(data)
