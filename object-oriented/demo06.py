#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/10 1:23
# @Author  : 雪成
# @Software: PyCharm

status_dic = {
    'username': None,
    'status': False
}


def get_user_pwd():
    """
    获取密码
    pass_word[0].strip() 用户名 pass_word[1].strip() 密码
    如果用户名 = 密码   key=value 那么就返回
    :return:
    """
    password_dic = {}
    with open(file='user', mode='r', encoding='utf-8') as f:
        for line in f:
            pass_word = line.strip().split("|")
            password_dic[pass_word[0].strip()] = pass_word[1].strip()
    return password_dic


def login():
    """
    登录
    :return:
    """
    user_dic = get_user_pwd()
    count = 1
    while count < 4:
        username = input("请输入用户名： ")
        password = input("请输入密码： ")
        # 如果用户名在 user_dic 这个字典里 和 密码 等于 user_dic[用户名]的value也就是密码返回登录成功
        if username in user_dic and password == user_dic.get(username):
            print("登录成功")
            status_dic['username'] = username
            status_dic['status'] = True
            return True
        else:
            print("用户名密码错误，请检查是否注册，或者是否输入有误 ！！")
        count += 1


def register():
    """
    如果用户名在这个文件里就提示用户名已经存在，否则就注册成功写入username文件
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


def auth(f):
    """
    判断用户是否登录，装饰器
    :param f:
    :return:
    """

    def inner(*args, **kwargs):

        if status_dic['status']:
            ret = f(*args, **kwargs)
            """访问函数之后的操作，功能。。。。。"""
            return ret
        else:
            if login():  # 调用login函数，如果登录成功就访问其他功能
                ret = f(*args, **kwargs)
                return ret
            else:
                print("登录失败,请先注册账号，或重新登录！！！")

    return inner


@auth
def article():
    with open('article', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line)
    print("欢迎访问文章页面")


@auth
def comment():
    print("欢迎访问评论页面")


@auth
def dariy():
    print('欢迎访问日记页面')


@auth
def collections():
    print("欢迎访问收藏页面")


def login_out():
    pass


num = ("请登录", '请注册', '进入文章页面', '进入评论页面', '进入日记页面', '进入收藏页面', '注销账号', '退出程序')
while 1:
    for i in range(len(num)):
        print(i + 1, num[i])

    n = input("请输入你要执行的菜单:")
    if n == '1':
        login()
    elif n == '2':
        register()
    elif n == "3":
        article()
    elif n == "4":
        comment()
    elif n == "5":
        dariy()
    elif n == "6":
        collections()
    elif n == "7":
        login_out()
    elif n == "8":
        print("程序退出成功")
        exit()
    else:
        print("对不起. 您输入的菜单不存在. 请重新输入")
