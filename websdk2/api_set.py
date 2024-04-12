#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2019/12/12 17:56
Desc    : API集合
"""

import json
from .apis import AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS


class ConstAPIS(AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError("Can't rebind const (%s)" % name)

        if not isinstance(value, dict):
            raise TypeError("Value must be in dict format")

        if not value.get('url'):
            raise TypeError("Value must have url")

        if not value.get('description'):
            raise TypeError("Value must have description")

        if value.get('body') and not isinstance(value.get('body'), dict):
            raise TypeError("Body value must be a dict")

        super().__setattr__(name, value)


api_set = ConstAPIS()
