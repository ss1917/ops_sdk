#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class AdminV4APIS:
    route_prefix = "/api/p"
    get_user_list = dict(method='GET',
                         url=f'{route_prefix}/v4/user/list/',
                         params={
                             'page': 1,
                             'limit': 201
                         },
                         field_help={},
                         description='查看用户列表')

    get_users = dict(method='GET',
                     url=f'{route_prefix}/v4/user/',
                     params={
                         'page': 1,
                         'limit': 201
                     },
                     field_help={},
                     description='管理-查看用户列表')

    opt_users = dict(method='POST',
                     url=f'{route_prefix}/v4/user/',
                     body={
                         'username': None,
                         'nickname': None,
                         'password': None,
                         'department': None,
                         'tel': None,
                         'email': None,
                         'user_state': '20',
                     },
                     field_help={
                         'user_state': '20',
                     },
                     description='操作用户数据，支持增删改，请修改method和body数据')

    get_normal_role_list = dict(method='GET',
                                url=f'{route_prefix}/v4/role/list/',
                                params={},
                                field_help={
                                    'page': '分页/第几页',  ### 分页/第几页
                                    'limit': '分页/每页多少个',  ### 分页/每页多少个
                                    'searchVal': '模糊查询'  ### 模糊查询
                                },
                                description='查看常规角色列表')

    get_all_base_role_list = dict(method='GET',
                                  url=f'{route_prefix}/v4/role/base_list/',
                                  params={},
                                  field_help={
                                  },
                                  description='查看所有基础角色')

    get_all_role_user_v4 = dict(method='GET',
                                url=f'{route_prefix}/v4/all_role_user/',
                                params={
                                },
                                field_help={
                                },
                                description='获取所有角色和角色内内用户信息')
