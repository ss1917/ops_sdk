#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class CMDBAPIS:
    cmdb_prefix = "/api/cmdb"
    create_jobs = dict(method='GET',
                       url=f'{cmdb_prefix}/api/v2/cmdb/tag/list/',
                       params={
                           'page_number': '1',  ### 分页/第几页
                           'page_size': '200',  ### 分页/每页多少个
                           "tag_key": None
                       },
                       field_help={
                       },
                       description='CMDB 获取标签key、value列表')
