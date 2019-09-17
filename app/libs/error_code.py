# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 8:59
# @Author  : lilong
# @File    : error_code.py
# @Description:
from app.libs.error import APIException

class ClientTypeError(APIException):
    code = 400 # 参数错误
    msg = 'client is invalid.'
    error_code = 1006

class ParameterException(APIException):
    code = 400 # 参数错误
    msg = 'invalid parameter.'
    error_code = 1000

class Success(APIException):
    code = 200
    msg = 'ok'
    error_code = 0

class ServerError(APIException):
    code = 500
    msg = 'unknown error...'
    error_code = 999

class NotFound(APIException):
    code = 404
    msg = 'the resource is not found..'
    error_code = 1001

class AuthFailed(APIException):
    code = 401 # 授权失败
    msg = 'authorization failed..'
    error_code = 1005