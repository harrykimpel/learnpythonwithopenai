# imports the Flask framework and some additional modules
# we'll use to render HTML templates and handle HTTP requests.
from flask import Flask, render_template, request

# creates a new Flask app with the name of the module passed in as the argument.
app = Flask(__name__)

# a route that maps the URL "/" to the main function.
# the main function returns the index.html template as the response.


@app.route("/")
def main():
    # uses the render_template function to display index.html
    # and return it as the response.
    return render_template("index.html")

# a route that maps the URL "/prompt" to the prompt function.
# the prompt function returns the index.html template as the response.


@app.route("/prompt", methods=["POST"])
def prompt():
    # gets the value of the input field in the form
    # and assigns it to the input_prompt variable.
    input_prompt = request.form.get("input")
    # assigns the value of input_prompt to output_prompt.
    output_prompt = input_prompt
    # uses the render_template function to display index.html.
    return render_template("index.html", output=output_prompt)


# run the application on the local machine using
# flask --app levelfour.py run --host 0.0.0.0 --port 5000
if __name__ == '__main__':
    # enables debug mode and specifies the port number to run the application on.
    app.run(host="0.0.0.0", debug=True, port=5000)
