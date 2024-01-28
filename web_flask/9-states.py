#!/usr/bin/python3
"""Importing the Flask library to be ran on the web's app"""
from models import storage

from flask import Flask, render_template

from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method that is to close up the session """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displaying a html's page  thats with the states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displaying a html's page thats with the citys of that particular state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
