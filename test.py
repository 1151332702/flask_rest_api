# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 17:49
# @Author  : lilong
# @File    : test.py
# @Description:  测试文件
import re
def func_args(pre='xiaoqiang'):
    def w_test_log(func):
        def inner():
            print('...记录日志...visitor is %s' % pre)
            func()
        return inner
    return w_test_log

@func_args('wangcai')
def test_log():
    print('this is test log')

p = r'^[A-Za-z0-9_*&$#@]{6,22}$'
print(re.match(p, 'sdkl$12_3j*fg'))