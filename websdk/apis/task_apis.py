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
                       url=f'{job_prefix}/v2/flow/accept/create/',
                       body={
                           "order_name": "标题",
                           "creator": "发起人",
                           "flow_version_name": "依赖的流程名称",
                           "start_node": "选择的开始节点",
                           "start_time": "2018-11-27 14:09:50",
                           "global_params": "{}",  ##参数，必须为json格式且可以格式化为字典
                           "global_node": "{}",  ### 初始的执行节点
                           "details": "这里是备注",
                           "classify": "",  ### 类型
                           "hosts": "{1: '127.0.0.1'}"
                       },
                       field_help={
                           "order_name": "标题",
                           "creator": "提交人",
                           "flow_version_name": "依赖的流程名称",
                           "start_node": "如果有多个开始节点，必须指定一个",
                           "start_time": "在开始节点上设置时间，到这个时间会进行执行",
                           "global_node": "初始的执行节点",
                           "global_params": "这里是一个字典，里面的参数可以自行定义，如上，你模板参数里面用到了哪些你都可以在这里定义出来，当你的POST到这个接口时候，我们会自动接受此参数，并帮你运行脚本 解析你要传入的参数。",
                           "details": "描述，备注信息",
                       },
                       description='基于此接口可以创建作业任务')
