#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author : shenshuo
date   : 2017年10月17日17:23:19
role   : 数据库连接
"""

import pymysql
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from .consts import const
from .configs import configs

engines = {}
scheduler_engines = {}


class DBConfigError(Exception):
    pass


# 调度器专用引擎池

def init_scheduler_engine(**settings):
    databases = settings.get(const.DB_CONFIG_ITEM) or configs[const.DB_CONFIG_ITEM]

    for dbkey, db_conf in databases.items():
        # 获取配置
        dbuser = db_conf.get(const.DBUSER_KEY)
        dbpwd = db_conf.get(const.DBPWD_KEY)
        dbhost = db_conf.get(const.DBHOST_KEY)
        dbport = db_conf.get(const.DBPORT_KEY)
        dbname = db_conf.get(const.DBNAME_KEY)

        # 验证配置完整性
        if None in (dbuser, dbpwd, dbhost, dbname):
            raise DBConfigError(f"Incomplete database configuration for '{dbkey}'")

        # 创建调度器专用引擎（小规格连接池）
        engine = create_engine(
            f'mysql+pymysql://{dbuser}:{quote_plus(dbpwd)}@{dbhost}:{dbport}/{dbname}?charset=utf8mb4',
            logging_name=dbkey,
            poolclass=None,  # QueuePool
            pool_size=10,  # 10个常驻连接（调度器用）
            max_overflow=30,  # 30个溢出连接
            pool_recycle=1800,  # 30分钟回收
            pool_pre_ping=True,  # 启用连接检查
            pool_timeout=10,  # 5秒超时
            echo_pool=False  # 关闭连接池日志
        )

        scheduler_engines[dbkey] = engine


def get_scheduler_engine(dbkey='default', **settings):
    if not scheduler_engines:
        init_scheduler_engine(**settings)
    return scheduler_engines[dbkey]


def _build_db_url(db_conf, const) -> str:
    """构建数据库连接URL"""
    return 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8mb4'.format(
        user=db_conf[const.DBUSER_KEY],
        pwd=quote_plus(db_conf[const.DBPWD_KEY]),
        host=db_conf[const.DBHOST_KEY],
        port=db_conf[const.DBPORT_KEY],
        dbname=db_conf[const.DBNAME_KEY]
    )


def init_engine(use_pool=False, pool_config=None, **settings):
    databases = settings.get(const.DB_CONFIG_ITEM) or configs[const.DB_CONFIG_ITEM]

    # 默认连接池配置 - 优化后的推荐值
    default_pool_config = {
        'pool_size': 20,  # 常驻连接: 20 (原10)
        'max_overflow': 30,  # 溢出连接: 30 (原50, 过大)
        'pool_recycle': 3600,  # 回收时间: 1小时
        'pool_pre_ping': True,  # 预检查: 启用 (避免僵尸连接)
        'pool_timeout': 20,  # 获取超时: 20秒 (原60秒, 过长)
        'echo_pool': False,  # 连接池日志: 关闭 (生产环境)
    }

    # 合并用户自定义配置
    if pool_config:
        default_pool_config.update(pool_config)

    for dbkey, db_conf in databases.items():
        db_url = _build_db_url(db_conf, const)

        if use_pool:
            # 使用连接池配置
            engine = create_engine(
                db_url,
                logging_name=dbkey,
                poolclass=None,  # 默认 QueuePool
                **default_pool_config
            )
        else:
            # 不使用连接池 (每次新建连接)
            engine = create_engine(db_url, logging_name=dbkey, poolclass=NullPool)

        engines[dbkey] = engine


def get_db_url(dbkey):
    """获取数据库连接URL"""
    db_conf = configs[const.DB_CONFIG_ITEM][dbkey]
    return _build_db_url(db_conf, const)


class DBContext:
    def __init__(self, rw='r', db_key=None, need_commit=False, use_pool=False, pool_config=None, **settings):
        self.__db_key = db_key or (const.DEFAULT_DB_KEY if rw == 'w' else const.READONLY_DB_KEY)
        self.__engine = self.__get_db_engine(self.__db_key, use_pool, pool_config, **settings)
        self.need_commit = need_commit
        self.__session = None

    @staticmethod
    def __get_db_engine(db_key, use_pool, pool_config, **settings):
        """获取数据库引擎"""
        if not engines:
            init_engine(use_pool=use_pool, pool_config=pool_config, **settings)
        return engines[db_key]

    @property
    def session(self):
        """获取session"""
        return self.__session

    def __enter__(self):
        """进入上下文"""
        self.__session = sessionmaker(bind=self.__engine)()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.need_commit:
            if exc_type:
                self.__session.rollback()
            else:
                self.__session.commit()
        self.__session.close()

    def get_session(self):
        """获取session（向后兼容）"""
        return self.__session


# ==================== 向后兼容 ====================

# DBContextV2 别名（完全兼容旧代码）
DBContextV2 = DBContext
