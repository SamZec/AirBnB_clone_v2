#!/usr/bin/python3
"""Flask web app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """shows c and text"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """shows python and text"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """shows number and n"""
    return "%s is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Makes a template with n passed into it"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Makes a template with n, and determine if odd or even"""
    if n % 2 == 0:
        string = "{} is even".format(n)
    else:
        string = "{} is odd".format(n)
    return render_template('5-number.html', n=string)


if __name__ == "__main__":
    app.run()
