#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Author雪成

# 菜单: ("查看员⼯信息","添加员⼯信息", "修改员⼯信息", "删除员⼯信息", "退出")

import os

'''查看员⼯信息'''


def Viewemployeeinformation():
    id = int(input('请输入你要查看的全部员工信息的id: '))
    f = open('emp.db', mode='r', encoding='utf-8')
    for line in f:
        lst = line.strip().split(',')
        print(f"id:{lst[0]}, 姓名:{lst[1]}, 生日:{lst[2]}, 薪资:{lst[3]},更新时间:{lst[4]}")
    print('此内容为全部的员工信息')
    f.close()


'''添加员⼯信息'''


def Addemployeeinformation():
    while 1:
        id = input('请输入员工id: ')
        f = open('emp.db', mode='r', encoding='utf-8')
        for line in f:
            if id == line.strip().split(',')[0]:  # 判断id是否存在
                print('您录入的id已重复')
                break
        else:
            print('您输入的id可以使用')
            name = input('请输入员姓名: ').swapcase()
            birthday = input('请输入员工生日: ')
            salary = input('请输入员工薪资: ')
            input_time = input('请输入修改时间: ')
            f = open('emp.db', mode='a', encoding='utf-8')
            f.write(id + ',' + name + ',' + birthday + ',' + salary + ',' + input_time + "\n")
            f.close()
            print('增加成功')


'''修改员⼯信息:显示所有员⼯信息. 然后让⽤户选择要修改的员⼯的id. 然后让⽤户输⼊员⼯的⼯资,将员⼯的⼯资修改为⽤户输⼊的⼯资. 其余内容不做改动  '''


def Modifyemployeeinformation():
    '''输入id'''
    flag = True
    while flag:
        id = input('请输入您要修改的id: ')
        f = open('emp.db', mode='r', encoding='utf-8')
        for line in f:
            lst = line.strip().split(',')
            if id == lst[0]:
                print(f"id:{lst[0]},姓名:{lst[1]},生日:{lst[2]},薪资:{lst[3]},更新时间:{lst[4]}")
                flag = False
                break
        else:
            print('您输入的id不存在')
    f.flush()
    f.close()

    salary = input('请输入薪资: ')  # 输入薪资进行修改
    with open("emp.db", mode="r", encoding="utf-8") as f1, \
            open("emp.db_副本", mode="w", encoding="utf-8") as f2:
        for line in f1:
            lst = line.strip().split(",")
            if id == lst[0]:
                line = f"{id},{lst[1]},{lst[2]},{salary},{lst[4]}"
            f2.write(line)  # 修改
    os.remove('emp.db')
    os.rename('emp.db_副本', 'emp.db')
    print("修改员工信息完毕!!!")


def Deleteemployeeinformation():
    id = input("请输入你要删除的员工的id")
    with open("emp.db", mode="r", encoding="utf-8") as f1, \
            open("emp.db_副本", mode="w", encoding="utf-8") as f2:
        for line in f1:
            if id == line.strip().split(",")[0]:
                continue
        f2.write(line)
    os.remove("emp.db")
    os.rename("emp.db_副本", "emp.db")
    print("删除完毕!!!!")


menu = ("查看员工信息", "添加员工信息", "修改员工信息", "删除员工信息", "退出")
while 1:
    for i in range(len(menu)):
        print(i + 1, menu[i])

    n = input("请输入你要执行的菜单:")
    if n == '1':
        Viewemployeeinformation()
    elif n == '2':
        Addemployeeinformation()
    elif n == "3":
        Modifyemployeeinformation()
    elif n == "4":
        Deleteemployeeinformation()
    elif n == "5":
        print("程序退出")
        exit()
    else:
        print("对不起. 您输入的菜单不存在. 请重新输入")
