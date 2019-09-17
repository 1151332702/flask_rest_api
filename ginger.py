# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:04
# @Author  : lilong
# @File    : ginger.py
# @Description:
from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if app.config['DEBUG']:
            raise e
        else:
            return ServerError()

if __name__ == '__main__':
    app.run(port=11511, debug=True)