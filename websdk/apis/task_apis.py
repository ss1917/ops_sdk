#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class TaskAPIS:
    create_jobs= dict(method='POST',
                     url='/task/v2/task/accept/',
                     body={
                         "task_name": "任务名称",
                         "submitter": "提交人",
                         "temp_id": "200",
                         "schedule": "ready",
                         "exec_time": "2018-11-27 14:09:50",
                         "associated_user": "{'group-1': ['奥特曼']}",
                         "args": "{'VERSION':'eeee', 'arg02': 'xxxx'}",
                         "details": "这里是备注",
                         "hosts": "{1: '127.0.0.1'}"
                     },
                     field_help={
                         "task_name": "任务名称",
                         "submitter": "提交人",
                         "temp_id": "模板ID，就是你创建模板时候生成的那个ID",
                         "schedule": "这是状态，常用的有ready和new ready：表示不通过人工审核，只要到了执行时间直接执行任务\
                         new：表示需要任何审核，管理员审核，选择执行时间，到时间后开始执行",
                         "exec_time": "任务执行时间，状态为ready的情况下，到这个时间会进行执行",
                         "associated_user": "{'group-1': ['奥特曼']}",
                         "args": "这里是一个字典，里面的参数可以自行定义，如上，你模板参数里面用到了哪些你都可以在这里定义出来，当你的POST到这个接口时候，我们会自动接受此参数，并帮你运行脚本 解析你要传入的参数。",
                         "details": "描述，备注信息",
                         "hosts": "这个是执行主机，字典形式， 1表示第一组主机，也就是上面模板里面的组1，"
                                  "任务支持多组。主机IP，这个是执行主机，这个废话多一点，比如我以上模板的脚本在172.16.0.101这台主机上，"
                                  "我就想平台登陆我这个主机，来帮我执行这些脚本，至于怎么登陆，那么就是我最开始在平台里面配置了一个执行用户，"
                                  "我将我这个主机的私钥放到了平台上，公钥在我服务器上，这样子就可以ssh -i xxxx.pem@{ip_address}\
                                  远程到我的主机上帮我执行命令。"
                     },
                     description='基于此接口可以创建作业任务')
