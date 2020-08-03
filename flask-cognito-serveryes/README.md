Flask Cognito ServerYES
=============

## Install

### Cognito

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

### Login

```bash
https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/login?client_id=2dc5j9593dmed6kkt8cmom3rr4&response_type=code&scope=email+openid+phone&redirect_uri=http://localhost/auth/redirect
```

### Logout

```bash
https://bo-user-dev.auth.ap-northeast-2.amazoncognito.com/logout?response_type=code&client_id=2dc5j9593dmed6kkt8cmom3rr4&logout_uri=http://localhost/auth/signout
```

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
