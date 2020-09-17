#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/7 1:01
# @Author  : 雪成
# @Software: PyCharm


login_flag = False


def login(fn):
    """
    实现登录功能
    :return:
    """

    def inner():
        global login_flag
        if login_flag:
            fn()
        else:
            with open(file='user', mode='r', encoding='utf-8') as f:
                username = input("请输入用户名： ")
                password = input("请输入密码: ")
                for line in f:
                    user = line.strip().split("|")[0]
                    pwd = line.strip().split("|")[1]
                    if user == username and pwd == password:
                        print("登录成功")
                        login_flag = True
                        fn()
                        break
                    else:
                        print("您输入的用户名不存在或者密码错误, 请进行注册！！！！！")
        return inner


# 注册

def register():
    """
    注册功能
    :return:
    """
    flag = True
    while flag:
        with open(file='user', mode='a+', encoding='utf-8') as f, \
                open(file='user', mode='r', encoding='utf-8') as f1:
            lis = []
            for line in f1:
                users = line.strip().split("|")[0]
                lis.append(users)
            username = input("请输入用户名：")
            if username in lis:
                print("您输入的用户名已经存在,请重新输入")
            elif username == " ":
                print("您输入的含有非法字符请检查 !!!!")
            elif " " in username:
                print("您输入的含有非法字符请检查 !!!!")
            elif username == '':
                print("用户名不能为空请检查")
            else:
                password = input("请输入密码：")
                f.write(username + "|" + password + "\n")
                print('注册成功')
                flag = False


@login
def read():
    """
    读取文章
    :return:
    """
    with open(file='article', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


menu = ("注册", "登录", "查看文章", "退出")
while 1:
    for i in range(len(menu)):
        print(i + 1, menu[i])

    n = input("请输入你要执行的菜单:")
    if n == '1':
        register()
    elif n == '2':
        pass
        # login
    elif n == "3":
        read()
    elif n == "4":
        print("程序退出")
        exit()
    else:
        print("对不起. 您输入的菜单不存在. 请重新输入")
