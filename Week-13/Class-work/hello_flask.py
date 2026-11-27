from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_flask():
     return "<p>Hello, Imman!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye, Imman!</p>"

@app.route("/mse")
def mse():
    return "<p>It's working! Imman learnt something...</p>"

@app.route("/page")
def page():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")
 
 
@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form["username"]
    return render_template("welcome.html", name=name)


 

if __name__ == "__main__":
    app.run(debug=True)
