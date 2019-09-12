# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 10:43
# @Author  : lilong
# @File    : ClientTypeEnum.py
# @Description:
from enum import Enum

class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101
    USER_MINA = 200 # 微信小程序
    USER_WX = 201