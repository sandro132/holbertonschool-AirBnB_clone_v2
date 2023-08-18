#!/usr/bin/python3
"""Inicialization of the Python Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display hello World'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display hello HBNB!'''
    return "HBNB"


if __name__ == '__main__':
    # start Flask server
    app.run(debug=True, port=5000, host="0.0.0.0")
