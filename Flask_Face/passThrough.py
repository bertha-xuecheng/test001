#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 0:39
# @Author  : 雪成
# @Software: PyCharm
import requests
from flask import Flask, make_response


def PassThrough(data):
    """
    1。重新对原有的接口发送请求 -- 获取响应
    2.构造响应 make_response()构造响应
    3.把响应返回回来
    :param data: 指的是前端收集到的请求参数
    :return:
    """
    url = 'http://127.0.0.1:5000/login'
    # 模拟发起请求
    result = requests.post(url, json=data)
    # 2.构造响应 make_response() 构造响应 [是把想返回的值放在 make_response 这个函数里面]
    resp = make_response(result.json())
    return resp


def PassThroughRe(data):
    """
    1。对注册的功能进行透传
    2.构造响应 make_response()构造响应
    3.把响应返回回来
    :param data: 指的是前端收集到的请求参数
    :return:
    """
    url = "http://127.0.0.1:5000/register"
    # 模拟发起请求
    result = requests.post(url, json=data)
    # 2.构造响应 make_response() 构造响应 [是把想返回的值放在 make_response 这个函数里面]
    resp = make_response(result.json())
    return resp
