#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : ming
date   : 2017/4/11 下午1:54
role   : 常量管理
"""

from enum import IntEnum as Enum


class ConstError(TypeError):
    pass


class IntEnum(Enum):
    @staticmethod
    def find_enum(cls, value):
        for k, v in cls._value2member_map_.items():
            if k == value:
                return v
        return None


class ErrorCode(IntEnum):
    """ 错误码枚举 """

    not_found = 404
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_allowed = 405
    not_acceptable = 406
    conflict = 409
    gone = 410
    precondition_failed = 412
    request_entity_too_large = 413
    unsupport_media_type = 415
    internal_server_error = 500
    service_unavailable = 503
    service_not_implemented = 501
    handler_uncatched_exception = 504
    config_import_error = 1001
    config_item_notfound_error = 1002


class _const(object):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise ConstError("Can't rebind const (%s)" % name)
        if not name.isupper():
            raise ConstError("Const must be upper.")
        self.__dict__[name] = value


const = _const()

const.DB_CONFIG_ITEM = 'databases'
const.DBHOST_KEY = 'host'
const.DBPWD_KEY = 'pwd'
const.DBUSER_KEY = 'user'
const.DBNAME_KEY = 'name'
const.DBPORT_KEY = 'port'
const.SF_DB_KEY = 'vmobel'
const.DEFAULT_DB_KEY = 'default'
const.READONLY_DB_KEY = 'readonly'

const.REDIS_CONFIG_ITEM = 'redises'
const.RD_HOST_KEY = 'host'
const.RD_PORT_KEY = 'port'
const.RD_DB_KEY = 'db'
const.RD_AUTH_KEY = 'auth'
const.RD_CHARSET_KEY = 'charset'
const.RD_DECODE_RESPONSES = 'decode_responses'
const.RD_PASSWORD_KEY = 'password'
const.DEFAULT_RD_KEY = 'default'

# ETCD
const.DEFAULT_ETCD_KEY = "default"
const.BACKUP_ETCD_KEY = "backup"
const.DEFAULT_ETCD_HOST = "host"
const.DEFAULT_ETCD_PORT = "port"
const.DEFAULT_ETCD_PROTOCOL = "protocol"
const.DEFAULT_ETCD_USER = "user"
const.DEFAULT_ETCD_PWD = "pwd"

# MQ
const.MQ_CONFIG_ITEM = 'mqs'
const.MQ_ADDR = 'MQ_ADDR'
const.MQ_PORT = 'MQ_PORT'
const.MQ_VHOST = 'MQ_VHOST'
const.MQ_USER = 'MQ_USER'
const.MQ_PWD = 'MQ_PWD'
const.DEFAULT_MQ_KEY = 'default'
const.AGENT_MQ_KEY = 'agent'

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
const.LOG_LEVEL = "log_level"
# JMS
const.JMS_CONFIG_ITEM = 'jmss'
const.DEFAULT_JMS_KEY = 'default'
const.JMS_API_BASE_URL = "jms_url"
const.JMS_API_KEY_ID = "jms_key_id"
const.JMS_API_KEY_SECRET = "jms_key_secret"

# consul
const.CONSUL_CONFIG_ITEM = 'consuls'
const.DEFAULT_CS_KEY = 'default'
const.CONSUL_HOST_KEY = 'cs_host'
const.CONSUL_PORT_KEY = 'cs_port'
const.CONSUL_TOKEN_KEY = 'cs_token'
const.CONSUL_SCHEME_KEY = 'cs_scheme'

# kafka
const.KAFKA_BOOTSTRAP_SERVERS = 'kafka_bootstrap_servers'
const.KAFKA_CLIENT_ID = 'kafka_client_id'
const.KAFKA_TOPIC = 'kafka_topic'

const.APP_NAME = 'app_name'
const.LOG_PATH = 'log_path'
const.LOG_BACKUP_COUNT = 'log_backup_count'
const.LOG_MAX_FILE_SIZE = 'log_max_filesize'

const.REQUEST_START_SIGNAL = 'request_start'
const.REQUEST_FINISHED_SIGNAL = 'request_finished'

const.NW_SALT = 'nw'
const.ALY_SALT = 'aly'
const.TX_SALT = 'tx'
const.SG_SALT = 'sg'
const.DEFAULT_SALT = 'default'
const.SALT_API = 'salt_api'
const.SALT_USER = 'salt_username'
const.SALT_PW = 'salt_password'
const.SALT_OUT = 'salt_timeout'

const.NW_INCEPTION = 'nw'
const.ALY_INCEPTION = 'aly'
const.TX_INCEPTION = 'tx'
const.DEFAULT_INCEPTION = 'default'

const.REGION = "cn-hangzhou"
const.PRODUCT_NAME = "Dysmsapi"
const.DOMAIN = "dysmsapi.aliyuncs.com"

# crypto
const.AES_CRYPTO_KEY = 'aes_crypto_key'
### app settings
const.APP_SETTINGS = 'APP_SETTINGS'
### all user info
const.USERS_INFO = 'USERS_INFO'

# API GW
const.WEBSITE_API_GW_URL = 'api_gw'
const.API_AUTH_KEY = 'settings_auth_key'
const.EMAILLOGIN_DOMAIN = 'EMAILLOGIN_DOMAIN'
const.EMAILLOGIN_SERVER = 'EMAILLOGIN_SERVER'

# email
const.EMAIL_SUBJECT_PREFIX = "EMAIL_SUBJECT_PREFIX"
const.EMAIL_HOST = "EMAIL_HOST"
const.EMAIL_PORT = "EMAIL_PORT"
const.EMAIL_HOST_USER = "EMAIL_HOST_USER"
const.EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD"
const.EMAIL_USE_SSL = "EMAIL_USE_SSL"
const.EMAIL_USE_TLS = "EMAIL_USE_TLS"

# 短信配置
const.SMS_REGION = "SMS_REGION"
const.SMS_PRODUCT_NAME = "SMS_PRODUCT_NAME"
const.SMS_DOMAIN = "SMS_DOMAIN"

const.SMS_ACCESS_KEY_ID = 'SMS_ACCESS_KEY_ID'
const.SMS_ACCESS_KEY_SECRET = 'SMS_ACCESS_KEY_SECRET'
# 钉钉
const.DING_TALK_WEBHOOK = "DING_TALK_WEBHOOK"
# 存储
const.STORAGE_REGION = "STORAGE_REGION"
const.STORAGE_NAME = "STORAGE_NAME"
const.STORAGE_PATH = "STORAGE_PATH"
const.STORAGE_KEY_ID = "STORAGE_KEY_ID"
const.STORAGE_KEY_SECRET = "STORAGE_KEY_SECRET"

### LDAP
const.LDAP_SERVER_HOST = "LDAP_SERVER_HOST"
const.LDAP_SERVER_PORT = "LDAP_SERVER_PORT"
const.LDAP_ADMIN_DN = "LDAP_ADMIN_DN"
const.LDAP_ADMIN_PASSWORD = "LDAP_ADMIN_PASSWORD"
const.LDAP_SEARCH_BASE = "LDAP_SEARCH_BASE"
const.LDAP_SEARCH_FILTER = "LDAP_SEARCH_FILTER"
const.LDAP_ATTRIBUTES = "LDAP_ATTRIBUTES"
const.LDAP_USE_SSL = "LDAP_USE_SSL"
const.LDAP_ENABLE = "LDAP_ENABLE"

### token 超时时间
const.TOKEN_EXP_TIME = "TOKEN_EXP_TIME"

### 全局 二次认证
const.MFA_GLOBAL = 'MFA_GLOBAL'

# task event 状态
const.STATE_NEW = '0'  # 新建任务
const.STATE_WAIT = '1'  # 等待执行
const.STATE_RUNNING = '2'  # 正在运行
const.STATE_SUCCESS = '3'  # 成功完成
const.STATE_ERROR = '4'  # 发生错误
const.STATE_MANUAL = '5'  # 等待手动
const.STATE_BREAK = '6'  # 中止状态 //不区分手动和自动
const.STATE_TIMING = '7'  # 定时状态
const.STATE_UNKNOWN = '8'  # 未知状态  // debug
const.STATE_FAIL = '9'  # 失败         // debug
const.STATE_IGNORE = '10'  # 忽略执行
const.STATE_QUEUE = '11'  # 排队中   //订单和任务节点公用
# 订单 状态
const.ORDER_STATE_WAITING = '31'  # 订单等待中
const.ORDER_STATE_RUNNING = '32'  # 订单执行中
const.ORDER_STATE_SUCCESS = '33'  # 订单成功
const.ORDER_STATE_FAIL = '34'  # 订单失败
const.ORDER_STATE_WAITING_APPROVAL = '35'  # 订单等待审批
const.ORDER_STATE_TERMINATED = '39'  # 订单终止
const.ORDER_STATE_QUEUE = '11'  # 订单排队中
const.EXEC_TIMEOUT = 1800

# 节点地址
const.NODE_ADDRESS = 'NODE_ADDRESS'
const.EXEC_NODE_MAP_KEY = 'EXEC_NODE_MAP_KEY'
const.AGENT_USED_KEY = "agent_is_used_map_mark_key"

# otel
const.JAEGER_EXPORTER_HOST = "jaeger_exporter_host"
const.JAEGER_EXPORTER_PORT = "jaeger_exporter_port"
const.OTEL_ENABLED = "otel_enabled"
