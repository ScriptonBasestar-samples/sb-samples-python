import os
from dotenv import load_dotenv
from flask_awscognito import AWSCognitoAuthentication
from flask_awscognito.services import TokenService, CognitoService
from flask_cognito import CognitoAuth

from .flask import app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'), verbose=True)


class Config:
    AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-2')
    AWS_COGNITO_DOMAIN = os.getenv('AWS_COGNITO_DOMAIN', 'domain.com')
    AWS_COGNITO_USER_POOL_ID = os.getenv('AWS_COGNITO_USER_POOL_ID', '')
    AWS_COGNITO_USER_POOL_CLIENT_ID = os.getenv('AWS_COGNITO_USER_POOL_CLIENT_ID', '')
    AWS_COGNITO_USER_POOL_CLIENT_SECRET = os.getenv('AWS_COGNITO_USER_POOL_CLIENT_SECRET', '')
    AWS_COGNITO_REDIRECT_URL = os.getenv('AWS_COGNITO_REDIRECT_URL', 'http://localhost:5000/auth/redirect')

    COGNITO_REGION = os.getenv('COGNITO_REGION', 'ap-northeast-2')
    COGNITO_USERPOOL_ID = os.getenv('COGNITO_USERPOOL_ID', '')

    COGNITO_APP_CLIENT_ID = os.getenv('COGNITO_APP_CLIENT_ID', '')
    COGNITO_CHECK_TOKEN_EXPIRATION = os.getenv('COGNITO_CHECK_TOKEN_EXPIRATION', False)
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
# aws_auth = AWSCognitoAuthentication(app)
aws_auth = AWSCognitoAuthentication(app, _token_service_factory=TokenService, _cognito_service_factory=CognitoService)

cogauth = CognitoAuth(app)
