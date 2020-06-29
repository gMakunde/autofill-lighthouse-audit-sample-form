import flask
import os
import json

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("audit_tests homepage.html")

@app.route('/autocomplete-audit-no-auto')
def index():
    return flask.render_template("autocomplete_audit_test.html")

@app.route('/autocomplete-audit-bad-auto')
def index():
    return flask.render_template("autocomplete_audit_test2.html")

@app.route('/placeholder-audit')
def index():
    return flask.render_template("placeholder_audit_test.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
