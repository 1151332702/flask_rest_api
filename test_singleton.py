# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 16:37
# @Author  : lilong
# @File    : test_singleton.py
# @Description:  单例模式
def singletom(cls):
    _instance = {}
    def decorator(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return decorator

@singletom
class A(object):
    a = 100
    def __init__(self, x):
        self.x = x

class B(object):
    a = 100
    def __init__(self, x):
        self.x = x

# 利用线程实现
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

o1 = Singleton()
o2 = Singleton()
print(o1)
print(o2)