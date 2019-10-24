# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 10:33
# @Author  : lilong
# @File    : base.py
# @Description:
from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException

class BaseForm(Form):
    def __init__(self):
        # data = request.json
        data = request.get_json(silent=True) # 如果body为空的话不报错
        # 可以通过查询参数来进行validate
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self