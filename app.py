from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/<myname>")
def greetings(myname):
    return f"Hello, {myname}!"


@app.route("/square/<int:number>")
def square(number):
    return f"The square of {str(number)} is {str(number**2)}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
