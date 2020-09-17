#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/29 23:25
# @Author  : 雪成
# @Software: PyCharm
from faker import Faker

fake = Faker(locale='zh_CN')
print('地址类'.center(20, "‐"))

print(fake.address())
print(fake.name())

print(fake.user_name(), fake.password(special_chars=False))
