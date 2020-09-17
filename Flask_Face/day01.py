#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 10:13
# @Author  : 雪成
# @Software: PyCharm
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_word():
    return "hello word"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('name') is None:
        return jsonify(
            {'code': 404, 'message': 'is not null', 'data': data}
        )
    elif data.get('pwd') is None:
        return jsonify(
            {'code': 404, 'message': 'is not null', 'data': data}
        )
    elif 'name' or 'pwd' is not data:
        return jsonify(
            {'code': 404, 'message': ' name or pwd is not null', 'data': data}
        )

    name = data.get('name')
    pwd = data.get('pwd')
    print(data)
    print(name)
    print(pwd)
    # 2，参数校验

    # 3.处理参数
    # 4.返回响应
    return jsonify(
        {
            'code': 200,
            'message': 'ok',
            "data": data
        }

    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)
