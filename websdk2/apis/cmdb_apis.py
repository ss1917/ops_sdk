#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录 CMDB API
"""


class CMDBAPIS:
    cmdb_prefix = "/api/cmdb"

    get_tag_list = dict(
        method='GET',
        url=f'{cmdb_prefix}/api/v2/cmdb/tag/list/',
        params={
            'page_number': '1',  # 分页/第几页
            'page_size': '200',  # 分页/每页多少个
            "tag_key": None
        },
        description='CMDB 获取标签key、value列表'
    )

    get_service_tree = dict(method='GET',
                            url=f'{cmdb_prefix}/api/v2/cmdb/tree/',
                            params={"biz_id": "0"},
                            description='获取当前业务服务树')

    get_dynamic_groups = dict(method='GET',
                              url=f'{cmdb_prefix}/api/v2/cmdb/biz/dynamic_group/list/',
                              params={
                                  "biz_id": ""
                              },
                              description='获取当前业务下动态分组')

    get_dynamic_group_details = dict(method='GET',
                                     url=f'{cmdb_prefix}/api/v2/cmdb/biz/dynamic_group/preview/',
                                     params={
                                     },
                                     description='获取动态分组详细数据')

    get_tree_asset_server = dict(method='GET',
                                 url=f'{cmdb_prefix}/api/v2/cmdb/tree/asset/server',
                                 params={
                                 },
                                 description='根据业务获取资源信息')
