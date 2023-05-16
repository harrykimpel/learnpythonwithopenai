import os
import openai
from flask import Flask, render_template, request

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# using the same function we saw back in levelthree.py
# taking the input from the user and returning the response from OpenAI


def chatCompletion(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=256,
        messages=[
            {"role": "user", "content": prompt}
        ])
    return completion.choices[0].message.content


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/prompt", methods=["POST"])
def prompt():
    input_prompt = request.form.get("input")
    # call the function - chatCompletion and pass the input from the user
    output_prompt = chatCompletion(input_prompt)
    return render_template("index.html", output=output_prompt)


# run the application on the local machine using flask --app levelfive.py run
if __name__ == '__main__':
    app.run(debug=True, port=5000)
