#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/2 23:26
# @Author  : 雪成
# @Software: PyCharm
import yaml


def parse_data(filename, key):
    """
    解析数据:读取 yml文件的数据
    :param filename: user_login.yml
    :param key: test_login
    :return: 列表嵌套字典
    """

    with open('../data/%s.yml' % filename, mode='r', encoding='utf-8') as f:
        yaml_login_data = yaml.load(f, Loader=yaml.FullLoader)
        temp = list()
        pre_value = yaml_login_data.get(key)
        for i in pre_value.values():
            temp.append(i)
        return temp


if __name__ == '__main__':
    data_list = parse_data('user', 'test_login')
    print(data_list)
