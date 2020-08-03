from models.users import User
from config import cogauth, db, app

import routes.home


@cogauth.identity_handler
def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    return User.query.filter(User.cognito_username == payload['username']).one_or_none()


if __name__ == "__main__":
    app.run()
