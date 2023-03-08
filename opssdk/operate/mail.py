#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
author : shenshuo
date   : 2018年2月6日16:28:03
role   : 发送邮件
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, mail_host="smtp.163.com", mail_user="xz_ops_mail", mail_pass="shenshuo1",
                 mail_postfix="163.com"):
        self.mail_host = mail_host    # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
        self.__mail_user = mail_user  # 用户名
        self.__mail_pass = mail_pass  # 密码
        self.mail_postfix = mail_postfix  # 邮箱的后缀，网易就是163.com

    def send_mail(self, to_list, header, sub, content, subtype='plain', att='none'):
        """
        :param to_list:  收件人以半角逗号分隔 必填
        :param header:   发件名，必填
        :param sub:      标题 必填。
        :param content:  发件内容 必填。
        :param subtype:  发件格式 默认plain，可选 html格式
        :param att:      附件 只支持单附件，选填
        """
        me = header + "<" + self.__mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = sub  ## 标题
        msg['From'] = me  ## 发件人
        msg['To'] = to_list  # 收件人，必须是一个字符串

        # 邮件正文内容
        msg.attach(MIMEText(content, subtype, 'utf-8'))
        ### 附件
        if att != 'none':
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
            server = smtplib.SMTP()
            server.connect(self.mail_host)  # 连接服务器
            server.login(self.__mail_user, self.__mail_pass)  # 登录操作
            server.sendmail(me, to_list.split(','), msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(str(e))
            return False
