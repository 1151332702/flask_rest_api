# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:24
# @Author  : lilong
# @File    : book.py
# @Description:
from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book

from app.validators.forms import BookSearchForm

api = Redprint('book')

@api.route('/search')
def search_book():
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(
        or_(
            Book.title.like(q),
            Book.publisher.like(q)
        )
    ).all()
    # 灵活的隐藏某些字段
    books = [book.hide('summary') for book in books]
    return jsonify(books)

@api.route('/<string:isbn>/detail')
def book_detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)