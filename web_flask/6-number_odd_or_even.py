#!/usr/bin/python3
"""
Flask application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    root directory
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb directory
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_life(text):
    """
    text substitution
    """
    return "C {}".format(text).replace("_", " ")


@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def py_sub(text):
    """
    More text substitution
    """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    url int substitution
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number(n):
    """
    renders jinja template
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def html_odd_even(n):
    """
    render jinja template
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)