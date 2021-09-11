#!/usr/bin/python3
""" Module Flask"""

from flask import Flask, escape
""" import module flask"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():

    """ function that displays 'Hello HBNB!'"""

    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    """ function that displays 'HBNB'"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def profile(text):

    """ function that displays display “C ”
    followed by the value of the text variable """

    return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):

    """ function that displays display “python ”
    followed by the value of the text variable """

    return 'Python %s' % escape(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
