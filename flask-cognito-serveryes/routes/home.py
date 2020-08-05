# from flask_cognito import cognito_auth_required, current_user, current_cognito_jwt, cognito_check_groups
from flask import _request_ctx_stack, current_app, jsonify, request, render_template

from config import app, cogauth_customer, awsauth_customer


@app.route('/')
def home():
    return render_template('index.html', realname='kimkimkim')


@app.route('/test-jwtuser')
@cogauth_customer.cognito_auth_required
@cogauth_customer.cognito_check_groups(['admin', 'developer'])
def api_private():
    # user must belongs to "admin" or "developer" groups
    return jsonify({
        'foo': "bar"
    })


@app.route('/test-awsauth')
@awsauth_customer.authentication_required
def index():
    claims = awsauth_customer.claims
    return jsonify({'claims': claims})
