#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 0:18
# @Author  : 雪成
# @Software: PyCharm
"""
接口文档
接口名字      method   url                              参数
登录接口      post     http://127.0.0.1:5000/login       {"name":"yaoyao","password": "yaoyao"}
注册接口      post     http://127.0.0.1:5000/register    {"name":"yaoyao","password": "yaoyao"}
2.没有页面，只有接口
"""

# 需求:
# 登录接口没有黑名单这个功能的
# todo 做一个mock服务(挡板),实现黑名单这个功能
# todo 这个登录接口原有的功能也是要保留的(登录成功...)--透传

from flask import Flask, jsonify, request
from Flask_Face.passThrough import PassThrough, PassThroughRe

app = Flask(__name__)
# 响应里面识别中文，如下更改
app.config['JSON_AS_ASCII'] = False


@app.route('/login/mock', methods=['POST'])
def login():
    """
    实现黑名单功能
    :return:
    """
    data = request.get_json()
    name = data.get('name')
    if name == 'blacklist':
        return jsonify({'data': data, 'message': '您已经被我们公司加入黑名单', 'code': 200})
    else:
        # 不走黑名单的mock服务，走原来的功能
        resp = PassThrough(data)
        return resp


# 透传注册 为什么实现透传注册功能， 原因：一个ip地址和端口号 port 注册的url最好和以前服务的url一致
@app.route('/<func>', methods=['POST'])
def register(func):
    # 判断条件就是前端穿来的参数
    data = request.get_json()
    if func == 'register':
        resp = PassThroughRe(data)
        return resp


if __name__ == '__main__':
    app.run(debug=True, port=9999)
