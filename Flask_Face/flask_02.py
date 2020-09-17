#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 22:36
# @Author  : 雪成
# @Software: PyCharm
from flask import Flask, make_response, request, Markup

app = Flask(__name__)


@app.route('/set_cookies')
def set_cookie():
    response = make_response("success")
    response.set_cookie('w3cshool', 'w3cshool', max_age=3600)
    return response


@app.route('/get_cookies')
def get_cookie():
    cookies = request.cookies.get('w3cshool')
    return cookies


@app.route("/delete_cookies")
def delete_cookie():
    res = make_response('del success')
    res.delete_cookie('w3cshool')
    return res
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.from ['uesrname'], )


if __name__ == '__main__':
    app.run(debug=True)
