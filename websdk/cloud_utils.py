#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
Contact : 191715030@qq.com
Author : shenshuo
Date   : 2019年2月5日13:37:54
Desc   : 云厂商的一些方法
"""
from .cloud.qcloud_api import QCloudApiOpt
from .cloud.ucloud_api import UCloudApi


def cloud_factory(cloud):
    if cloud == 'aliyun':
        return None

    elif cloud == 'qcloud':
        return QCloudApiOpt()

    elif cloud == 'ucloud':
        return UCloudApi()

    elif cloud == 'aws':
        return None
    else:
        return None
