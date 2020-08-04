from flask_cognito import cognito_auth_required, current_user, current_cognito_jwt, cognito_check_groups
from flask import _request_ctx_stack, current_app, jsonify, request, render_template

from config import app, aws_auth


@app.route('/')
def home():
    return render_template('index.html', realname='kimkimkim')


@app.route('/test-jwtuser')
@cognito_auth_required
@cognito_check_groups(['admin', 'developer'])
def api_private():
    # user must belongs to "admin" or "developer" groups
    return jsonify({
        'foo': "bar"
    })


@app.route('/test-awsauth')
@aws_auth.authentication_required
def index():
    claims = aws_auth.claims
    return jsonify({'claims': claims})
