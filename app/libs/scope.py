# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 17:27
# @Author  : lilong
# @File    : scope.py
# @Description:
class Scope:
    allow_api = []
    allow_moudle = []
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # 去重
        self.allow_api = list(set(self.allow_api))

        self.allow_moudle = self.allow_moudle + other.allow_moudle
        # 去重
        self.allow_moudle = list(set(self.allow_moudle))
        return self

class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']
    # allow_moudle = ['v1.user']
    def __init__(self):
        self + UserScope()

class UserScope:
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']

def is_in_scope(scope, endpoint):
    sp = endpoint.split('+')
    red_name = sp[0]
    func_name = sp[1]
    scope = globals()[scope]()
    if func_name in scope.allow_api:
        return True
    if red_name in scope.allow_moudle:
        return True
    return False