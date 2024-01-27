#!/usr/bin/python3
"""
Starting a web application that has two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
    Returning the string to when the route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Returning the string to when the route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Returning the reformatted texts
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
    Reformatting the text thats based on the optional variable
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n=None):
    """
    Allowing the request if the path variable that is a valid int
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
