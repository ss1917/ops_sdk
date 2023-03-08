#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date   : 2019年2月5日13:37:54
Desc   : 云厂商的一些方法
"""

import requests
import hashlib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y %H:%M:%S')

logger = logging.getLogger("ucloud")
logger.setLevel(logging.WARN)


class UCloudApi:
    """UCloud接口"""

    def __init__(self, access_id, access_key, url='https://api.ucloud.cn/'):
        self.url = url
        self.access_id = access_id
        self.access_key = access_key

    def get_region_list(self):
        params = {
            'Action': 'GetRegion',
            'PublicKey': self.access_id
        }
        params = self.add_signature(params)
        req = requests.get(url=self.url, params=params)
        regions = list(set([r['Region'] for r in req.json()['Regions']]))
        return regions

    def get_project_list(self):
        params = {
            'Action': 'GetProjectList',
            'PublicKey': self.access_id
        }
        params = self.add_signature(params)
        req = requests.get(url=self.url, params=params)
        project = list(set([r['ProjectId'] for r in req.json()['ProjectSet']]))
        return project

    def get_project_info(self):
        params = {
            'Action': 'GetProjectList',
            'PublicKey': self.access_id
        }
        params = self.add_signature(params)
        req = requests.get(url=self.url, params=params)
        project_list =  []
        for i in req.json()['ProjectSet']:
            if isinstance(i, dict):
                project_list.append(i)
        return project_list


    def add_signature(self, params):
        items = params.items()
        params_data = ""
        for key in sorted(items):
            params_data = params_data + str(key[0]) + str(key[1])
        params_data = params_data + self.access_key
        sign = hashlib.sha1()
        sign.update(params_data.encode('utf8'))
        signature = sign.hexdigest()
        params['Signature'] = signature
        return params
