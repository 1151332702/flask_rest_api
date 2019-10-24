# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 12:46
# @Author  : lilong
# @File    : book.py
# @Description:
from sqlalchemy import Column, Integer, String, orm

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # 该装饰器表示实例化对象的时候会执行该方法
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding', 'publisher', 'price', 'summary']


