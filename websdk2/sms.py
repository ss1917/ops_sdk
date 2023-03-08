#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
author : shenshuo
date   : 2018年5月22日
role   ：发送短信

pip install --upgrade setuptools
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-dysmsapi
"""
import sys, json
from libs.consts import const
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err


class SmsApi:
    def __init__(self, sms_access_key_id, sms_access_key_secret, REGION=const.REGION, DOMAIN=const.DOMAIN,
                 PRODUCT_NAME=const.PRODUCT_NAME):
        self.acs_client = AcsClient(sms_access_key_id, sms_access_key_secret, REGION)
        region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

    def send_sms(self, phone_numbers, template_param=None, sign_name="自动化", template_code="SMS_136397944"):
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


if __name__ == '__main__':
    pass
