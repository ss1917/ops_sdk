#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
Contact : 191715030@qq.com
Author : shenshuo
Date   : 2018年2月5日13:37:54
Desc   : 处理API请求
"""

# import jwt
# import shortuuid
from shortuuid import uuid
import traceback
# from .cache import get_cache
from .cache_context import cache_conn
from tornado.web import RequestHandler, HTTPError
from .jwt_token import AuthToken, jwt


class BaseHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        self.new_csrf_key = str(uuid())
        self.business_id, self.resource_group = None, None
        self.user_id, self.username, self.nickname, self.email, self.is_super = None, None, None, None, False
        self.is_superuser = self.is_super
        self.token_verify = False
        self.params = {}
        super(BaseHandler, self).__init__(*args, **kwargs)

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

        if self.request_resource_map and isinstance(self.request_resource_map, dict):
            self.params['filter_map'] = {**filter_map, **self.request_resource_map}
        if "auth_key" in self.params: self.params.pop('auth_key')

    def codo_csrf(self):
        # 验证客户端CSRF，如请求为GET，则不验证，否则验证。最后将写入新的key
        cache = cache_conn()

        # or self.request.headers.get('X-Gitlab-Token')
        if self.request.method in ("GET", "HEAD", "OPTIONS") or self.request.headers.get('Sdk-Method'):
            pass
        else:
            csrf_key = self.get_cookie('csrf_key')
            if not csrf_key:  raise HTTPError(402, 'csrf error need csrf key')
            result = cache.get(csrf_key)
            cache.delete(csrf_key)
            if isinstance(result, bytes): result = result.decode()
            if result != '1':   raise HTTPError(402, 'csrf error')
        cache.set(self.new_csrf_key, '1', ex=1800)
        self.set_cookie('csrf_key', self.new_csrf_key)

    def codo_login(self):
        ### 登陆验证
        auth_key = self.get_cookie('auth_key', None)
        if not auth_key:
            url_auth_key = self.get_argument('auth_key', default=None, strip=True)
            if url_auth_key: auth_key = bytes(url_auth_key, encoding='utf-8')

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

    def initialize(self, *args, **kwargs):
        pass

    def prepare(self):
        ### 获取url参数为字典
        self.get_params_dict()
        ### 验证客户端CSRF
        self.codo_csrf()

        ### 登陆验证
        self.codo_login()

        # 验证客户端CSRF，如请求为GET，则不验证，否则验证。最后将写入新的key
        # cache = cache_conn()
        # if self.request.method in ("GET", "HEAD", "OPTIONS") or self.request.headers.get('Sdk-Method'):
        #     pass
        # else:
        #     csrf_key = self.get_cookie('csrf_key')
        #     pipeline = cache.get_pipeline()
        #     result = cache.get(csrf_key, private=False, pipeline=pipeline)
        #     cache.delete(csrf_key, private=False, pipeline=pipeline)
        #     if result != '1':
        #         raise HTTPError(402, 'csrf error')
        #
        # cache.set(self.new_csrf_key, 1, expire=1800, private=False)
        # self.set_cookie('csrf_key', self.new_csrf_key)
        #
        # ### 登陆验证
        # auth_key = self.get_cookie('auth_key', None)
        #
        # if not auth_key:
        #     url_auth_key = self.get_argument('auth_key', default=None, strip=True)
        #     if url_auth_key:
        #         auth_key = bytes(url_auth_key, encoding='utf-8')
        #
        # if not auth_key:
        #     # if not auth_key or not self.get_secure_cookie("user_id") or not self.get_secure_cookie("username") :
        #     # 没登录，就让跳到登陆页面
        #     raise HTTPError(401, 'auth failed')
        #
        # else:
        #     if self.token_verify:
        #         auth_token = AuthToken()
        #         user_info = auth_token.decode_auth_token(auth_key)
        #     else:
        #         user_info = jwt.decode(auth_key, verify=False).get('data')
        #     if not user_info:
        #         raise HTTPError(401, 'auth failed')
        #
        #     self.user_id = user_info.get('user_id', None)
        #     self.username = user_info.get('username', None)
        #     self.nickname = user_info.get('nickname', None)
        #     self.email = user_info.get('email', None)
        #     self.is_super = user_info.get('is_superuser', False)
        #
        #     if not self.user_id:
        #         raise HTTPError(401, 'auth failed')
        #     else:
        #         self.user_id = str(self.user_id)
        #         self.set_secure_cookie("user_id", self.user_id)
        #         self.set_secure_cookie("nickname", self.nickname)
        #         self.set_secure_cookie("username", self.username)
        #         self.set_secure_cookie("email", str(self.email))
        # self.is_superuser = self.is_super

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
            resource_group = self.get_secure_cookie("resource_group")
            if resource_group and isinstance(resource_group, bytes):  return bytes.decode(resource_group)
            return None
        return self.resource_group

    @property
    def request_resource_map(self):
        if self.request_resource_group in [None, 'all', '所有项目']:
            return dict()
        else:
            return dict(resource_group=self.request_resource_group)

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
