#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2024年4月12日
Desc    ：Agent常用API
"""


class AgentAPIS:
    route_prefix = "/api/agent"
    agent_list_url = f'{route_prefix}/v1/agent/info'
    get_agent_work_url = f'{route_prefix}/v1/manager/agent/get_running_task'
    batch_add_task_url = f'{route_prefix}/v1/agent/task/batch'
    sync_files_url = f'{route_prefix}/v1/manager/agent/share_file/register'
    cloud_native_url = f'{route_prefix}/v1/manager/agent/task/cloud_native'

    sync_files_register_url_v2 = f"{route_prefix}/v1/manager/agent/share_filev2/register"
    sync_files_cancel_url_v2 = f"{route_prefix}/v1/manager/agent/share_filev2/cancel"

    get_agent_list = dict(method='GET',
                          url=agent_list_url,
                          params={},
                          field_help={},
                          description='查看Agent列表')

    get_agent_work = dict(method='GET',
                          url=get_agent_work_url,
                          params={},
                          field_help={},
                          description='查询agent状态')

    batch_add_task = dict(method='POST',
                          url=batch_add_task_url,
                          body={
                          },
                          field_help={
                          },
                          description='批量脚本任务下发')

    sync_files_task = dict(method='POST',
                           url=sync_files_url,
                           body={
                           },
                           field_help={
                           },
                           description='批量分发文件下发')

    sync_files_register_v2 = dict(method='POST',
                                  url=sync_files_register_url_v2,
                                  body={
                                  },
                                  field_help={
                                  },
                                  description='批量分发文件下发V2')

    sync_files_cancel_v2 = dict(method='POST',
                                url=sync_files_cancel_url_v2,
                                body={
                                },
                                field_help={
                                },
                                description='批量分发文件取消V2')

    cloud_native_task = dict(method='POST',
                             url=cloud_native_url,
                             body={
                             },
                             field_help={
                             },
                             description='云原生任务下发/终止/重试')

    get_cloud_native_task = dict(method='GET',
                                 url=cloud_native_url,
                                 params={},
                                 field_help={
                                 },
                                 description='云原生任务查询')
