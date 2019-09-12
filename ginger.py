# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:04
# @Author  : lilong
# @File    : ginger.py
# @Description:
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=11511, debug=True)