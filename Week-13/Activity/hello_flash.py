from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_flask():
     return "<p>Hello, Imman!</p>"

@app.route("/page")
def hello_flask():
     render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
