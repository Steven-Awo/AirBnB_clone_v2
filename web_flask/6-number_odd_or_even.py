#!/usr/bin/python3
"""
Starting a web application that has two routings
"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Retrieving the template that for the request
    """
    path = '5-number.html'
    return render_template(path, n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Rendering the template thats based on just conditional
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
