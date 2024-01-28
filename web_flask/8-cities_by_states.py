#!/usr/bin/python3
"""
Starting the web's application with only two routings
"""

from models.state import State

from models import storage

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """
    Rendering the templates with the states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)
# sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path,
            states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Cleaning-up the session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
