#!/usr/bin/python3
'''Starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State

'''Create an instance of a flask and assings it to the variable app'''
app = Flask(__name__)

'''Teardown to remove SQLALchemy session after each request'''


@app.teardown_appcontext
def teardown(self):
    '''Remove the current session'''
    storage.close()


'''Define the route for /states_list'''


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Display an HTML page with a list of all states'''
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    ''''start the Flask development server'''
    app.run(host='0.0.0.0', port=5000)
