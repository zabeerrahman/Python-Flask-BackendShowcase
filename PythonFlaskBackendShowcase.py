# First import the Flask class from the flask package into Python
from flask import Flask, render_template

# Setting variable "app" to instance of Flask class, since Python will be running the script, __name__ = __main__
app = Flask(__name__)

# Create route(s) for home page
@app.route("/")
@app.route("/home")
# Create empty function for each page
def home():
    return render_template("home.html")

# GET message is sent, and server returns data. Most common method.
# POST sends HTML form data to server. Received data is not cached.

# Create route for Class Grade Average Calculator
@app.route("/calc", methods = ["GET", "POST"])
def calculator():
    return render_template("calc.html")

# Create route for Examination Statistics and define methods that will be used
@app.route("/stats", methods = ["GET", "POST"])
def statistics():
    return render_template("stats.html")

# Create route for Final Grade Resolver and define methods that will be used
@app.route("/resolve", methods = ["GET", "POST"])
def resolver():
    return render_template("resolve.html")

# Create conditional for when we execute using Python
# Allows flask to know where to run the active Debugger
if __name__ == "__main__":
    app.run(debug=True)
