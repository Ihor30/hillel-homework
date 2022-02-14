from datetime import datetime
import flask
from flask import request
import string
import random
import webbrowser

app = flask.Flask(__name__)


@app.route("/whoami")
def whoami():
    headers = flask.request.headers
    date = datetime.now()

    return "Request headers: " + str(headers) + "Current time: " + str(date)


@app.route("/source_code")
def source_code():
    r = webbrowser.open('dz4.py')
    return r


@app.route("/random")
def random_string():
    length = request.values.get('length')
    specials = request.values.get('specials')
    digits = request.values.get('digits')

    letters = string.ascii_letters
    rnd_symbol = ''.join(random.choice(letters) for i in range(0, int(length)) if int(length) < 101)

    digits = 0 < int(digits) < 2

    specials = 0 < int(specials) < 2

    return f'Length: {rnd_symbol}, Specials: {bool(specials)}, Digits: {bool(int(digits))}'


app.run(debug=True)
