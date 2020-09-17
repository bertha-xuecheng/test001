#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 22:58
# @Author  : 雪成
# @Software: PyCharm
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    # flask是通过request来接收的，前端的参数都是在request里面
    # post 请求 request.get_json 获取数据，返回的数据就是字典的形式
    # 接口中我们自己定义了必穿参数 name pwd
    # 1. 获取前端穿来的请求参数
    data = request.get_json()
    #  2. 进行参数校验
    if 'name' not in data or not data.get('name'):
        return jsonify(
            {
                'code': 404,
                'message': 'Invalid parameter name'
            }
        )
    if 'pwd' not in data or not data.get('pwd'):
        return jsonify(
            {
                'code': 404,
                'message': 'Invalid parameter pwd'
            }
        )
    try:
        name = data.get('name')
        pwd = data.get('pwd')
        print(name)
        print(pwd)

        # 3. 处理参数
        # 4，返回响应
        # 请求
        return jsonify(
            {'code': 200,
             'message': 'ok',
             "data": data

             }
        )
    except Exception as e:
        return jsonify(
            {'code': 1001,
             'message': e,
             "data": data

             }
        )


if __name__ == '__main__':
    app.run(debug=True)
