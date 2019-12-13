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
    def __init__(self, request=None, auth_key=None, csrf_key=None, headers=None, endpoint=None, request_timeout=5):
        if request:
            self.headers = request.headers
        elif headers:
            self.headers = headers
        else:
            self.headers = {"Cookie": f"auth_key={auth_key}; csrf_key={csrf_key}", "X-Xsrftoken": csrf_key}

        self.endpoint = endpoint
        self.request_timeout = request_timeout

    ###设置返回为json
    def do_action(self, **kwargs):
        kwargs = self.with_params_data_url(**kwargs)
        response = requests.request(kwargs.get('method'), kwargs.get('url'), headers=self.headers,
                                    data=kwargs.get('body'), timeout=self.request_timeout)

        return response.text

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
        self.headers['sdk_method'] = 'yes'

        return kwargs

    @property
    def help(self):
        help_info = """ """
        return help_info


if __name__ == '__main__':
    pass
