# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 10:43
# @Author  : lilong
# @File    : client.py
# @Description:
from flask import request

from app.libs.redprint import Redprint
from app.libs.ClientTypeEnum import ClientTypeEnum
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')

@api.route('/register', methods=['POST']) #新增资源 使用post
def create_client():
    # 注册 登录
    # 参数 校验 接受参数
    # WTForms
    # 接受参数 表单 一般是=网页端  json 一般是移动端
    # 获取参数
    data = request.json
    form = ClientForm(data=data)
    if form.validate(): # 校验通过
        # 对于不同的注册方式采用不同的方法：
        promise = {
            ClientTypeEnum.USER_EMAIL: _register_user_by_email
        }
        promise[form.type.data]()

    return 'success'

def _register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)