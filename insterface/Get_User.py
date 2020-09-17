#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/29 23:31
# @Author  : 雪成
# @Software: PyCharm
import random
from faker import Faker


def get_user_login(count):
    faker = Faker(locale='zh_CN')
    data_list = []
    for i in range(1, count + 1):
        dic = {}
        username = faker.name()
        password = faker.password(special_chars=False)
        gender = random.randint(0, 1)
        mobile = faker.phone_num()
        email = faker.email()
        address = faker.address()
        id_card = faker.ssn()
        dic['username'] = username
        dic['password'] = password
        dic['gender'] = gender
        dic['mobile'] = mobile
        dic['email'] = email
        dic['address'] = address
        dic['id_card'] = id_card
        data_list.append(dic)
    return data_list
