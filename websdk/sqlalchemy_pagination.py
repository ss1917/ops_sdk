#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Version : 0.0.1
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2021/3/2 18:23 
Desc    : 分页
"""

import math
from .model_utils import queryset_to_list


class Page(object):

    def __init__(self, items, page, page_size, total):
        self.items = items
        self.previous_page = None
        self.next_page = None
        self.has_previous = page > 1
        if self.has_previous: self.previous_page = page - 1
        previous_items = (page - 1) * page_size
        self.has_next = previous_items + len(items) < total
        if self.has_next: self.next_page = page + 1
        self.total = total
        self.pages = int(math.ceil(total / float(page_size)))


def paginate(query, order_by: str = None, **query_params):
    page = int(query_params.get('page', 1))
    page_size = int(query_params.get('limit')) if 'limit' in query_params else int(query_params.get('page_size', 10))

    if 'order_by' in query_params: order_by = query_params.get('order_by')
    items_not_to_list = query_params.get('items_not_to_list')  ### 如果不序列化要额外加参数，主要为了连表查询

    if page <= 0: raise AttributeError('page needs to be >= 1')
    if page_size <= 0: raise AttributeError('page_size needs to be >= 1')
    if order_by:
        items = query.order_by(order_by).all() if page_size >= 200 else query.order_by(order_by).limit(
            page_size).offset((page - 1) * page_size).all()
    else:
        items = query.all() if page_size >= 200 else query.limit(page_size).offset((page - 1) * page_size).all()

    total = query.order_by(order_by).count()
    if not items_not_to_list: items = queryset_to_list(items)
    return Page(items, page, page_size, total)
