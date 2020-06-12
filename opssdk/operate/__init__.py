#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author : shenshuo
date   : 2018年2月5日13:37:54
role   : 运维操作
'''

import os
import sys
import time
import re
import subprocess
import base64
import rsa
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


###执行shell命令函数
def exec_shell(cmd):
    sub2 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub2.communicate()
    ret = sub2.returncode
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')


###脚本排它函数
def exclusiveLock(scriptName):
    pid_file = '/tmp/%s.pid' % scriptName
    lockcount = 0
    while True:
        if os.path.isfile(pid_file):
            ###打开脚本运行进程id文件并读取进程id
            fp_pid = open(pid_file, 'r')
            process_id = fp_pid.readlines()
            fp_pid.close()

            ###判断pid文件取出的是否是数字
            if not process_id:
                break

            if not re.search(r'^\d', process_id[0]):
                break

            ###确认此进程id是否还有进程
            lockcount += 1
            if lockcount > 4:
                print('2 min after this script is still exists')
                sys.exit(111)
            else:
                if os.popen('/bin/ps %s|grep "%s"' % (process_id[0], scriptName)).readlines():
                    print("The script is running...... ,Please wait for a moment!")
                    time.sleep(30)
                else:
                    os.remove(pid_file)
        else:
            break

    ###把进程号写入文件
    wp_pid = open(pid_file, 'w')
    sc_pid = os.getpid()
    wp_pid.write('%s' % sc_pid)
    wp_pid.close()


### 加密解密模块
class MyCrypt:
    """
    usage: mc = MyCrypt()               实例化
        mc.my_encrypt('ceshi')          对字符串ceshi进行加密
        mc.my_decrypt('')               对密文进行解密
    """

    def __init__(self, key='HOrUmuJ4bCVG6EYu2docoRNNYSdDpJJw'):
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度
        self.key = key
        self.mode = AES.MODE_CBC

    def my_encrypt(self, text):
        length = 32
        count = len(text)
        if count < length:
            add = length - count
            text = text + ('\0' * add)

        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add)

        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext).decode('utf-8')

    def my_decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text)).decode('utf-8')
        return plain_text.rstrip('\0')


class MyCryptV2:

    def __init__(self, key='HOrUmuJ4bCVG6EYu2docoRNNYSdDpJJw'):
        """
        Usage:
            #实例化
            mc = MyCrypt()
            #加密方法
            mc.my_encrypt('password')
            #解密方法
            mc.my_decrypt('ZpZjEcsqnySTz6UsXD/+TA==')
        :param key:
        """
        self.key = key

    # str不是16的倍数那就补足为16的倍数
    def add_to_16(self, value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # 返回bytes

    def my_encrypt(self, text):
        """
        加密方法
        :param text: 密码
        :return:
        """
        aes = AES.new(self.add_to_16(self.key), AES.MODE_ECB)
        # 先进行aes加密

        encrypt_aes = aes.encrypt(self.add_to_16(text))
        # 用base64转成字符串形式
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '')  # 执行加密并转码返回bytes
        # print('[INFO]: 你的加密为：{}'.format(encrypted_text))
        return encrypted_text

    def my_decrypt(self, text):
        """
        解密方法
        :param text: 加密后的密文
        :return:
        """
        # 初始化加密器
        aes = AES.new(self.add_to_16(self.key), AES.MODE_ECB)
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        # 执行解密密并转码返回str
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
        # print('[INFO]: 你的解密为：{}'.format(decrypted_text))
        return decrypted_text


class MyCryptV3:
    """
    加密：公钥加密，私钥解密；
    签名：私钥签名，公钥验签。
    用作加密时，密文泄露是无所谓的（相对而言），重要的是用于解密的密钥必须安全，所以用不公开的私钥来解密，用公钥来加密；
    用作签名时，目的是防止别人伪造我的身份发信息，所以用私钥来签名，用公钥来验签。
    """

    @classmethod
    def check_message(cls, message):
        if isinstance(message, str):  # 如果msg为字符串, 则转化为字节类型
            message = message.encode('utf-8')
        elif isinstance(message, bytes):  # 如果msg为字节类型, 则无需处理
            pass
        else:  # 否则抛出异常
            raise TypeError('message必须为字符串或者字节类型!')
        return message

    @classmethod
    def create_new_keys(cls, num=4096):  # 可以加密数据长度 4096/8 - 11
        public_key, private_key = rsa.newkeys(num)

        with open('public.pem', 'w+') as f:
            f.write(public_key.save_pkcs1().decode())
        with open('private.pem', 'w+') as f:
            f.write(private_key.save_pkcs1().decode())
        return public_key, private_key

    @classmethod
    def load_private_key(cls, private_path=None, private_info=None):
        if not private_path and not private_info:  raise ValueError('两个参数不能都为空')

        if private_path:
            with open(private_path, "rb") as private_file:
                p = private_file.read()
                return rsa.PrivateKey.load_pkcs1(p)
        else:
            if isinstance(private_info, str):  # 如果pub_key为字符串, 则转化为字节类型
                private_info = private_info.encode('utf-8')
            elif isinstance(private_info, bytes):  # 如果key为字节类型, 则无需处理
                pass
            else:  # 否则抛出异常
                raise TypeError('私钥必须为None、字符串或者字节类型!')
            return rsa.PrivateKey.load_pkcs1(private_info)

    @classmethod
    def load_public_key(cls, public_path=None, public_info=None):
        if not public_path and not public_info:  raise ValueError('两个参数不能都为空')

        if public_path:
            with open(public_path, "rb") as public_file:
                p = public_file.read()
                return rsa.PublicKey.load_pkcs1(p)
        else:
            if isinstance(public_info, str):  # 如果pub_key为字符串, 则转化为字节类型
                public_info = public_info.encode('utf-8')
            elif isinstance(public_info, bytes):  # 如果key为字节类型, 则无需处理
                pass
            else:  # 否则抛出异常
                raise TypeError('公钥必须为None、字符串或者字节类型!')

            return rsa.PublicKey.load_pkcs1(public_info)

    @classmethod
    def to_sign_with_private_key(cls, message, private_path=None, private_key=None):
        # 私钥签名
        message = cls.check_message(message)
        private_key_obj = cls.load_private_key(private_path, private_key)
        result = rsa.sign(message, private_key_obj, 'SHA-384')
        return result

    @classmethod
    def to_verify_with_public_key(cls, message, signature, public_path=None, public_key=None):
        # 公钥验签
        public_key_obj = cls.load_public_key(public_path, public_key)
        message = cls.check_message(message)
        result = rsa.verify(message, signature, public_key_obj)
        return result

    @classmethod
    def to_decrypt(cls, message, private_path=None, private_key=None, be_base64=True):
        # 非对称解密
        if be_base64: message = base64.b64decode(message)
        message = cls.check_message(message)

        private_key_obj = cls.load_private_key(private_path, private_key)

        return rsa.decrypt(message, private_key_obj).decode()

    @classmethod
    def to_encrypt(cls, message, public_path=None, public_key=None, be_base64=True):
        # 非对称加密
        """
        :param message: 待加密字符串或者字节
        :param public_path: 公钥路径  二选一
        :param public_key: 公钥字符串  二选一
        :return: base64密文字符串
        """

        message = cls.check_message(message)
        public_key_obj = cls.load_public_key(public_path, public_key)

        cryto_msg = rsa.encrypt(message, public_key_obj)  # 生成加密文本
        if be_base64: return base64.b64encode(cryto_msg).decode("utf-8")  # 将加密文本转化为 base64 编码

        return cryto_msg  # 将字节类型的 base64 编码转化为字符串类型


### 当前时间
def now_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))


def is_ip(ip):
    if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b$', ip):
        return True
    return False


if __name__ == "__main__":
    # 待加密字符串或者字节
    ceshiyixia = "富强、民主、文明、和谐”，是我国社会主义现代化国家的建设目标，也是从价值目标层面对社会主义核心价值观基本理念的凝练，在社会主义核心价值观中居于最高层次，对其他层次的价值理念具有统领作用。"

    # MyCryptV3.create_new_keys(num=4096)  ## 4096/8 - 11 生成密钥对

    ## 公钥加密
    cryto_info = MyCryptV3.to_encrypt(ceshiyixia, public_path='public.pem', public_key=None)
    print(cryto_info)

    ## 私钥解密
    haha_info = MyCryptV3.to_decrypt(cryto_info, private_path='private.pem', private_key=None)
    print(haha_info)

    ## 签名
    eee_info = MyCryptV3.to_sign_with_private_key(ceshiyixia, private_path='private.pem', private_key=None)
    print(eee_info)

    ## 验签
    aaa_info = MyCryptV3.to_verify_with_public_key(ceshiyixia, eee_info, public_path='public.pem')
    print(aaa_info)

    public_key = ''
    private_key = ''
    ## 公钥加密
    cryto_info = MyCryptV3.to_encrypt(ceshiyixia, public_path=None, public_key=public_key)
    print(cryto_info)

    ## 私钥解密
    haha_info = MyCryptV3.to_decrypt(cryto_info, private_path=None, private_key=private_key)
    print(haha_info)
