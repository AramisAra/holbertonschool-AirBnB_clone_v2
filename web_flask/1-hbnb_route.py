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

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port="5000")
