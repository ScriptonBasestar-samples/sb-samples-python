Flask Cognito ServerYES
=============

하다보니까... 이거 필요한건가? 라는 의문이 들었지만...\
완료는 해놔야지

## TODO

로그인,로그아웃, 사용자조회(로컬-코그니토)


## Install

### Cognito

JWT support
* https://github.com/jetbridge/flask_cognito
  * https://github.com/borisrozumnuk/cognitojwt


* https://github.com/cgauge/Flask-AWSCognito
* https://flask-awscognito.readthedocs.io/en/latest/installation.html

* https://github.com/mcrowson/flask-cognito

```text
LoginID
  Email assress - only
required field
  email?? duplicate?
  phone number
  name, nickname
EMIAL verify..
.....
```

## Usage

### Endpoint

Signin <https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/login-endpoint.html>
```bash
GET https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/login?client_id=2dc5j9593dmed6kkt8cmom3rr4&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost/auth/redirect
```

Signout <https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/logout-endpoint.html>
```bash
GET https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/logout?client_id=2boue2dcmn06s20spnjh0og3g&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost:5000/auth/redirect
GET https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/logout?client_id=2boue2dcmn06s20spnjh0og3g&logout_uri=http://localhost:5000/auth/signout
```

UserInfo <https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/userinfo-endpoint.html>
```bash
GET https://<your-user-pool-domain>/oauth2/userInfo
Authorization: Bearer <access_token>
```

Signup
```bash
GET/POST https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/signup?client_id=2boue2dcmn06s20spnjh0og3g&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost:5000/auth/redirect
```

Token <https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/token-endpoint.html>

Authorize <https://docs.aws.amazon.com/ko_kr/cognito/latest/developerguide/authorization-endpoint.html>

### OAuth2

https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/oauth2/token&


### JWT public

```bash
https://cognito-idp.{region}.amazonaws.com/{userPoolId}/.well-known/jwks.json
https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_49M4XHccl/.well-known/jwks.json
```

### JWT check

```bash
https://cognito-idp.us-east-1.amazonaws.com/<userpoolID>
https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_49M4XHccl
```


## REF

* https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-verifying-a-jwt.html
* https://flask-awscognito.readthedocs.io/en/latest/index.html
* https://stackoverflow.com/questions/48983708/where-to-store-access-token-in-react-js
* https://pyjwt.readthedocs.io/en/latest/usage.html
* https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUsers.html
* https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html?highlight=cognito#CognitoIdentityProvider.Client.admin_create_user
