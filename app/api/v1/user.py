# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:24
# @Author  : lilong
# @File    : user.py
# @Description:
from flask import Blueprint, jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

# user = Blueprint('user', __name__)
from app.models.user import User

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    # 对于需要用户身份标识的接口 比如获取用户信息
    # token 是否合法  是否过期
    user = User.query.get_or_404(uid)
    return jsonify(user)

@api.route('/create')
def create_user():
    return 'i am user'