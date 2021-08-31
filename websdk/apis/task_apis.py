#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class TaskAPIS:
    job_prefix = "/api/job"
    create_jobs = dict(method='POST',
                       url=f'{job_prefix}/v1/flow/accept/create/',
                       body={
                           "order_name": "标题",
                           "creator": "发起人",
                           "flow_version_name": "依赖的流程名称",
                           "start_time": "2018-11-27 14:09:50",
                           "global_params": "{}",  ##参数，必须为json格式且可以格式化为字典
                           "details": "这里是备注"
                       },
                       field_help={
                           "order_name": "标题",
                           "creator": "提交人",
                           "flow_version_name": "依赖的流程名称",
                           "start_node": "如果有多个开始节点，必须指定一个",
                           "start_time": "在开始节点上设置时间，到这个时间会进行执行",
                           "global_params": "这里是一个字典，里面的参数可以自行定义，如上，你模板参数里面用到了哪些你都可以在这里定义出来，当你的POST到这个接口时候，我们会自动接受此参数，并帮你运行脚本 解析你要传入的参数。",
                           "details": "描述，备注信息",
                       },
                       description='基于此接口可以创建作业任务')

    ##(r"/v1/proxy/cmdbv3/dynamic_group/info/"
    get_proxy_dynamic_group_list = dict(
        method='GET',
        url=f'{job_prefix}/v1/proxy/cmdbv3/dynamic_group/list/',
        params={
            "biz_id": None,  ###  业务/资源id
            'page_number': '1',  ### 分页/第几页
            'page_size': '200',  ### 分页/每页多少个
        },
        field_help={
        },
        description='COCO动态分组'
    )

    ##CC动态分组 获取动态分组详细数据"
    get_proxy_dynamic_group_info = dict(
        method='GET',
        url=f'{job_prefix}/v1/proxy/cmdbv3/dynamic_group/info/',
        params={
            "exec_uuid": None,  ###  使用动态分组的UUID查询
            'exec_uuid_list': '[]',  ### 批量查询
        },
        field_help={
        },
        description='CC动态分组 获取动态分组详细数据'
    )
