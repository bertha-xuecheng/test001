#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/30 21:22
# @Author  : 雪成
# @Software: PyCharm
from nb_log import LogManager


class GetLog:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = LogManager('simple').get_logger_and_add_handlers(log_path='../logger',
                                                                          log_filename='test.log',
                                                                          formatter_template=5,
                                                                          log_file_size=10)

            return cls.logger


if __name__ == '__main__':
    log = GetLog().get_logger()
    log.info('开始初始化日志')
    print("==================================")
    log.error('初始化日志失败')
