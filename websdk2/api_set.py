#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2025/02/12 17:56
Desc    : API集合
"""

from .tools import singleton
from .apis import AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS, NoticeAPIS


@singleton
class ConstAPIS(AdminAPIS, TaskAPIS, KerriganAPIS, AdminV4APIS, CMDBAPIS, AgentAPIS, NoticeAPIS):
    """
    集合所有常用 API 配置的常量类，继承了各个 API 模块的接口配置。

    提供了对 API 配置项的只读管理，并且对每个新增属性值进行校验。
    """

    def __init__(self):
        pass

    def __setattr__(self, name: str, value: dict) -> None:

        """
        自定义属性设置方法，确保 API 配置项的合法性。

        校验条件：
        1. 不允许重新绑定常量。
        2. 属性值必须是字典格式。
        3. 必须包含 'url' 和 'description' 字段。

        Args:
            name (str): 属性名称
            value (dict): 属性值，必须为字典格式并包含必要字段
        """

        if name in self.__dict__:
            raise TypeError(f"Cannot rebind constant '{name}'.")

        if not isinstance(value, dict):
            raise TypeError(f"Value for '{name}' must be a dictionary.")

        # 确保包含 'url' 和 'description' 字段
        if 'url' not in value:
            raise TypeError(f"Value for '{name}' must contain 'url'.")

        if 'description' not in value:
            raise TypeError(f"Value for '{name}' must contain 'description'.")

        self.__dict__[name] = value


api_set = ConstAPIS()
