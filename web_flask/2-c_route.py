#!/usr/bin/python3
""" starts the flask app """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ returns hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def funC(text):
    """ returns C """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
