#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 22:13
# @Author  : 雪成
# @Software: PyCharm
"""
简易博客园系统
1)，启动程序，首页面应该显示成如下格式：
                欢迎来到博客园首页
                1:请登录
                2:请注册
                3:文章页面
                4:日记页面
                5:注销
                6:退出程序

2)，用户输入选项，3, 4选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从  register  文件中读取验证 ，三次机会，没成功则结束整个程序，
    登录成功之后，可以选择访问 3, 4 ， 访问页面之前，必须要在 log文件中 打印日志，
    日志格式为 --> 用户:xx在xx年xx月xx日 执行了xxx函数，访问页面时，
    页面内容为：欢迎 xx 用户访问评论（文章，日记）页面
4)，如果用户没有注册，则可以选择注册， 注册成功之后， 可以自动完成登录， 然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
6)，退出程序为结束整个程序运行。



坑: 由于所有的操作都要带着用户名的. 比如, 查看alex的文章. 打开的文件就是alex_文章.txt.
所以, 我们需要在登录的时候把用户名记录在全局变量中. 方便其他函数访问.

做题顺序: 先把框架搭起来. 让用户选择不同的菜单.
根据不同的菜单. 执行不同的函数.
先做:
    注册
    登录
    日志(装饰器)
    登录状态检查(装饰器)
    注销
    退出程序
后做:
    文章
    日记
其中进入文章和日记之后:
进入文章页面:
    1. 查看文章
    2. 添加文章
    3. 删除文章
    4. 返回上一单元

进入日记页面:
    1. 查看日记
    2. 添加日记
    3. 删除日记
    4. 返回单一单元

思路: 在注册用户的时候, 给该用户创建两个文件, 一个是存储文章的, 一个是存储日记的.
alex_文章.txt:
    {"title":"昨夜大保健被抓实录", "content":"人在江湖飘, 哪能不去piao"}
    {"title":"前天大保健被抓实录", "content":"这家不好, 以后不来了"}
    {"title":标题, "content": 文章内容}
alex_日记.txt:
    2019-01-02$$今天很无聊. 在家看电影
    2019-01-02$$今天很无聊. 在家看电影
    时间$$内容


至理名言(我说的): 简单的问题复杂化, 复杂的问题简单化. 至繁归于至简!
最后: 以上思路是我个人的. 你可以有自己的想法和发挥. 加油干吧.
 1:请登录
                2:请注册
                3:文章页面
                4:日记页面
                5:注销
                6:退出程序
先做:
    注册
    登录
    日志(装饰器)
    登录状态检查(装饰器)
    注销
    退出程序
后做:
    文章
    日记

"""

import os

print("欢迎来到博客园首页  1:请登录, 2:请注册, 3:文章页面, 4:日记页面, 5:注销, 6:退出程序")


def register():
    flag = True
    while flag:
        with open(file='register', mode='a+', encoding='utf-8') as f:
            lis = []
            user_name = input('请输入您需要注册的用户名： ')
            if user_name == " " or " " in user_name:
                print('输入的内容中含有非法字符请重新输入')
            else:
                f.seek(0)
                lst = f.readlines()
                for line in lst:
                    user, pwd = line.strip().split(':')
                    lis.append(user)
            if user_name in lis:
                print('用户名已经存在')
            else:
                pass_word = input('请输入密码： ')
                while True:
                    password = input("请确认你输入的密码： ")
                    if password == pass_word:
                        print('注册成功')
                        strvar = user_name + ":" + pass_word + "\n"
                        f.write(strvar)
                        flag = False
                        break
                    elif password.upper() == "Q":
                        print("您已经退出密码确认环节")
                        break
                    else:
                        print('密码输入的不一致请检查')


register()
