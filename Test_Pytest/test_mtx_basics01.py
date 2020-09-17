#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 1:15
# @Author  : 雪成
# @Software: PyCharm
import pytest

"""
 装饰器函数：fixture
  类外面
     1.setup_function()  在每个测试函数（不在类里面的测试用例）之前执行初始化操作
     2.setup_module() 模块之前(python文件之前)
     3.teardown_module() 模块之后(python文件之后)
     4.teardown_function() 在每个测试函数（不在类里面的测试用例）之前执行销毁操作
  类里面
     1.setup_method()  在每个实例化方法之前执行初始化操作
     2.setup_class() 在每个类之前执行的初始化操作
     3.teardown_class() 在每个类之后执行的初始化操作


"""


def setup_module():
    print("模块之前(python文件之前)")


def teardown_module():
    print("模块之后(python文件之后)")


def setup_function():
    print("在每个测试函数（不在类里面的测试用例）之前执行初始化操作")


def teardown_function():
    print("在每个测试函数（不在类里面的测试用例）之前执行销毁操作")


def test_case_1():
    print('test_case_1')

def test_case_4():
    print('test_case_4')

class TestKon:
    def setup_module(self):
        print("实例化方法之前")

    def teardown_module(self):
        print("实例化方法之后")

    def setup_class(self):
        print("类之前执行的初始化操作")

    def teardown_class(self):
        print('类之后执行的初始化操作')

    def test_case_02(self):
        print("test_case_02")

    def test_case_03(self):
        print("test_case_03")
