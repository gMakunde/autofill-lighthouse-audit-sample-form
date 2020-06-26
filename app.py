import flask
import os
import json

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("autocomplete_audit_test.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
