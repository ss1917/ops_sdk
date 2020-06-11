#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/12/11
Desc    : 
"""

import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest, QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
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
                server = smtplib.SMTP_SSL()
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


class SendSms(object):
    def __init__(self, REGION, DOMAIN, PRODUCT_NAME, sms_access_key_id, sms_access_key_secret, ):
        self.acs_client = AcsClient(sms_access_key_id, sms_access_key_secret, REGION)
        region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

    def send_sms(self, phone_numbers, template_param=None, sign_name="ops", template_code=""):
        business_id = uuid.uuid1()
        sms_request = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        sms_request.set_TemplateCode(template_code)

        # 短信模板变量参数
        if template_param is not None:
            sms_request.set_TemplateParam(template_param)

        # 设置业务请求流水号，必填。
        sms_request.set_OutId(business_id)

        # 短信签名
        sms_request.set_SignName(sign_name)

        # 短信发送的号码列表，必填。
        sms_request.set_PhoneNumbers(phone_numbers)

        # 调用短信发送接口，返回json
        sms_response = self.acs_client.do_action_with_exception(sms_request)

        ##业务处理
        return sms_response

    def query_send_detail(self, biz_id, phone_number, page_size, current_page, send_date):
        query_request = QuerySendDetailsRequest.QuerySendDetailsRequest()
        # 查询的手机号码
        query_request.set_PhoneNumber(phone_number)
        # 可选 - 流水号
        query_request.set_BizId(biz_id)
        # 必填 - 发送日期 支持30天内记录查询，格式yyyyMMdd
        query_request.set_SendDate(send_date)
        # 必填-当前页码从1开始计数
        query_request.set_CurrentPage(current_page)
        # 必填-页大小
        query_request.set_PageSize(page_size)

        # 数据提交方式
        # queryRequest.set_method(MT.POST)

        # 数据提交格式
        # queryRequest.set_accept_format(FT.JSON)

        # 调用短信记录查询接口，返回json
        query_response = self.acs_client.do_action_with_exception(query_request)
        # print(query_response.decode('utf-8'))

        return query_response


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

    # src_key = list(src_data.keys())
    # dst_key = list(dst_data.keys())
    pd = [False for c in src_data.keys() if c not in dst_data]
    if pd:
        return False
    else:
        src_val = list(src_data.values())
        dst_val = list(dst_data.values())
        pds = [False for c in src_val if c not in dst_val]
        if pds:
            return False
        else:
            return True

if __name__ == '__main__':
    pass
