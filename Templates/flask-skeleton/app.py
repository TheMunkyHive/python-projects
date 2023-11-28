from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    text = "Hello World!"
    return render_template("index.html", Greeting=text)

if __name__ == '__main__':
    # Enable debugging with debug=True
    app.run(debug=True)

    # CLI: Flask run