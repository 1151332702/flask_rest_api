# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:24
# @Author  : lilong
# @File    : user.py
# @Description:
from flask import Blueprint
from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('/get')
def get_user():
    return 'i am user'

@api.route('/create')
def create_user():
    return 'i am user'