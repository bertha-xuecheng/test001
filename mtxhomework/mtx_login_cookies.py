#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 0:45
# @Author  : 雪成
# @Software: PyCharm
import requests


url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'

headers = {'X-Requested-With': 'XMLHttpRequest'}
data = {
    'accounts': 'fanxuecheng',
    'pwd': 'fxc123456'
}
response = requests.post(url, data=data, headers=headers)

cookies = response.cookies.get('PHPSESSID')
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
# 构造cookie
cookie = {'PHPSESSID': cookies}

response = requests.post(url, headers=headers, data=data, cookies=cookie)
print(response.json())
