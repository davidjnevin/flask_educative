from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    Username = "Sally"
    return render_template("index.html", username = Username)


@app.route("/dict")
def index_dict():
    Users = { "Betty":"San Franscisco" }
    return render_template("index_dict.html", users = Users)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/flask")
def flask():
    return "Hello, flask!"

@app.route("/<myname>")
def greetings(myname):
    return f"Hello, {myname}!"


@app.route("/square/<int:number>")
def square(number):
    return f"The square of {str(number)} is {str(number**2)}!"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
