#!/usr/bin/python3
"""Initialization of the Python Flask application"""
from flask import Flask, render_template


app = Flask(__name__)

'''Route root URL'''


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


'''Route for /hbnb'''


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


'''Route for /c/<text>'''


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


'''Route for /python/<text> with default value "is cool"'''


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


'''Route for /number/<n>'''


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return f"{n} is a number"


'''Route for /number_template/<n>'''


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
