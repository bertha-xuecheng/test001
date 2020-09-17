#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 21:17
# @Author  : 雪成
# @Software: PyCharm
import requests
import config
import allure
import pytest


class Login:
    # headers = {'X-Requested-With': 'XMLHttpRequest'}

    @allure.title('登录admin系统')
    @allure.feature('测试登录功能')
    @allure.description('输入用户名输入密码登陆成功')
    # @pytest.mark.run(order=1)
    def erp_login(self):
        # global session
        url = 'http://beta.admin.edianzu.cn/index.php?r=site/login&controller=site&action=index'

        data = {

            'LoginForm[username]': '范雪成',
            'LoginForm[password]': 'fxc123456'
        }
        response = requests.post(url=url, data=data, headers=config.HEADERS)
        # config.COOKIES_SSID = response.cookies['ssid'] + 'for .edianzu.cn'
        # config.COOKIES_LABELID = response.cookies['labelId'] + 'for .edianzu.cn'
        config.COOKIES = response.cookies['RequestsCookieJar']
        # res = config.COOKIES['ssid']
        print(config.COOKIES)
        """
        <RequestsCookieJar[<Cookie labelId=0.1 for .edianzu.cn/>, 
        <Cookie ssid=2d4p7kcu1e56vvrllk0a0hsjt7 for .edianzu.cn/>]>
        """

        # print('labelId的值是', res)
        return response
        # response = session.post(url, data=data, headers=self.headers)
        # response.cookies
        # print('获取到的响应结果是', response)
        # return session


if __name__ == '__main__':
    res = Login().erp_login()
    print(res.cookies)
    print(type(res.cookies))
