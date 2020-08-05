from functools import wraps

from flask import request, jsonify
from flask_awscognito import AWSCognitoAuthentication
from jose import jwt
from werkzeug.utils import redirect

from config.cognito import cogauth_customer
from models.users import User
from config import db, app

import routes.auth
import routes.home

db.create_all()


@cogauth_customer.identity_handler
def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    return User.query.filter(User.username == payload['username']).one_or_none()


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            # data = jwt.decode(token, app.config[SECRET_KEY])
            # current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


if __name__ == "__main__":
    app.run(debug=True)
