import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# variables are containers for storing data values.
prompt = "Hello who are you?"

# a function is a block of code which only runs when it is called.
# you can include data - prompt, known as parameters, into a function.


def chatCompletion(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=256,
        messages=[
            {"role": "user", "content": prompt}
        ])
    # returns with a value from a function
    return completion.choices[0].message.content


# call the function
print(chatCompletion(prompt))
