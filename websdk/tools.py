#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : ss
date   : 2018年4月12日
role   : 工具类
"""

import sys
import re
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


def bytes_to_unicode(input_bytes):
    if sys.version_info.major >= 3:
        return str(input_bytes, encoding='utf-8')
    else:
        return (input_bytes).decode('utf-8')


def convert(data):
    if isinstance(data, bytes):  return data.decode('utf8')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data


def check_password(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 8 else False


def is_mail(text, login_mail=None):
    if login_mail:
        if re.match(r'[0-9a-zA-Z_]{0,19}@%s' % login_mail, text):
            return True
        else:
            return False
    p = re.compile(r"[^@]+@[^@]+\.[^@]+")
    # if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', text):
    if p.match(text):
        return True
    else:
        return False


def is_tel(tel):
    ### 检查是否是手机号
    ret = re.match(r"^1[35678]\d{9}$", tel)
    if ret:
        return True
    else:
        return False

def check_contain_chinese(check_str):
    ### 检查是否包含汉字
    """
    :param check_str:
    :return:
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


class Executor(ThreadPoolExecutor):
    """ 线程执行类 """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


def exec_shell(cmd):
    '''执行shell命令函数'''
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub.communicate()
    ret = sub.returncode
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')


class RunningProcess:
    def __init__(self, process):
        self.process = process
        self.start_time = time.time()

    def is_running(self):
        return bool(self.process.poll() is None)

    def read_line(self):
        return self.process.stdout.readline()

    @property
    def unread_lines(self):
        lines = self.process.stdout.readlines()
        self.process.stdout.close()
        return lines

    @property
    def run_state(self):
        return bool(self.process.poll() is 0)

    def is_timeout(self, exec_time=600):
        duration = time.time() - self.start_time
        if duration > exec_time:
            self.process.terminate()
            self.process.wait()
            self.process.communicate()
            # print("execute timeout, execute time {}, it's killed.".format(duration))
            return True
        return False