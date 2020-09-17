#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 0:51
# @Author  : 雪成
# @Software: PyCharm
import pytest


# 跳过测试函数
@pytest.mark.run(order=3)
@pytest.mark.skipif(condition=True, reason='a与b不相等跳过测试用例')
def test_case_01():
    a = 10
    b = 20
    assert a == b
    print('test_case_01')

@pytest.mark.run(order=2)
def test_case_02():
    a = 10
    b = 20
    assert a != b
    print('test_case_02')

# 预期失败
@pytest.mark.xfail(condition=True, reason='a不在b里面')
def test_case_03():
    a = 10
    b = 20
    assert a in b
    print('test_case_03')


@pytest.mark.xfail(condition=True, reason='a不在b里面')
def test_case_04():
    a = 10
    b = 20
    assert a != b
    print('test_case_04')

@pytest.mark.run(order=1)
def test_case_05():
    a = 10
    b = 20
    assert a != b
    print('test_case_05')
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_mtx_basics.py'])
