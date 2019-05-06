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
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\n', '')# 执行加密并转码返回bytes
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

### 当前时间
def now_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

def is_ip(ip):
    if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b$', ip):
        return True
    return False

if __name__ == "__main__":
    pass
