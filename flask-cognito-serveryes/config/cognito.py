import os
from dotenv import load_dotenv
from flask_awscognito import AWSCognitoAuthentication
from flask_awscognito.services import TokenService, CognitoService
from flask_cognito import CognitoAuth

from .flask import app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'), verbose=True)


class Config:
    AWS_DEFAULT_REGION = os.getenv('CUSTOMER_AWS_DEFAULT_REGION', 'ap-northeast-2')
    AWS_COGNITO_DOMAIN = os.getenv('CUSTOMER_AWS_COGNITO_DOMAIN', 'domain.com')
    AWS_COGNITO_USER_POOL_ID = os.getenv('CUSTOMER_AWS_COGNITO_USER_POOL_ID', '')
    AWS_COGNITO_USER_POOL_CLIENT_ID = os.getenv('CUSTOMER_AWS_COGNITO_USER_POOL_CLIENT_ID', '')
    AWS_COGNITO_USER_POOL_CLIENT_SECRET = os.getenv('CUSTOMER_AWS_COGNITO_USER_POOL_CLIENT_SECRET', '')
    AWS_COGNITO_REDIRECT_URL = os.getenv('CUSTOMER_AWS_COGNITO_REDIRECT_URL', 'http://localhost:5000/auth/redirect')

    COGNITO_REGION = os.getenv('CUSTOMER_COGNITO_REGION', 'ap-northeast-2')
    COGNITO_USERPOOL_ID = os.getenv('CUSTOMER_COGNITO_USERPOOL_ID', '')

    COGNITO_APP_CLIENT_ID = os.getenv('CUSTOMER_COGNITO_APP_CLIENT_ID', '')
    COGNITO_CHECK_TOKEN_EXPIRATION = os.getenv('CUSTOMER_COGNITO_CHECK_TOKEN_EXPIRATION', False)
    COGNITO_JWT_HEADER_NAME = os.getenv('CUSTOMER_COGNITO_JWT_HEADER_NAME', 'X-MyApp-Authorization')
    COGNITO_JWT_HEADER_PREFIX = os.getenv('CUSTOMER_COGNITO_JWT_HEADER_PREFIX', 'Bearer')


# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False

# class DevConfig(Config):
#     FLASK_ENV = 'development'
#     DEBUG = True
#     TESTING = True

# flask app config를 사용하기 때문에 이 순서가중요.
app.config.from_object('config.cognito.Config')
awsauth_customer = AWSCognitoAuthentication(app)
cogauth_customer = CognitoAuth(app)

app.config.from_object('config.cognito.Config')
awsauth_manager = AWSCognitoAuthentication(app)
cogauth_manager = CognitoAuth(app)
