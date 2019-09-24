# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 15:54
# @Author  : lilong
# @File    : token_auth.py
# @Description:
from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from tensorboard.backend.event_processing.event_accumulator import namedtuple

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'is_admin'])

@auth.verify_password
def verify_password(account, paaword):
    # 账号密码放在header中
    # key=Authorization
    # value=basic base64(account:password)
    user_info = verify_auth_token(account)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid.', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired.', error_code=1003)
    return User(data['uid'], data['type'], data['is_admin'])