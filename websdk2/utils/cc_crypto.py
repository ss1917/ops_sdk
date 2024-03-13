#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2023/4/17 17:07
Desc    : 加密
"""

import base64
from cryptography.fernet import Fernet
from .consts import const
from .configs import configs


class AESCryptoV3:
    """
    usage:  mc = AESCryptoV3()                  实例化
            mc.my_encrypt('ceshi')          对字符串ceshi进行加密
            mc.my_decrypt('')               对密文进行解密
    """

    def __init__(self, key: str = 'W1zFCF-pnUXi1zRtfgNkHmM3qv_3zvCkVSx68vXqks4='):
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度
        if not isinstance(key, bytes): key = key.encode('utf-8')
        if len(key) > 32:
            key = key[0:32]
        else:
            key = key.rjust(32, b'0')

        self.key = base64.urlsafe_b64encode(key)
        self.f = Fernet(self.key)

    @property
    def create_key(self):
        return Fernet.generate_key()

    def my_encrypt(self, text: str):
        if isinstance(text, str): text = text.encode('utf-8')
        return self.f.encrypt(text).decode('utf-8')

    def my_decrypt(self, text: str):
        if isinstance(text, str): text = text.encode('utf-8')
        return self.f.decrypt(text).decode('utf-8')


class AESCryptoV4:
    """
    usage:  mc = AESCryptoV4()                  实例化
            mc.my_encrypt('ceshi')          对字符串ceshi进行加密
            mc.my_decrypt('')               对密文进行解密
    """

    def __init__(self, key: str = None):
        # 如果没有提供密钥，则使用默认密钥
        if key is None:
            # 若没有提供密钥，则生成一个新密钥
            key = configs.get(const.AES_CRYPTO_KEY, 'W1zFCF-pnUXi1zRtfgNkHmM3qv_3zvCkVSx68vXqks4=')

        # 确保密钥是字节类型
        if not isinstance(key, bytes):
            key = key.encode('utf-8')

        if len(key) > 32:
            key = key[0:32]
        else:
            key = key.rjust(32, b'0')
        # 创建Fernet对象
        self.f = Fernet(base64.urlsafe_b64encode(key))

    @property
    def create_key(self):
        return Fernet.generate_key()

    def my_encrypt(self, text: str):
        if isinstance(text, str): text = text.encode('utf-8')
        return self.f.encrypt(text).decode('utf-8')

    def my_decrypt(self, text: str):
        if isinstance(text, str): text = text.encode('utf-8')
        return self.f.decrypt(text).decode('utf-8')


mcv4 = AESCryptoV4()
