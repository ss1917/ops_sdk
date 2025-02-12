#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2025年2月12日13:37:54
Desc    ：记录API
"""


class NoticeAPIS:
    route_prefix = "/api/noc"
    send_router_alert = dict(method='POST',
                             url=f'{route_prefix}/v1/router-alert',
                             params={
                             },
                             body={
                             },
                             field_help={},
                             description='通过告警路由发送告警')
