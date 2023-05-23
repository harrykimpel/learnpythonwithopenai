# import the New Relic Python Agent
import newrelic.agent
import openai
from flask import Flask, render_template, request

openai.api_key = "API_KEY_HERE"

app = Flask(__name__)

# initialize the New Relic Python agent
newrelic.agent.initialize('newrelic.ini')


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
def home():
    return render_template("index.html")


@app.route("/prompt", methods=["POST"])
def prompt():
    input_prompt = request.form.get("input")
    output_prompt = chatCompletion(input_prompt)
    return render_template("index.html", output=output_prompt)


# run the application on the local machine using flask --app levelsix.py run
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5004)
