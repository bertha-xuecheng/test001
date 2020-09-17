#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 2:01
# @Author  : 雪成
# @Software: PyCharm
import requests
import pytest

"""
accounts pwd exp
参数化：
@pytest.mark.parametrize('','')
第一个参数： 字符串 ""
第二个参数：列表
    列表套元祖[(),(),()]
    列表套列表[[],[],[]]
"""
# 参数化信息
data_list = {
    ('fanxuecheng', 'fxc123456', '登录成功'),
    ('', 'fxc123456', '登录账号有误'),
    ('fanxuecheng', '', '密码格式 6~18 个字符之间'),
    ('fanCCCCC', '1221F2313', '帐号不存在'),
    ('fanxuecheng', 'FXC1231RTG', '密码错误')

}

ids = ['登录成功', '账号有误', '密码格式错误', '帐号不存在', '密码错误']


class TestMtxLogin:
    ip = 'http://121.42.15.146:9090'
    headers = {'X-Requested-With': 'XMLHttpRequest'}

    @pytest.mark.parametrize("value", data_list, ids=ids)
    def test_login(self, value):
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        data = {'accounts': value[0],
                'pwd': value[1]}
        response = requests.post(url, data=data, headers=self.headers)
        res = response.json()
        print('获取到的响应结果是', res)
        assert res['msg'] == value[2]

    @pytest.mark.parametrize("accounts,pwd,exp", data_list)
    def test_login_01(self, accounts, pwd, exp):
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        data = {'accounts': accounts,
                'pwd': pwd}
        response = requests.post(url, data=data, headers=self.headers)
        res = response.json()
        print('获取到的响应结果是', res)
        assert res['msg'] == exp



