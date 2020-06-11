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


def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        if isinstance(getattr(model, key), datetime):
            model_dict[column.name] = str(getattr(model, key))
        else:
            model_dict[column.name] = getattr(model, key, None)
    return model_dict


def queryset_to_list(queryset, **kwargs) -> list:
    if kwargs:
        return [model_to_dict(q) for q in queryset if get_contain_dict(kwargs, model_to_dict(q))]
    return [model_to_dict(q) for q in queryset]
