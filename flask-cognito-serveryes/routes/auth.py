from flask_cognito import cognito_auth_required, current_user, current_cognito_jwt, cognito_check_groups
from flask import _request_ctx_stack, current_app, jsonify, request, render_template, redirect

from config import app, aws_auth


@app.route('/auth/signin', methods=['GET'])
def signin():
    return redirect(aws_auth.get_sign_in_url())


@app.route('/auth/signup', methods=['POST'])
def signup():
    return jsonify({'success': 'signout'})


@app.route('/auth/signout', methods=['GET'])
def signout():
    return jsonify({'success': 'signout'})


@app.route('/auth/jwtpubkeys', methods=['GET'])
def jwt_pubkeys():
    print(aws_auth.token_service._load_jwk_keys())
    return jsonify({'succes': aws_auth.token_service._load_jwk_keys()})


@app.route('/auth/redirect', methods=['GET'])
def aws_cognito_redirect():
    access_token = aws_auth.get_access_token(request.args)
    return render_template('redirect.html', access_token=access_token)
