#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
Contact : 191715030@qq.com
Author : shenshuo
Date   : 2018年2月5日13:37:54
Desc   : 处理API请求
"""

import json
import requests
from urllib.parse import urlencode
import logging
from tornado.httpclient import AsyncHTTPClient

logger = logging.getLogger(__name__)


class AcsClient:
    def __init__(self, request=None, auth_key=None, headers=None, endpoint='http://gw.opendevops.cn',
                 request_timeout=5):
        if request:
            self.headers = request.headers
        elif headers:
            self.headers = headers
        else:
            self.headers = {"Cookie": 'auth_key={}'.format(auth_key)}

        self.endpoint = endpoint
        self.headers['Sdk-Method'] = 'zQtY4sw7sqYspVLrqV'
        self.request_timeout = request_timeout

    ###设置返回为json
    def do_action(self, **kwargs):
        kwargs = self.with_params_data_url(**kwargs)
        response = requests.request(kwargs.get('method'), kwargs.get('url'), headers=self.headers,
                                    data=kwargs.get('body'), timeout=self.request_timeout)

        return response.text

    ### 返回完整信息
    def do_action_v2(self, **kwargs):
        kwargs = self.with_params_data_url(**kwargs)
        response = requests.request(kwargs.get('method'), kwargs.get('url'), headers=self.headers,
                                    data=kwargs.get('body'), timeout=self.request_timeout)
        return response

    async def do_action_with_async(self, **kwargs):

        body = await self._implementation_of_do_action(**kwargs)
        return body

    async def _implementation_of_do_action(self, **kwargs):
        http_client = AsyncHTTPClient()
        request = self.with_params_data_url(**kwargs)

        response = await http_client.fetch(request.get('url'), method=request.get('method'), raise_error=False,
                                           body=request.get('body'), headers=self.headers,
                                           request_timeout=self.request_timeout)

        return response.body

    def with_params_data_url(self, **kwargs):
        ### 重新组装URL
        url = "{}{}".format(self.endpoint, kwargs['url'])
        kwargs['url'] = url

        if not kwargs['method']: kwargs['method'] = 'GET'

        body = kwargs.get('body', {})

        if kwargs['method'] in ['POST', 'post', 'PATCH', 'patch', 'PUT', 'put']:
            if not body:
                raise TypeError('method {},  body can not be empty'.format(kwargs['method']))
            else:
                if not isinstance(body, dict):  json.loads(body)

        if body and isinstance(body, dict): kwargs['body'] = json.dumps(body)

        params = kwargs.get('params')
        if params: kwargs['url'] = "{}?{}".format(url, urlencode(params))

        if not self.headers: self.headers = kwargs.get('headers', {})

        if kwargs['method'] not in ['GET', 'get']: self.headers['Content-Type'] = 'application/json'

        return kwargs

    @staticmethod
    def help():
        help_info = """
        headers = {"Cookie": 'auth_key={}'.format(auth_key)}
        ### 三种实例化方式
        1. client = AcsClient(endpoint=endpoint, headers=headers)
        2. client = AcsClient(endpoint=endpoint, request=self.request)
        3. client = AcsClient(endpoint=endpoint, auth_key=auth_key)
        
        调用： 传入api 的参数，可以参考下面示例
        
        同步
        response = client.do_action(**api_set.get_users) 
        print(json.loads(response))
        
        异步
        # import asyncio
        # loop = asyncio.get_event_loop()
        # ### 使用gather或者wait可以同时注册多个任务，实现并发
        # # task1 = asyncio.ensure_future(coroutine1)
        # # task2 = asyncio.ensure_future(coroutine2)
        # # tasks = asyncio.gather(*[task1, task2])
        # # loop.run_until_complete(tasks)
        # ### 单个使用
        # response = loop.run_until_complete(client.do_action_with_async(**api_set.get_users))
        # response = json.loads(response)
        # print(response)
        # loop.close()
        
        tornado 项目内必须使用异步，不过可以直接使用
        #client.do_action_with_async(**api_set.get_users)
        # response = json.loads(response)
        # print(response)
        
         """
        return help_info


if __name__ == '__main__':
    pass
