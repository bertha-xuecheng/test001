#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/29 22:16
# @Author  : 雪成
# @Software: PyCharm
import requests

"""
post 
传递参数的时候需要使用关键字参数，data json file
1.json = 参数  参数json类型的那么前面一定是json
2.data = 参数  参数 k = value k = json
3.files = 参数  使用于上传文件

"""
url = 'http://localhost:8080/pinter/com/login'

data = {
    'userName': 'admin',
    'password': '1234'
}

# header 是否需要穿特殊类型
response = requests.post(url, data=data,varify=False)
res = response.json()
print(res)

print("=================================================")
# 参数是json类型的

url = 'http://localhost:8080/pinter/com/register'

json = {"userName": "test", "password": "1234", "gender": 1, "phoneNum": "110", "email": "beihe@163.com",
        "address": "Beijing"}

response = requests.post(url, json=json)
print("参数是json类型的", response.json())

print("================================================")
# 参数是k = json类型的


url = 'http://localhost:8080/pinter/com/buy'

data = {

    'param': {"skuId": 123, "num": 10}
}

response = requests.post(url, data=data)
print("参数是k = json类型的", response.json())

print("==========================================")
# 表单上传的接口 【上传文件】
url = "http://localhost:8080/pinter/file/api/upload"

# 参数构造字典

data = {
    'file': './Requests_get.py'
}

response = requests.post(url, files=data)

print(response.text)
