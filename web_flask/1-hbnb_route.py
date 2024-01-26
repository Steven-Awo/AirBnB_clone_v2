#!/usr/bin/python3
"""Starting a flask's web app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
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

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
