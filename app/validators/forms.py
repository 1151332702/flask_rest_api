# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 10:49
# @Author  : lilong
# @File    : forms.py
# @Description:
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms import ValidationError

from app.libs.ClientTypeEnum import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(),
                                      length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired(),
                                    ])

    # 自定义校验器
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()

class BookSearchForm(Form):
    q = StringField(validators=[DataRequired()])

class TokenForm(Form):
    token = StringField(validators=[DataRequired()])