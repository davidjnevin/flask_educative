from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Paws Rescue Center 🐾"


@app.route("/about")
def about():
    return """
    We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology "adopt, don't shop"!
    """

@app.route("/<myname>")
def greetings(myname):
    return f"Hello, {myname}!"


@app.route("/square/<int:number>")
def square(number):
    return f"The square of {str(number)} is {str(number**2)}!"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
