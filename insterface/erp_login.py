#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 17:04
# @Author  : 雪成
# @Software: PyCharm
import pytest
import allure
import config
import requests
from faker import Faker
from datetime import datetime

fake = Faker(locale='zh_CN')

session = requests.Session()
data_list = {
    ('ELIBT450S01', fake.numerify(), '22222', '保存成功！'),
    ('A', '222', '222', '该SKU不存在，请确认！')}

ids = ['保存成功！', '该SKU不存在，请确认！']


class TestMtxLogin:
    headers = {'X-Requested-With': 'XMLHttpRequest'}

    @allure.title('登录admin系统')
    @allure.feature('测试登录功能')
    @allure.description('输入用户名输入密码登陆成功')
    @pytest.mark.run(order=1)
    def test_login(self):
        global session
        url = 'http://beta.admin.edianzu.cn/index.php?r=site/login&controller=site&action=index'

        data = {

            'LoginForm[username]': '范雪成',
            'LoginForm[password]': 'fxc123456'
        }

        response = session.post(url, data=data, headers=self.headers)
        # print(response.status_code)
        # print('获取到的响应结果是', response)
        print(response.status_code)
        print("===================================================")
        print('type的值是', type(response.status_code))
        print("===================================================")
        # print(response.content)
        # print(response.headers)
        # print(response.text)
        # return session


if __name__ == '__main__':
    TestMtxLogin().test_login()
# erp 搜索
# @allure.title("搜索订单号")
# @allure.feature('测试搜索订单号')
# @allure.description('订单管理页面根据订单号:2020082910043775010搜索成功')
# def orders():
#     # global session
#     url = 'http://stage-console.edianzu.cn/saasOrder/orderQuery/queryAll?macValue=error'
#     data = {
#
#         'pageNumber': 1,
#         'pageSize': 10,
#         'startDate': '2020-08-01',
#         'isVirtual': 0,
#         'endDate': datetime.now().strftime('%Y-%m-%d'),
#         'status': 0,
#         'orderSn': '2020082910043775010',
#         'saasInstance': 0
#
#     }
#
#     response = requests.post(url, headers=config.HEADERS, data=data, cookies=config.COOKIES)
#     res = response.text
#     res01 = response.content
#     print(res01)
#     print('获取到的响应结果是', res)
#     # assert res['data']['rows'][0]['orderSn'] == '2020082910043775010'
#     # assert res['code'] == 0
#     # assert res['message'] == 'SUCCESS'
#     # return res


# orders()
# @allure.title("sku列表维修价格管理测试用例")
# @allure.feature('赔偿价格新增成功')
# @allure.description('重复新增相同的数据')
# @pytest.mark.run(order=3)
# def test_sku(self):
#     global session
#     url = 'http://stage.erp.edianzu.cn/product/saveMaintainPrice'
#     data = {
#         'modelNumber': '小',
#         'majorCategory': 110,
#         'subCategory': 22,
#         'dealWay': 111,
#         'amount': -1}
#
#     response = session.post(url, headers=self.headers, data=data)
#     res = response.json()
#     print('获取到的响应结果是', res)
#     assert res['code'] == 0
#     assert res['message'] == '保存成功'
#
#
# @pytest.mark.parametrize("value", data_list, ids=ids)
# @allure.title("sku列表配件赔偿价格测试用例")
# @allure.feature('配件赔偿价格新增成功')
# @allure.description('配件赔偿价格新增，新增sku==EAAPMF88500')
# @pytest.mark.run(order=4)
# def test_sku_demo(self, value):
#     global session
#     url = 'http://stage.erp.edianzu.cn/product/saveProductComoensatePrice'
#     data = {
#         'skuCode': value[0],
#         'skuMinAmount': value[1],
#         'skuMaxAmount': value[2]}
#     response = session.post(url, data=data, headers=self.headers)
#     res = response.json()
#     print('获取到的响应结果是', res)
#     assert res['message'] == value[3]
