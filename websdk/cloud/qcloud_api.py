#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""
Contact : 191715030@qq.com
Author : shenshuo
Date   : 2019年2月5日13:37:54
Desc   : 云厂商的一些方法
"""

import hmac
import hashlib
import base64
from urllib import parse


class QCloudApiOpt:

    @staticmethod
    def sort_dic(keydict):
        return sorted(zip(keydict.keys(), keydict.values()))

    @staticmethod
    def get_str_sign(sortlist, api_url):
        sign_str_init = ''
        for value in sortlist:
            sign_str_init += value[0] + '=' + value[1] + '&'
        sign_str = 'GET' + api_url + sign_str_init[:-1]
        return sign_str, sign_str_init

    @staticmethod
    def get_signature(sign_str, secret_key):
        secretkey = secret_key
        signature = bytes(sign_str, encoding='utf-8')
        secretkey = bytes(secretkey, encoding='utf-8')
        my_sign = hmac.new(secretkey, signature, hashlib.sha1).digest()
        return base64.b64encode(my_sign)

    @staticmethod
    def encode_signature(my_sign):
        return parse.quote(my_sign)

    @staticmethod
    def get_result_url(sign_str, result_sign, api_url):
        return 'https://' + api_url + sign_str + 'Signature=' + result_sign

    @staticmethod
    def run(keydict, api_url, secret_key):
        sortlist = QCloudApiOpt.sort_dic(keydict)
        # 获取拼接后的sign字符串
        sign_str, sign_str_int = QCloudApiOpt.get_str_sign(sortlist, api_url)
        # 获取签名
        my_sign = QCloudApiOpt.get_signature(sign_str, secret_key)
        # 对签名串进行编码
        result_sign = QCloudApiOpt.encode_signature(my_sign)
        # 获取最终请求url
        result_url = QCloudApiOpt.get_result_url(sign_str_int, result_sign, api_url)
        return result_url
