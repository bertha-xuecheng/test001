#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/6 13:40
# @Author  : 雪成
# @Software: PyCharm
d = {'k': 'v'}
print(d, id(d))

d['k'] = 'vvvvvv'
print(d, id(d))
