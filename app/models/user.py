# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 18:22
# @Author  : lilong
# @File    : user.py
# @Description:
from sqlalchemy import inspect, Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from .base import Base, db

class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @orm.reconstructor
    def __init__(self): # 通过sqlalchemy常用语法构建的User对象不会执行init方法，但是打上orm.reconstructor就可以执行了。
                        # 这样就可以为对象赋予实例变量值， 类变量改变了之后，所有该类的对象，类变量都改变了
        self.fieles = ['id', 'email', 'nickname', 'auth']



    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFound(msg='user not found..')
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}


    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
