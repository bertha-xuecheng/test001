#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 21:41
# @Author  : 雪成
# @Software: PyCharm
import requests
import config

session = requests.Session()


def login():
    url = 'http://beta.admin.edianzu.cn/index.php?r=site/login&controller=site&action=index'

    data = {

        'LoginForm[username]': '范雪成',
        'LoginForm[password]': 'fxc123456'
    }
    response = session.post(url=url, data=data, headers=config.HEADERS)
    print(response)
    return session


def core_asset():
    url = "http://stage-core-asset.edianzu.cn/stock/getAssetDepreList"
    data = {
        'pageNumber': 1,
        'pageSize': 10,
        'sn': "R8D2GCA"
    }

    res = session.post(url, data, headers=config.HEADERS)
    print('cookies的值是', res.cookies)
    print('headers的值是', res.headers)
    print(res.content)
    print(res.status_code)
    res_json = res.json()
    print(res_json)
    res_data_sn = res_json['data'][0]['sn']
    print('sn的值是', res_data_sn)
    # print(type(res_data))
    # res_sn = res_data[0]
    # print(res_sn)
    # sn = res_sn['sn']
    # print(sn)


if __name__ == '__main__':
    login()
    core_asset()
