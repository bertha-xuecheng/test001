#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 13:46
# @Author  : 雪成
# @Software: PyCharm
# 定义一个圆形，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形
#
# class Round:
#     def __init__(self, radius):
#         self.radius = radius
#
#
# radii01 = Round(0.5)
# print(radii01.__dict__)
# radii02 = Round(10)
# print(radii02.__dict__)
import os


def login(name, password, filepath='user_info'):
    """

    :param name: 用户名
    :param password: 密码
    :param filepath: 文件路径
    :return:
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f:
            user, pwd = line.strip().split('|')
            if user == name and pwd == password:
                return True, name, pwd
        else:
            return False


# 定义一个用户类，用户名和密码都是这个类的属性，实例化两个用户
class User:
    def __init__(self, user_name, pass_word):
        self.user_name = user_name
        self.pass_word = pass_word

    # 登陆成功后才能创建对象

    def change_password(self):
        old_pwd = input('输入原密码：')
        new_pwd = input('输入新密码：')
        flag = False
        with open('user_info', mode='r', encoding='utf-8')as f1, \
                open('user_info.bak', mode='w', encoding='utf-8') as f2:
            for line in f1:
                username, password = line.strip().split('|')
                if username == self.user_name and password == old_pwd:
                    line = '%s|%s\n' % (username, new_pwd)
                    flag = True
                f2.write(line)

        os.remove("user_info")
        os.rename('user_info.bak', 'user_info')
        return flag


name = input('请输入用户名： ')
password = input("请输入密码： ")
ret = login(name, password)
if ret:
    print('登录成功')
    user_obj = User(name, password)
    res = user_obj.change_password()
    if res:
        print('修改成功')
    else:
        print('修改失败')
