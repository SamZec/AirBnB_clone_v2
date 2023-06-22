#!/usr/bin/python3
"""Flask web app that prints Hello HBNB!"""

from flask import Flask
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

if __name__ == '__main__':
    app.run()
