# -*-coding:utf-8-*-
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


def init_engine(**settings):
    if settings:
        databases = settings[const.DB_CONFIG_ITEM]
    else:
        databases = configs[const.DB_CONFIG_ITEM]
    for dbkey, db_conf in databases.items():
        dbuser = db_conf[const.DBUSER_KEY]
        dbpwd = db_conf[const.DBPWD_KEY]
        dbhost = db_conf[const.DBHOST_KEY]
        dbport = db_conf[const.DBPORT_KEY]
        dbname = db_conf[const.DBNAME_KEY]
        engine = create_engine('mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8'
                               .format(user=dbuser, pwd=quote_plus(dbpwd), host=dbhost, port=dbport, dbname=dbname),
                               # logging_name=dbkey)
                               logging_name=dbkey, poolclass=NullPool)
        engines[dbkey] = engine


def get_db_url(dbkey):
    databases = configs[const.DB_CONFIG_ITEM]
    db_conf = databases[dbkey]
    dbuser = db_conf['user']
    dbpwd = db_conf['pwd']
    dbhost = db_conf['host']
    dbport = db_conf.get('port', 3306)
    dbname = db_conf['name']

    return 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8'.format(user=dbuser, pwd=quote_plus(dbpwd),
                                                                                     host=dbhost, port=dbport,
                                                                                     dbname=dbname, poolclass=NullPool)


class DBContext(object):
    def __init__(self, rw='r', db_key=None, need_commit=False, **settings):
        self.__db_key = db_key
        if not self.__db_key:
            if rw == 'w':
                self.__db_key = const.DEFAULT_DB_KEY
            elif rw == 'r':
                self.__db_key = const.READONLY_DB_KEY
        engine = self.__get_db_engine(self.__db_key, **settings)
        self.__engine = engine
        self.need_commit = need_commit

    # @property
    # def db_key(self):
    #     return self.__db_key

    @staticmethod
    def __get_db_engine(db_key, **settings):
        if len(engines) == 0:
            init_engine(**settings)
        return engines[db_key]

    @property
    def session(self):
        return self.__session

    def __enter__(self):
        self.__session = sessionmaker(bind=self.__engine)()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.need_commit:
            if exc_type:
                self.__session.rollback()
            else:
                self.__session.commit()
        self.__session.close()

    def get_session(self):
        return self.__session


def init_engine_v2(**settings):
    if settings:
        databases = settings[const.DB_CONFIG_ITEM]
    else:
        databases = configs[const.DB_CONFIG_ITEM]
    for dbkey, db_conf in databases.items():
        dbuser = db_conf[const.DBUSER_KEY]
        dbpwd = db_conf[const.DBPWD_KEY]
        dbhost = db_conf[const.DBHOST_KEY]
        dbport = db_conf[const.DBPORT_KEY]
        dbname = db_conf[const.DBNAME_KEY]
        engine = create_engine('mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8mb4'
                               .format(user=dbuser, pwd=quote_plus(dbpwd), host=dbhost, port=dbport, dbname=dbname),
                               logging_name=dbkey, poolclass=None, pool_size=30, max_overflow=200, pool_recycle=3600,
                               pool_pre_ping=True)
        engines[dbkey] = engine

class DBContextV2(object):
    def __init__(self, rw='r', db_key=None, need_commit=False, **settings):
        self.__db_key = db_key
        if not self.__db_key:
            if rw == 'w':
                self.__db_key = const.DEFAULT_DB_KEY
            elif rw == 'r':
                self.__db_key = const.READONLY_DB_KEY
        engine = self.__get_db_engine(self.__db_key, **settings)
        self.__engine = engine
        self.need_commit = need_commit

    # @property
    # def db_key(self):
    #     return self.__db_key

    @staticmethod
    def __get_db_engine(db_key, **settings):
        if len(engines) == 0:
            init_engine_v2(**settings)
        return engines[db_key]

    @property
    def session(self):
        return self.__session

    def __enter__(self):
        self.__session = sessionmaker(bind=self.__engine)()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.need_commit:
            if exc_type:
                self.__session.rollback()
            else:
                self.__session.commit()
        self.__session.close()

    def get_session(self):
        return self.__session