#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ return the Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return C plus the parameters
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ return Python
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return the number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ return a html
    """
    return render_template(
                "5-number.html",
                num=n
            )


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        odev = "even"
    else:
        odev = "odd"
    return render_template(
                "6-number_odd_or_even.html",
                odd_or_even=odev,
                num=n
            )


if __name__ == "__main__":
    app.run()
