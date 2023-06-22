#!/usr/bin/python3
"""Flask web app that prints Hello HBNB!"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run()
