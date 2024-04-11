#!/usr/bin/python3
"""
This module contains a Flask web application.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function is a route handler for the root URL ("/").
    It returns the string 'Hello HBNB!' as the response.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the string 'HBNB' when the '/hbnb' route is accessed.
    Returns:
        A string containing the text 'HBNB'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def is_fun(text):
    """
    Returns a string indicating that C is fun.

    Returns:
        str: A string indicating that C is fun.
    """
    return 'C ' + text.replace("_", " ")

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port="5000")
