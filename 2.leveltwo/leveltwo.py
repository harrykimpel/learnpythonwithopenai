import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# chat models take a series of messages as input, and return a model-generated message as output
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.8,
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Hello who are you?"}
    ])

# print the response received from OpenAI
print(completion)