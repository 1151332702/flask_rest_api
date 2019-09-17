# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 9:18
# @Author  : lilong
# @File    : error.py
# @Description:
from flask import request, json
from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    code = 500
    msg = 'unknown error...'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request= request.method + ' ' + self.get_url_no_param()
        )
        return json.dumps(body)

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]
        return main_path