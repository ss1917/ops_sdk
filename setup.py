#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
author : shenshuo
date   : 2018年2月5日13:37:54
desc   : SDK
"""
from distutils.core import setup

setup(
    name='opssdk',
    version='0.0.11',
    packages=['opssdk', 'opssdk.logs', 'opssdk.operate', 'opssdk.install', 'opssdk.get_info', 'opssdk.utils', 'websdk'],
    url='https://github.com/ss1917/ops_sdk/',
    license='',
    install_requires=['fire', 'shortuuid', 'pymysql===0.9.3', 'sqlalchemy===1.2.15', 'python3-pika===0.9.14', 'PyJWT',
                      'Crypto===1.4.1', 'requests', 'redis===2.10.6', 'tornado===5.0',
                      'aliyun-python-sdk-core-v3===2.8.6', 'aliyun-python-sdk-dysmsapi','python-dateutil===2.7.5'],
    author='shenshuo',
    author_email='191715030@qq.com',
    description='SDK of the operation and maintenance script'
                'logs'
                'operate'
)
