#!/usr/bin/python3
"""Inicialización de la aplicación Python Flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    is_even = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        '6-number_odd_or_even.html',
        number=n, is_even=is_even)


6
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
