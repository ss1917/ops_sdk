#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/9/5
Desc    : 配置文件
"""

from .consts import const
from .tools import singleton


@singleton
class Config(dict):
    def __init__(self):
        self.__can_import = True
        self.__init_default()
        dict.__init__(self)

    def __getattr__(self, item, default=""):
        if item in self:
            return self[item]
        return ""

    @property
    def can_import(self):
        return self.__can_import

    def import_dict(self, **kwargs):
        if self.__can_import:
            for k, v in kwargs.items():
                self[k] = v
            self.__can_import = False
        else:
            raise Exception('ConfigImportError')

    def __init_default(self):
        self['debug'] = False
        self['autoreload'] = True
        self[const.DB_CONFIG_ITEM] = {
            const.DEFAULT_DB_KEY: {
                const.DBHOST_KEY: '',
                const.DBPORT_KEY: 3306,
                const.DBUSER_KEY: '',
                const.DBPWD_KEY: '',
                const.DBNAME_KEY: '',
            },
            const.READONLY_DB_KEY: {
                const.DBHOST_KEY: '',
                const.DBPORT_KEY: 3306,
                const.DBUSER_KEY: '',
                const.DBPWD_KEY: '',
                const.DBNAME_KEY: '',
            }
        }
        self[const.REDIS_CONFIG_ITEM] = {
            const.DEFAULT_RD_KEY: {
                const.RD_HOST_KEY: '',
                const.RD_PORT_KEY: 6379,
                const.RD_DB_KEY: -1,
                const.RD_AUTH_KEY: True,
                const.RD_CHARSET_KEY: 'utf-8',
                const.RD_PASSWORD_KEY: ''
            }
        }
        self[const.MQ_CONFIG_ITEM] = {
            const.DEFAULT_MQ_KEY: {
                const.MQ_ADDR: '',
                const.MQ_PORT: 5672,
                const.MQ_VHOST: '/',
                const.MQ_USER: '',
                const.MQ_PWD: '',
            }
        }
        # self[const.APP_NAME] = ''
        # self[const.LOG_TO_FILE] = False

    def has_item(self, item):
        return item in self

    def clear(self):
        self.__can_import = True
        dict.clear(self)
        self.__init_default()

    @staticmethod
    def __get_key_dict(sub_set, key):
        if key in sub_set:
            sk_dict = sub_set[key]
        else:
            sk_dict = {}
            sub_set[key] = sk_dict
        return sk_dict


configs = Config()
