#!/usr/bin/python3
""" Module Flask"""

from flask import Flask, escape, render_template
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

    return 'python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):

    """display “n is a number” only if n is an integer """

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):

    """display a HTML page only if n is an integer"""

    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
