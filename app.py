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

@app.route('/autocomplete-audit-no-form-name')
def autocomplete6():
    return flask.render_template("autocomplete_audit_test_no_form_name.html")

@app.route('/autocomplete-audit-passed')
def autocomplete7():
    return flask.render_template("autocomplete_audit_test_passed.html")

@app.route('/placeholder-audit')
def placeholder():
    return flask.render_template("placeholder_audit_test.html")

@app.route('/placeholder-audit-passed')
def placeholder2():
    return flask.render_template("placeholder_audit_test_pass.html")

@app.route('/formfield-audit-no-credit')
def formfield1():
    return flask.render_template("formfield_audit_test_no_credit.html")

@app.route('/formfield-audit-first-last')
def formfield2():
    return flask.render_template("formfield_audit_test_first_last.html")

@app.route('/formfield-audit-no-cvc')
def formfield3():
    return flask.render_template("formfield_audit_test_no_cvc.html")

@app.route('/formfield-audit-no-date')
def formfield4():
    return flask.render_template("formfield_audit_test_no_date.html")

@app.route('/formfield-audit-no-name')
def formfield5():
    return flask.render_template("formfield_audit_test_no_name.html")

@app.route('/formfield-audit-passed-auto')
def formfield6():
    return flask.render_template("formfield_audit_test_passed_auto.html")

@app.route('/formfield-audit-naming-flag')
def formfield7():
    return flask.render_template("formfield_audit_test_passed_naming_flag.html")

@app.route('/formfield-audit-passed-no-auto')
def formfield8():
    return flask.render_template("formfield_audit_test_passed_no_auto.html")

@app.route('/realistic-ebay')
def realistic1():
    return flask.render_template("realistic_ebay.html")

@app.route('/realistic-ajmason')
def realistic2():
    return flask.render_template("realistic_ajmason.html")

@app.route('/realistic-1800contacts')
def realistic3():
    return flask.render_template("realisitc_1800contacts.html")

@app.route('/formless-inputs')
def formless():
    return flask.render_template("formless_address.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )
