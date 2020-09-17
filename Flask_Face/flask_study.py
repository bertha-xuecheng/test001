#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 23:51
# @Author  : 雪成
# @Software: PyCharm
from flask import Flask, request, redirect, make_response, url_for

"""
1.get 请求获取参数
2，设置cookie
3.自己构造响应 make_response()
4.跳转 redirect(url_for(函数名字))
5. <> 动态生成路由
"""

app = Flask(__name__)


@app.route('/set/<name>')
def set_cookie(name):
    """
    构造一个响应添加cookie
    :param name:
    :return:
    """
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name, max_age=3600)
    return response


@app.route("/hello")
def hello():
    # 1.从请求中获取参数,从get请求中获取参数 request.args  如果从post里面获取参数 request.get_json()
    name = request.args.get('name')
    if name is None:
        # 从cookie中进行获取name值  request.cookies 获取请求头中的所有的cookie值
        name = request.cookies.get('name')
    return '<h1>hello word,%s</h1>' % name
    # 2,对前端传来的参数【动态路由】进行验证 if name  None 就从cookie中进行获取name值
    # 3.如果前端传值 name 那么直接返回响应
    # 4.最终都会返回同一个响应  【欢迎 name】


if __name__ == '__main__':
    app.run(debug=True)
