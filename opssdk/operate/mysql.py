#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author : shenshuo
date   : 2018年2月5日13:37:54
role   : mysql操作
'''

import pymysql
from opssdk.logs import Log


class MysqlBase:
    def __init__(self, **args):
        self.host = args.get('host')
        self.user = args.get('user')
        self.pswd = args.get('passwd')
        self.db = args.get('db')
        self.port = int(args.get('port', 3306))
        self.charset = args.get('charset', 'utf8')

        log_path = '/log/yunwei/yunwei_mysql.log'
        self.log_ins = Log('111', log_path)
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user,
                                        password=self.pswd, db=self.db, port=self.port, charset=self.charset)
            self.cur = self.conn.cursor()
        except:
            raise ValueError('mysql connect error {0}'.format(self.host))

    ###释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()

    ### 查询
    def query(self, sql):
        try:
            self.cur.execute(sql)  # 执行sql语句
            res = self.cur.fetchall()  # 获取查询的所有记录
        except Exception as e:
            self.log_ins.write_log("error", e)
            raise e

        return res

    def change(self, sql):
        resnum = 0
        try:
            resnum = self.cur.execute(sql)
            # 提交
            self.conn.commit()
        except Exception as e:
            # 错误回滚
            self.log_ins.write_log("error", e)
            self.conn.rollback()
        return resnum
