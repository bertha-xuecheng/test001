#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/7 2:16
# @Author  : 雪成
# @Software: PyCharm
def run(fn):
    def add():
        flag = True
        while flag:
            with open(file='user', mode='a+', encoding='utf-8') as f, \
                    open(file='user', mode='r', encoding='utf-8') as f1:
                lis = []
                for line in f1:
                    users = line.strip().split("|")[0]
                    lis.append(users)
                print(lis)
                username = input("请输入注册的用户名：")
                if not username.split():
                    print("您输入的内容为空请检查")
                elif username in lis:
                    print("您输入的用户名已经存在,请重新输入")
                elif username == " ":
                    print("您输入的含有非法字符请检查 !!!!")
                elif " " in username:
                    print("您输入的含有非法字符请检查 !!!!")
                else:
                    password = input("请输入密码：").swapcase()
                    f.write(username + "|" + password + "\n")
                    flag = False
                    print('注册成功')
                    fn()

    return add


@run
def login():
    with open(file='user', mode='r', encoding='utf-8') as f:
        lis = []
        for i in f:
            u = i.strip().split("|")[0]
            pw = i.strip().split("|")[1]
            lis.append(u)
        name = input("请输入登陆用户名： ")
        if name not in lis:
            print('您输入的用户名不存在, 请先注册!!!!')
        elif name == u:
            pwd = input("请输入密码： ")
            if pwd == pw:
                print('登录成功')
            else:
                print('密码错误请重新输入')


login()
