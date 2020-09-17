#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/29 23:57
# @Author  : 雪成
# @Software: PyCharm
"""
2020606week11-3作业 一作业需求：登录和订单提交接口的测试
"""

import requests

session = requests.Session()

url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'

headers = {'X-Requested-With': 'XMLHttpRequest'}
data = {
    'accounts': 'fanxuecheng',
    'pwd': 'fxc123456'
}
response = session.post(url, data=data, headers=headers)
print(response.json())

# 加入购物车
url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/cart/save.html'
headers = {'X-Requested-With': 'XMLHttpRequest'}
data = {
    'goods_id': 12,
    'buy_type': 'goods',
    'stock': 10,
    'spec': '[{"type":"颜色","value":"粉色"},{"type":"尺码","value":"M"}]',
    'address_id': 1155,
    'payment_id ': 1,
    'site_model': 0

}

response = session.post(url, headers=headers, data=data)
print(response.json())

# 下订单

url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/buy/add.html'

headers = {'X-Requested-With': 'XMLHttpRequest'}

data = {
    'goods_id': 4,
    'buy_type': 'goods',
    'stock': 1,
    'spec':	'[]',
    'address_id': 1155,
    'payment_id': 1,
    'site_model': 0
}

response = session.post(url, data=data, headers=headers)
print(response.json())
