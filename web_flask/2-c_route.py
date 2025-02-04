#!/usr/bin/python3
"""c_route module
Starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Return: Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return: HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """Return: C text"""
    return "C %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
