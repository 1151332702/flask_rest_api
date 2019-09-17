# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:05
# @Author  : lilong
# @File    : app.py
# @Description:
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        raise ServerError()

class Flask(_Flask):
    json_encoder = JSONEncoder

