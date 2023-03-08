#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class KerriganAPIS:
    kerrigan_prefix = "/api/kerrigan"
    get_publish_config = dict(method='GET',
                              url=f'{kerrigan_prefix}/v1/conf/publish/config/',
                              params={'project_code': '',
                                      'environment': '',
                                      'service': 'service',
                                      'filename': 'filename'},
                              field_help={},
                              description='获取配置'
                              )
