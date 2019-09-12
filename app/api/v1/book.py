# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:24
# @Author  : lilong
# @File    : book.py
# @Description:
from flask import Blueprint
from app.libs.redprint import Redprint

# book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/get')
def get_book():
    return 'i am book'

@api.route('/create')
def create_book():
    return 'create book'