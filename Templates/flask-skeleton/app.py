from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    text = "Hello Flask!"
    return render_template("index.html", Greeting=text)

if __name__ == '__main__':
    # Enable debugging with debug=True
    app.run(debug=True)

    # To start the server via cli: flask run --host=10.8.0.1
    # To use the environment variables: source flask.env -> flask run
