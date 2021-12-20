#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
Contact : 191715030@qq.com
Author : shenshuo
Date   : 2018年2月5日13:37:54
Desc   : 处理API请求
"""

import json
import base64
import hmac
from shortuuid import uuid
import traceback
# from .cache_context import cache_conn
from tornado.escape import utf8, _unicode
from tornado.web import RequestHandler, HTTPError
from .jwt_token import AuthToken, jwt


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        self.new_csrf_key = str(uuid())
        self.business_id, self.resource_group = None, None
        self.user_id, self.username, self.nickname, self.email, self.is_super = None, None, None, None, False
        self.is_superuser = self.is_super
        self.token_verify = False
        self.tenant_filter = False
        self.params = {}
        super(BaseHandler, self).__init__(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        pass

    def get_params_dict(self):
        self.params = {k: self.get_argument(k) for k in self.request.arguments}
        if "filter_map" in self.params:
            try:
                import json
                filter_map = self.params.get('filter_map')
                filter_map = json.loads(filter_map)
            except:
                filter_map = {}
        else:
            filter_map = {}
        self.params['filter_map'] = filter_map

        if self.tenant_filter and self.request_tenant_map and isinstance(self.request_tenant_map, dict):
            self.params['filter_map'] = {**filter_map, **self.request_tenant_map}

        if "auth_key" in self.params: self.params.pop('auth_key')

    def codo_csrf(self):
        pass

    def check_xsrf_cookie(self):
        if not self.settings.get('xsrf_cookies'): return
        if self.request.method in ("GET", "HEAD", "OPTIONS") or self.request.headers.get('Sdk-Method'):
            pass
        else:
            token = (
                    self.get_argument("_xsrf", None)
                    or self.request.headers.get("X-Xsrftoken")
                    or self.request.headers.get("X-Csrftoken")
            )
            if not token: raise HTTPError(402, "'_xsrf' argument missing from POST")
            _, token, _ = self._decode_xsrf_token(token)
            _, expected_token, _ = self._get_raw_xsrf_token()
            if not token:
                raise HTTPError(402, "'_xsrf' argument has invalid format")
            if not hmac.compare_digest(utf8(token), utf8(expected_token)):
                raise HTTPError(402, "XSRF cookie does not match POST argument")

    def codo_login(self):
        ### 登陆验证
        auth_key = self.get_cookie('auth_key') if self.get_cookie("auth_key") else self.request.headers.get('auth-key')
        if not auth_key: auth_key = self.get_argument('auth_key', default=None, strip=True)

        if not auth_key: raise HTTPError(401, 'auth failed')

        if self.token_verify:
            auth_token = AuthToken()
            user_info = auth_token.decode_auth_token(auth_key)
        else:
            user_info = jwt.decode(auth_key, options={"verify_signature": False}).get('data')

        if not user_info: raise HTTPError(401, 'auth failed')

        self.user_id = user_info.get('user_id', None)
        self.username = user_info.get('username', None)
        self.nickname = user_info.get('nickname', None)
        self.email = user_info.get('email', None)
        self.is_super = user_info.get('is_superuser', False)

        if not self.user_id: raise HTTPError(401, 'auth failed')

        self.user_id = str(self.user_id)
        self.set_secure_cookie("user_id", self.user_id)
        self.set_secure_cookie("nickname", self.nickname)
        self.set_secure_cookie("username", self.username)
        self.set_secure_cookie("email", str(self.email))
        self.is_superuser = self.is_super

    def prepare(self):
        ### 获取url参数为字典
        self.get_params_dict()
        ### 验证客户端CSRF
        self.codo_csrf()
        self.xsrf_token

        ### 登陆验证
        self.codo_login()

    def get_current_user(self):
        return self.username

    def get_current_id(self):
        return self.user_id

    def get_current_nickname(self):
        return self.nickname

    def get_current_email(self):
        return self.email

    def is_superuser(self):
        return self.is_superuser

    @property
    def request_resource_group(self):
        if not self.resource_group:
            self.resource_group = self.get_secure_cookie("resource_group") if self.get_secure_cookie(
                "resource_group") else self.request.headers.get('resource-group')

            if not self.resource_group: return None
            if isinstance(self.resource_group, bytes):  self.resource_group = bytes.decode(self.resource_group)
            return self.resource_group

        return self.resource_group

    @property
    def request_resource_map(self):
        if self.request_resource_group in [None, 'all', '所有项目']:
            return dict()
        else:
            return dict(resource_group=self.request_resource_group)

    @property
    def request_business_id(self):
        if not self.business_id:
            self.business_id = self.get_secure_cookie("business_id") if self.get_secure_cookie("business_id") else \
                self.request.headers.get('biz-id')
            if not self.business_id: return None
            if isinstance(self.business_id, bytes):  self.business_id = bytes.decode(self.business_id)
            return self.business_id

        return self.business_id

    ### 新添加
    @property
    def request_tenant(self):
        if self.request.headers.get('tenant'):
            return str(base64.b64decode(self.request.headers.get('tenant')), "utf-8")
        if self.get_secure_cookie('tenant'):  return self.get_secure_cookie('tenant')
        if self.get_secure_cookie('resource_group'):  return self.get_secure_cookie('resource_group')
        return None

    @property
    def request_tenantid(self):
        if self.request.headers.get('tenantid'):  return self.request.headers.get('tenantid')
        if self.get_secure_cookie('tenantid'):  return self.get_secure_cookie('tenantid')
        if self.get_secure_cookie('business_id'):  return self.get_secure_cookie('business_id')
        return None

    @property
    def request_tenant_map(self):
        if self.request_tenantid in [None, '500'] or self.request_tenant in [None, 'all', '所有项目']:
            return dict()
        else:
            return dict(tenantid=self.request_tenantid)

    @property
    def biz_info_map(self):
        from .cache_context import cache_conn
        redis_conn = cache_conn()
        try:
            biz_info_str = redis_conn.get("BIZ_INFO_STR")
            biz_info_dict = json.loads(biz_info_str.decode())
        except Exception as err:
            return {}
        return biz_info_dict

    @property
    def request_username(self):
        return self.username

    @property
    def request_user_id(self):
        return self.user_id

    @property
    def request_nickname(self):
        return self.nickname

    @property
    def request_email(self):
        return self.email

    @property
    def request_is_superuser(self):
        return self.is_superuser

    def request_fullname(self):
        return f'{self.request_username}({self.request_nickname})'

    def write_error(self, status_code, **kwargs):
        error_trace_list = traceback.format_exception(*kwargs.get("exc_info"))
        if status_code == 404:
            self.set_status(status_code)
            return self.finish('找不到相关路径-404')

        elif status_code == 400:
            self.set_status(status_code)
            return self.finish('bad request...')

        elif status_code == 402:
            self.set_status(status_code)
            return self.finish('csrf error...')

        elif status_code == 403:
            self.set_status(status_code)
            return self.finish('Sorry, you have no permission. Please contact the administrator')

        if status_code == 500:
            self.set_status(status_code)
            for line in error_trace_list:
                self.write(str(line))
            self.finish()

        elif status_code == 401:
            self.set_status(status_code)
            return self.finish('你没有登录')

        else:
            self.set_status(status_code)


class LivenessProbe(RequestHandler):
    def initialize(self, *args, **kwargs):
        pass

    def head(self, *args, **kwargs):
        self.write(dict(code=0, msg="I'm OK"))

    def get(self, *args, **kwargs):
        self.write(dict(code=0, msg="I'm OK"))
