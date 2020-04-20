#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2019/12/12 17:56
Desc    : 解释一下吧
"""

import json
from websdk.tools import singleton
from .apis import AdminAPIS, TaskAPIS, KerriganAPIS


@singleton
class ConstAPIS(AdminAPIS, TaskAPIS, KerriganAPIS):
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
