# import is used to make code in one module available in another
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# chat models take a series of messages as input, and return a model-generated message as output
completion = client.chat.completions.create(
    # ID of the model to use
    model="gpt-3.5-turbo",
    # sampling temperature for non deterministic responses
    temperature=0.8,
    # the total length of input tokens and generated tokens is limited by the model's context length
    max_tokens=256,
    # a list of messages describing the conversation
    messages=[
        {"role": "user", "content": "Hello who are you?"}
    ])