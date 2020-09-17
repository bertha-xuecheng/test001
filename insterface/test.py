#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 17:59
# @Author  : 雪成
# @Software: PyCharm
import requests
from faker import Faker
from datetime import datetime

fake = Faker(locale='zh_CN')

session = requests.Session()

url = 'http://beta.admin.edianzu.cn/index.php?r=site/login&controller=site&action=index'

data = {

    'LoginForm[username]': '范雪成',
    'LoginForm[password]': 'fxc123456'
}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = session.post(url, data=data, headers=headers)
print('获取到的cookies的值是', response.cookies)

print("========================================================================")


def sku_code():
    global session
    url = "http://stage-core-asset.edianzu.cn/stock/getAssetDepreList"

    headers = {'X-Requested-With': 'XMLHttpRequest'}
    data = {
        'pageNumber': 1,
        'pageSize': 10,
        'sn': "R8D2GCA"

    }

    res = session.post(url, data=data, headers=headers)
    print(res.text)
    print('啊哈哈哈哈', res.json())


sku_code()
# print("========================================================================")
#
# url = 'http://stage.erp.edianzu.cn/product/saveMaintainPrice'
#
# headers = {'X-Requested-With': 'XMLHttpRequest'}
# data = {
#     'modelNumber': '小',
#     'majorCategory': 110,
#     'subCategory': 22,
#     'dealWay': 111,
#     'amount': -1
#
# }
# re = session.post(url, data=data, headers=headers)
# print(re.json())
#
# print("========================================================================")
#
# url = 'http://stage.erp.edianzu.cn/productBrand/brandValidateName'
#
# headers = {'X-Requested-With': 'XMLHttpRequest'}
# data = {
#     'bcode': '租返专用11',
#     'name': 1
#
# }
# re = session.post(url, data=data, headers=headers)
# print(re.json())
#
# print("========================================================================")
#
# url = 'http://stage-finance-cloud.edianzu.cn/v1/u8cproapi/certificate/regenerateCreateCertificate'
# headers = {'X-Requested-With': 'XMLHttpRequest'}
# data = {
#     "examineStatus": 1,
#     "pushStatus": 0,
#     "certificateIds": 708061,
#     'delOrChargeAgainst': 1
# }
#
# re = session.post(url, data, headers=headers)
# print(re.text)
#
# url = "http://stage-core-asset.edianzu.cn/stock/getAssetDepreList"
# data = {
#     'pageNumber': 1,
#     'pageSize': 10,
#     'sn': "R8D2GCA"
#
# }
# headers = {'X-Requested-With': 'XMLHttpRequest'}
# response = session.post(url, data=data, headers=headers)
# res = response.json()
# print(res)
