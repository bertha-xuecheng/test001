#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/29 21:23
# @Author  : 雪成
# @Software: PyCharm
import requests

"""

1.requests.text  转换成文本  场景：返回值是文本
2.requests.json() 返回的是字典结果，type() 验证数据格式，得到里面的值按照字典处理
3.request.content   返回的是二进制文件  场景 返回值为图片或者MP3  MP4

目的 : 断言  相应提取

"""
url = 'http://localhost:8080/pinter/com/getSku'

params = {'id': '1'}
# get请求可以使用params 这个关键字去接受请求参数
response = requests.get(url, params=params)
res = response.json()
# 获取json中sku_id的值
sku_id = res['data']['skuId']
print(sku_id)
print(response)
print(response.json())


