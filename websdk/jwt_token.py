#!/usr/bin/env python
# -*- coding:utf-8 -*-
import jwt, datetime, hashlib
from .configs import configs as my_configs


class AuthToken:
    def __init__(self):
        self.token_secret = my_configs.get('token_secret', '3AIiOq18i~H=WWTIGq4ODQyMzcsIdfghs')

    def encode_auth_token(self, **kwargs):
        """
        生成认证Token
        :param user_id: string
        :param username: string
        :param nickname: string
        :return: string
        """
        try:
            exp_time = kwargs.get('exp_time', 1)
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=int(exp_time), seconds=10),
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'auth: ss',
                'sub': 'my token',
                'id': '15618718060',
                'data': {
                    'user_id': kwargs.get('user_id', ''),
                    'username': kwargs.get('username', ''),
                    'nickname': kwargs.get('nickname', ''),
                    'email': kwargs.get('email', ''),
                    'is_superuser': kwargs.get('is_superuser', False)
                }
            }
            return jwt.encode(
                payload,
                self.token_secret,
                algorithm='HS256'
            )

        except Exception as e:
            return e

    def encode_auth_token_v2(self, **kwargs):
        ### 支持到自定义小时
        """
        生成认证Token
        :param user_id: string
        :param username: string
        :param nickname: string
        :param exp_time: int
        :param exp_hour: int
        :return: string
        """
        try:
            exp_days = kwargs.get('exp_days', 1)
            exp_hours = kwargs.get('exp_hours')
            if exp_hours and isinstance(exp_hours, int) and exp_days == 1:
                exp_time =  datetime.datetime.utcnow() + datetime.timedelta(hours=int(exp_hours),  seconds=30)
            else:
                exp_time = datetime.datetime.utcnow() + datetime.timedelta(days=int(exp_days), seconds=30)

            payload = {
                'exp': exp_time,
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'auth: ss',
                'sub': 'my token',
                'id': '15618718060',
                'data': {
                    'user_id': kwargs.get('user_id', ''),
                    'username': kwargs.get('username', ''),
                    'nickname': kwargs.get('nickname', ''),
                    'email': kwargs.get('email', ''),
                    'is_superuser': kwargs.get('is_superuser', False)
                }
            }
            return jwt.encode(
                payload,
                self.token_secret,
                algorithm='HS256'
            )

        except Exception as e:
            return e

    def decode_auth_token(self, auth_token):
        """
         验证Token
        :param auth_token:
        :return: dict
        """
        try:
            payload = jwt.decode(auth_token, self.token_secret, algorithms=['HS256'],
                                 leeway=datetime.timedelta(seconds=10))
            if 'data' in payload and 'user_id' in payload['data']:
                return payload['data']
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return dict(status=-1, msg='Token过期')
        except jwt.InvalidTokenError:
            return dict(status=-2, msg='无效Token')


def gen_md5(pd):
    m2 = hashlib.md5()
    m2.update(pd.encode("utf-8"))
    return m2.hexdigest()
