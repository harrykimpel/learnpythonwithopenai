import os
import openai
# API keys for accessing AI models developed by OpenAI.
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.8,
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Hello who are you?"}
    ])

# print the response received from OpenAI
print(completion)
