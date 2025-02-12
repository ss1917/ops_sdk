#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2019/12/12 17:56
Desc    : API集合
"""

from .tools import singleton
from .apis import AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS, NoticeAPIS


@singleton
class ConstAPIS(AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS, NoticeAPIS):
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

        # body_data = value.get('body')
        # if body_data is not None and not isinstance(body_data, (dict, list)):
        #     try:
        #         json.loads(body_data)
        #     except (TypeError, ValueError):
        #         raise TypeError("Body data cannot be loaded as JSON")

        self.__dict__[name] = value


api_set = ConstAPIS()
