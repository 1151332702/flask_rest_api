# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:24
# @Author  : lilong
# @File    : user.py
# @Description:
from flask import Blueprint, jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

# user = Blueprint('user', __name__)
from app.models.base import db
from app.models.user import User

api = Redprint('user')

# 管理员用户
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 对于需要用户身份标识的接口 比如获取用户信息
    # token 是否合法  是否过期
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed()
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 普通用户
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    # 对于需要用户身份标识的接口 比如获取用户信息
    # token 是否合法  是否过期
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

@api.route('/create')
def create_user():
    return 'i am user'