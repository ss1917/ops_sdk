#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""
import json
from ..tools import singleton


@singleton
class ConstAPIS:
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError("Can't rebind const (%s)" % name)

        if not isinstance(value, dict):
            raise TypeError("Value must be in dict format")

        if not value.get('url'):
            raise TypeError("Value must have url")

        if not value.get('description'):
            raise TypeError("Value must have description")

        if value.get('body'):
            if not isinstance(value.get('body'), dict):
                json.loads(value)

        self.__dict__[name] = value


api_set = ConstAPIS()
api_set.get_users = dict(method='GET',
                         url='/mg/v2/accounts/user/',
                         params={
                             'page': 1,
                             'limit': 201,
                             'key': None,
                             'value': None
                         },
                         field_help={},
                         description='获取用户信息')

api_set.opt_users = dict(method='POST',
                         url='/mg/v2/accounts/user/',
                         body={
                             'username': None,
                             'nickname': None,
                             'password': None,
                             'department': None,
                             'tel': None,
                             'wechat': None,
                             'no': None,
                             'email': None,
                             'user_state': '20',
                         },
                         field_help={},
                         description='操作用户数据，支持增删改，请修改method和body数据')
