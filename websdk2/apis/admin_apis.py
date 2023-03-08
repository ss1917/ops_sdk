#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class AdminAPIS:
    route_prefix = "/api/mg"
    get_users = dict(method='GET',
                     url=f'{route_prefix}/v3/accounts/user/',
                     params={
                         'page': 1,
                         'limit': 201
                     },
                     field_help={},
                     description='获取用户信息')

    opt_users = dict(method='POST',
                     url=f'{route_prefix}/v3/accounts/user/',
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
                     field_help={
                         'user_state': '20',
                     },
                     description='操作用户数据，支持增删改，请修改method和body数据')

    get_resource_info_by_user = dict(method='GET',
                                     url='/mg/v2/overall/resource/user/',
                                     params={
                                         'nickname': None,  ## 默认为当前用户有权限的
                                         'expand': None  ## yes 是扩展为目录的 ， no 是可以当全局标签的
                                     },
                                     field_help={
                                         'nickname': None,  ## 默认为当前用户有权限的
                                         'expand': None  ## yes 是扩展为目录的 ， no 是可以当全局标签的，没有则是全部
                                     },
                                     description='获取用户有权限的资源组/目录')

    get_resource_info = dict(method='GET',
                             url='/mg/v2/overall/resource/',
                             params={
                                 'key': None,  ## 筛选字段
                                 'value': None  ## 筛选字段值
                             },
                             field_help={
                                 'key': None,  ## 筛选字段
                                 'value': None  ## 筛选字段值
                             },
                             description='获取资源组/目录')

    get_role_list = dict(method='GET',
                         url=f'{route_prefix}/v3/accounts/role/',
                         params={
                         },
                         field_help={
                             'page': '分页/第几页',  ### 分页/第几页
                             'limit': '分页/每页多少个',  ### 分页/每页多少个
                             'value': '模糊查询'  ### 模糊查询
                         },
                         description='获取角色信息')

    get_all_role_user = dict(method='GET',
                             url=f'{route_prefix}/v3/accounts/all_role_user/',
                             params={
                             },
                             field_help={
                                 'page': '分页/第几页',  ### 分页/第几页
                                 'limit': '分页/每页多少个',  ### 分页/每页多少个
                                 'value': '模糊查询'  ### 模糊查询
                             },
                             description='获取用户组和用户组内用户信息')

    get_send_addr = dict(method='GET',
                         url=f'{route_prefix}/v1/notifications/send_addr/',
                         params={
                         },
                         field_help={
                             'users_str': '用户  半角逗号分隔',  ### 用户  半角逗号分隔
                             'notice_group_str': '通知组  半角逗号分隔',  ### 通知组  半角逗号分隔
                             'roles_str': '角色   半角逗号分隔'  ### 角色   半角逗号分隔
                         },
                         description='获取用户的联系方式，手机/邮箱/钉钉ID')

    get_notice_group = dict(method='GET',
                            url=f'{route_prefix}/v3/notifications/group/',
                            params={
                                'page': 1,
                                'limit': 201,
                                'value': ''
                            },
                            field_help={
                                'page': '分页/第几页',  ### 分页/第几页
                                'limit': '分页/每页多少个',  ### 分页/每页多少个
                                'value': '模糊查询'  ### 模糊查询
                            },
                            description='获取通知组')

    opt_notice_group = dict(method='POST',
                            url=f'{route_prefix}/v3/notifications/group/',
                            body={
                            },
                            field_help={
                            },
                            description='操作通知组')

    send_notice = dict(method='POST',
                       url=f'{route_prefix}/v3/notifications/factory/',
                       body={
                           "name": 'default',
                           "msg": {"msg": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级"}
                       },
                       field_help={
                           "name": '模板名称',
                           "msg": "发送的消息变量字典",
                           "notice_conf": "随着通知一起传入的配置信息，会覆盖模板里面的配置信息"
                       },
                       description='根据通知模板发送通知')

    send_update_notice = dict(method='PUT',
                              url=f'{route_prefix}/v3/notifications/factory/',
                              body={
                                  "agent_id": 27689,
                                  "status_value": "已同意",
                                  "status_bg": "0xFF78C06E",
                                  "task_id": 37491848
                              },
                              field_help={
                                  "agent_id": '申请的应用id',
                                  "status_value": "状态值",
                                  "status_bg": "颜色",
                                  "task_id": "已经发送消息ID，发送通知的时候可以获取他的返回"
                              },
                              description='变更已发出通知消息的状态， 目前只有钉钉工作通知OA方式可用')

    send_custom_notice = dict(method='POST',
                              url=f'{route_prefix}/v1/notifications/custom/',
                              body={
                                  "send_addr": '',
                                  "userid_list": '',
                                  "msg": {"msg": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级"}
                              },
                              field_help={
                                  "send_addr": '需要的通知的用户信息',
                                  "userid_list": "",
                                  "msg": "发送的消息变量字典",
                              },
                              description='自定义的通知信息')
