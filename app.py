import flask
import os
import json

app = flask.Flask(__name__)


@app.route('/')
def homepage():
    return flask.render_template("audit_tests homepage.html")

@app.route('/autocomplete-audit-no-auto')
def autcomplete1():
    return flask.render_template("autocomplete_audit_test_no_auto.html")

@app.route('/autocomplete-audit-bad-auto')
def autocomplete2():
    return flask.render_template("autocomplete_audit_test_invalid_auto.html")

@app.route('/autocomplete-audit-on-auto')
def autocomplete3():
    return flask.render_template("autocomplete_audit_test_on_auto.html")

@app.route('/autocomplete-audit-off-auto')
def autocomplete4():
    return flask.render_template("autocomplete_audit_test_off_auto.html")

@app.route('/autocomplete-audit-mixed-auto')
def autocomplete5():
    return flask.render_template("autocomplete_audit_test_mixed_auto.html")

@app.route('/autocomplete-audit-passed')
def autocomplete6():
    return flask.render_template("autocomplete_audit_test_passed.html")

@app.route('/placeholder-audit')
def placeholder():
    return flask.render_template("placeholder_audit_test.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
