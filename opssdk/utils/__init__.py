#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author : shenshuo
date   : 2018-3-7
role   : 工具类
'''

import time
from opssdk.logs import Log

log_path = '/log/yunwei/yunwei.log'
log_ins = Log('utils', log_path)

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        log_ins.write_log("info", '%s execute duration :%.3f second' % (str(func), duration))
        return result

    return wrapper