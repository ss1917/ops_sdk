#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
author : shenshuo
date   : 2023年3月8日
desc   : CODO SDK
"""

import sys
from distutils.core import setup

VERSION = '0.1.73'

if sys.version_info < (2, 7) or (3, 0) <= sys.version_info < (3, 6):
    print('This program requires at least Python 2.7 or 3.6 to run.')
    sys.exit(1)


def get_data_files():
    data_files = [
        ('share/doc/ops_sdk', ['README.md'])
    ]
    return data_files


def get_install_requires():
    requires = ['fire==0.5.0', 'shortuuid==1.0.11', 'pymysql==0.9.3', 'sqlalchemy==1.3.23', 'pika==1.3.1',
                'PyJWT==2.0.1', 'requests==2.28.2', 'redis==4.5.1', 'tornado>=6.0', 'loguru>=0.6.0',
                'cryptography==42.0.4', 'ldap3==2.9', 'pydantic>=1.10.5']
    return requires


classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
]

setup(
    name='opssdk',
    version=VERSION,
    description="CODO项目的Python SDK",
    packages=['opssdk', 'opssdk.utils', 'websdk2', 'websdk2.apis', 'websdk2.cloud', 'websdk2.utils'],
    url='https://github.com/ss1917/ops_sdk/',
    license='GPLv3',
    keywords="ops,opencodo,devops",
    install_requires=get_install_requires(),
    author='shenshuo',
    author_email='191715030@qq.com',
    long_description='SDK of the operation and maintenance script logs operate',
    long_description_content_type='text/markdown',
    include_package_data=True,
    data_files=get_data_files(),
    python_requires=">=3.6",
    classifiers=classifiers,
    platforms='any'
)
