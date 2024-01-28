#!/usr/bin/python3
"""
Starting the web's application with just two routings
"""

from models.state import State

from models import storage

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """
    Rendering the template with the states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)
    return render_template(path, states=states))


@app.teardown_appcontext
def app_teardown(arg=None):
    """Cleaning-up the session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

