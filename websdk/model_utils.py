#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
Date   : 2019年12月11日
Desc   : models类
"""

from datetime import datetime
from sqlalchemy.orm import class_mapper
from .utils import get_contain_dict
from .db_context import DBContextV2 as DBContext
from sqlalchemy import text


def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        if isinstance(getattr(model, key), datetime):
            model_dict[column.name] = str(getattr(model, key))
        else:
            model_dict[column.name] = getattr(model, key, None)

    if isinstance(getattr(model, "custom_extend_column_dict", None), dict):
        model_dict.update(**getattr(model, "custom_extend_column_dict", {}))
    return model_dict


def queryset_to_list(queryset, **kwargs) -> list:
    if kwargs: return [model_to_dict(q) for q in queryset if get_contain_dict(kwargs, model_to_dict(q))]
    return [model_to_dict(q) for q in queryset]


def GetInsertOrUpdateObj(cls: classmethod, str_filter: str, **kw) -> classmethod:
    """
    cls:            Model 类名
    str_filter:      filter的参数.eg:"name='name-14'" 必须设置唯一 支持 and or
    **kw:           【属性、值】字典,用于构建新实例，或修改存在的记录
    session.add(GetInsertOrUpdateObj(TableTest, "name='name-114'", age=33114, height=123.14, name='name-114'))
    """
    with DBContext('r') as session:
        existing = session.query(cls).filter(text(str_filter)).first()
    if not existing:
        res = cls()
        for k, v in kw.items():
            if hasattr(res, k):
                setattr(res, k, v)
        return res
    else:
        res = existing
        for k, v in kw.items():
            if hasattr(res, k):
                setattr(res, k, v)

        return res
