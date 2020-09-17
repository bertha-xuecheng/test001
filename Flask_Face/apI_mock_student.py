#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 0:18
# @Author  : 雪成
# @Software: PyCharm
"""
url地址: http://127.0.0.1:9999/login/mock
# 需求:
# 登录接口被锁定
"""

from flask import Flask, jsonify, request
from Flask_Face.passThrough import PassThrough, PassThroughRe

app = Flask(__name__)
# 响应里面识别中文，如下更改
app.config['JSON_AS_ASCII'] = False


@app.route('/login/mock', methods=['POST'])
def login():
    """
    实现接口被锁定功能
    :return:
    """
    data = request.get_json()
    name = data.get('name')
    # 如果name等于lock,提示用户被锁定无法登陆
    if name == 'lock':
        return jsonify({'data': data, 'message': '您的用户名已经被锁定无法登录', 'code': 200})
    else:
        # 不走锁定的mock服务，走正常登录的功能
        resp = PassThrough(data)
        return resp


@app.route('/<func>', methods=['POST'])
def register(func):
    data = request.get_json()
    if func == 'register':
        resp = PassThroughRe(data)
        return resp


if __name__ == '__main__':
    app.run(debug=True, port=9999)
