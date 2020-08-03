import os
from dotenv import load_dotenv
from flask_cognito import CognitoAuth

from .flask import app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    COGNITO_REGION = os.getenv('COGNITO_REGION', 'eu-central-1')
    COGNITO_USERPOOL_ID = os.getenv('COGNITO_USERPOOL_ID', 'eu-central-1c3fea2')

    # optional
    COGNITO_APP_CLIENT_ID = os.getenv('COGNITO_APP_CLIENT_ID', 'abcdef123456')  # client ID you wish to verify user is authenticated against
    COGNITO_CHECK_TOKEN_EXPIRATION = os.getenv('COGNITO_CHECK_TOKEN_EXPIRATION', False)  # disable token expiration checking for testing purposes
    COGNITO_JWT_HEADER_NAME = os.getenv('COGNITO_JWT_HEADER_NAME', 'X-MyApp-Authorization')
    COGNITO_JWT_HEADER_PREFIX = os.getenv('COGNITO_JWT_HEADER_PREFIX', 'Bearer')


# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False

# class DevConfig(Config):
#     FLASK_ENV = 'development'
#     DEBUG = True
#     TESTING = True


app.config.from_object('config.cognito.Config')
cogauth = CognitoAuth(app)
