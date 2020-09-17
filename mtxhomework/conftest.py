#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 2:29
# @Author  : 雪成
# @Software: PyCharm
"""
    1.conftest.py 固定的名字
    2.钩子函数: (hook)
    3.pytest_collection_modifyitems(items) 这个函数的运行机制为
    4.作用: 测试用例之前
    5.items ： 测试用例
"""


def pytest_collection_modifyitems(items):
    for items in items:
        items.name = items.name.encode().decode('unicode_escape')
        items._nodeid = items.nodeid.encode().decode('unicode_escape')
