# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 14:55
# @Author  : lilong
# @File    : token.py
# @Description:
from flask import current_app, jsonify

from app.libs.ClientTypeEnum import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[form.type.data](
        form.account.data,
        form.secret.data
    )
    token = generate_auth_token(identity['uid'],
                                form.type.data.value,
                                None,
                                current_app.config['TOKEN_EXPIRATION'])
    r = {
        'token': token.decode('ascii')
    }
    return jsonify(r)

def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type
    })