#!/usr/bin/python3
""" Module Flask"""

from flask import Flask
""" import module flask"""
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """ function that displays 'Hello HBNB!'"""
    return 'Hello HBNB'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
