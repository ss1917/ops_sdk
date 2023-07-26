#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
Author  : shenshuo
Date    : 2023年2月5日13:37:54
Desc    : 日期时间格式化处理
"""

from datetime import datetime, timedelta


def date_format_to8(start_date: str = None, end_date: str = None) -> tuple:
    """
    # iview 前端日期时间段数据格式化
    start_time_tuple, end_time_tuple = date_format_to8(start_date, end_date)
    # 查询语句中使用
    session.query(dbA).filter(dbA.create_time.between(start_time_tuple, end_time_tuple).all()
    """
    date_format_1 = "%Y-%m-%dT%H:%M:%S.%fZ"
    date_format_2 = "%Y-%m-%d"

    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime(date_format_2)
    if not end_date:
        end_date = (datetime.now() + timedelta(days=1)).strftime(date_format_2)

    for date_format in [date_format_1, date_format_2]:
        try:
            start_time_tuple = datetime.strptime(start_date, date_format) + timedelta(hours=8)
            end_time_tuple = datetime.strptime(end_date, date_format) + timedelta(hours=8)
            return start_time_tuple, end_time_tuple
        except ValueError:
            pass

    raise ValueError(f"Unable to parse the dates. Expected formats are {date_format_1} and {date_format_2}.")
