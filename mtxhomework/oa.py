#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/31 22:51
# @Author  : 雪成
# @Software: PyCharm
# import yaml
#
# with open('user.yml', mode='r', encoding='utf-8') as f:
#     data = yaml.load(f.read(), Loader=yaml.FullLoader)
#     data = data['test_login']
#     print(data)
#     temp = list()
#     for i in data.values():
#         temp.append(i)
#     print(temp[0])
#     print(temp)
#     print(type(temp))


# user = data.get('deviceName')
# pwd = data.get('unicodeKeyboard')
# print('user的值为', user)
#
#
# print('pwd的值为', pwd)

def acc():
    a = {'test_login': {'test_login_001': {'accounts': 'fanxuecheng', 'pwd': '', 'exp': '密码格式 6~18 个字符之间'},
                        'test_login_002': {'accounts': '', 'pwd': 'fxc123456', 'exp': '登录账号有误'},
                        'test_login_003': {'accounts': 'fanCCCCC', 'pwd': '1221F2313', 'exp': '帐号不存在'},
                        'test_login_004': {'accounts': 'fanxuecheng', 'pwd': 'FXC1231RTG', 'exp': '密码错误'}}}

    temp = list()
    data = a.get('test_login')
    for i in data.values():
        temp.append(i)
    print(temp)
    return temp

acc()