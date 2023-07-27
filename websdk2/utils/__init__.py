#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/12/11
Desc    : 
"""

import os
import time
import json
import socket
import smtplib
from ..consts import const
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid


class SendMail(object):
    def __init__(self, mail_host, mail_port, mail_user, mail_password, mail_ssl=False, mail_tls=False):
        """
        :param mail_host:     SMTP主机
        :param mail_port:     SMTP端口
        :param mail_user:     SMTP账号
        :param mail_password: SMTP密码
        :param mail_ssl:      SSL=True, 如果SMTP端口是465，通常需要启用SSL，  如果SMTP端口是587，通常需要启用TLS
        """
        self.mail_host = mail_host
        self.mail_port = mail_port
        self.__mail_user = mail_user
        self.__mail_password = mail_password
        self.mail_ssl = mail_ssl
        self.mail_tls = mail_tls

    def send_mail(self, to_list, subject, content, subtype='plain', att=None):
        """
        :param to_list:  收件人，多收件人半角逗号分割， 必填
        :param subject:  标题， 必填
        :param content:  内容， 必填
        :param subtype:  格式，默认：plain, 可选html
        :param att:      附件，支持单附件，选填
        """
        msg = MIMEMultipart()
        msg['Subject'] = subject  ## 标题
        msg['From'] = self.__mail_user  ## 发件人
        msg['To'] = to_list  # 收件人，必须是一个字符串
        # 邮件正文内容
        msg.attach(MIMEText(content, subtype, 'utf-8'))
        if att:
            if not os.path.isfile(att):
                raise FileNotFoundError('{0} file does not exist'.format(att))

            dirname, filename = os.path.split(att)
            # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="{0}"'.format(filename)
            msg.attach(att1)

        try:
            if self.mail_ssl:
                '''SSL加密方式，通信过程加密，邮件数据安全, 使用端口465'''
                # print('Use SSL SendMail')
                server = smtplib.SMTP_SSL(host=self.mail_host)
                server.connect(self.mail_host, self.mail_port)  # 连接服务器
                server.login(self.__mail_user, self.__mail_password)  # 登录操作
                server.sendmail(self.__mail_user, to_list.split(','), msg.as_string())
                server.close()
            elif self.mail_tls:
                # print('Use TLS SendMail')
                '''使用TLS模式'''
                server = smtplib.SMTP()
                server.connect(self.mail_host, self.mail_port)  # 连接服务器
                server.starttls()
                server.login(self.__mail_user, self.__mail_password)  # 登录操作
                server.sendmail(self.__mail_user, to_list.split(','), msg.as_string())
                server.close()
                return True
            else:
                '''使用普通模式'''
                server = smtplib.SMTP()
                server.connect(self.mail_host, self.mail_port)  # 连接服务器
                server.login(self.__mail_user, self.__mail_password)  # 登录操作
                server.sendmail(self.__mail_user, to_list.split(','), msg.as_string())
                server.close()
                return True
        except Exception as e:
            print(str(e))
            return False



def mail_login(user, password, mail_server='smtp.exmail.qq.com'):
    ### 模拟登录来验证邮箱
    try:
        server = smtplib.SMTP()
        server.connect(mail_server)
        server.login(user, password)
        return True
    except Exception as e:
        print(user, e)
        return False


# def get_contain_dict(src_data: dict, dst_data: dict) -> bool:
#     if not isinstance(src_data, dict):
#         try:
#             src_data = json.loads(src_data)
#         except Exception as err:
#             return False
#
#     if not isinstance(dst_data, dict):
#         try:
#             dst_data = json.loads(dst_data)
#         except Exception as err:
#             return False
#
#     # src_key = list(src_data.keys())
#     # dst_key = list(dst_data.keys())
#     pd = [False for c in src_data.keys() if c not in dst_data]
#     if pd:
#         return False
#     else:
#         src_val = list(src_data.values())
#         dst_val = list(dst_data.values())
#         pds = [False for c in src_val if c not in dst_val]
#         if pds:
#             return False
#         else:
#             return True

def get_contain_dict(src_data: dict, dst_data: dict) -> bool:
    if not isinstance(src_data, dict):
        try:
            src_data = json.loads(src_data)
        except Exception as err:
            return False

    if not isinstance(dst_data, dict):
        try:
            dst_data = json.loads(dst_data)
        except Exception as err:
            return False

    ### 判断键是否存在
    pd = [False for c in src_data.keys() if c not in dst_data]
    if pd:
        return False
    else:
        src_val = list(src_data.values())
        dst_val = list(dst_data.values())
        pds = [False for c in src_val if c not in dst_val]
        if pds:
            try:
                for d in dst_val:
                    if isinstance(d, dict) and src_val and isinstance(src_val[0], dict):
                        pds1 = [True for sv in src_val[0].keys() if sv in d and d.get(sv) == src_val[0].get(sv)]
                        if True in pds1: return True
            except:
                return False
            return False
        else:
            return True

def now_time_stamp() -> int:
    """
    秒时间戳
    :return: int
    """
    return int(time.time())


### 这个地址具有唯一性
def get_node_address():
    node_name = os.getenv(const.NODE_ADDRESS) if os.getenv(const.NODE_ADDRESS) else socket.gethostname()
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return f'{node_name}--mac-{mac}'


### 这个地址是默认可以通配的
def get_node_topic(node=False):
    if not node:
        if os.getenv(const.NODE_ADDRESS): return os.getenv(const.NODE_ADDRESS) + '#'
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return f'{socket.gethostname()}--mac-{mac}#'
    else:
        if os.getenv(const.NODE_ADDRESS): return os.getenv(const.NODE_ADDRESS)
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return f'{socket.gethostname()}--mac-{mac}'


### 令牌桶限流
'''
示例
import time
from settings import settings
from websdk2.configs import configs
from websdk2.cache_context import cache_conn

if configs.can_import: configs.import_dict(**settings)

redis_conn = cache_conn()
obj = TokenBucket(redis_conn, 'ss', 5, 60)
for i in range(120):
    time.sleep(0.5)
    status = obj.can_access('tuanzi')
    print(status)
'''


class TokenBucket:
    """令牌桶限流"""

    # bucket_key  用来标记令牌
    # func_name   第二段标记
    # capacity = 5  # 桶容量
    # rate = 1  # 速率 每分增加一个令牌

    def __init__(self, cache, bucket_key, capacity: int = 5, rate: int = 1):
        self.bucket_key = bucket_key  # 用来标记令牌桶
        self.capacity = capacity  # 桶容量
        self.rate = rate  # 速率 每分钟增加的令牌
        self.cache = cache
        if not isinstance(rate, int): raise Exception('Rate must be int')

    def can_access(self, func_name) -> bool:
        """令牌桶限流"""
        redis_key = self.bucket_key + func_name

        now = int(time.time())
        current_tokens = self.cache.hget(redis_key, 'current_tokens')
        last_time = self.cache.hget(redis_key, 'last_time')

        current_tokens = current_tokens if current_tokens else self.capacity
        try:
            current_tokens = int(current_tokens)
        except:
            current_tokens = float(current_tokens)
            self.capacity = float(self.capacity)

        last_time = int(last_time) if last_time else now

        increase_tokens = (now - last_time) * self.rate / 60  # 增加的令牌桶  按分钟计算
        current_tokens = min(self.capacity, current_tokens + increase_tokens)
        if current_tokens > 0:
            self.cache.hset(redis_key, 'current_tokens', current_tokens - 1)
            self.cache.hset(redis_key, 'last_time', int(time.time()))
            return True
        else:
            return False


if __name__ == '__main__':
    pass
