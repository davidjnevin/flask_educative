from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


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
