#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
Date   : 2025年02月08日
Desc   : 存储类
"""

import logging
from sqlalchemy import true
from sqlalchemy.exc import IntegrityError
from .db_context import DBContextV2 as DBContext
from .utils.pydantic_utils import sqlalchemy_to_pydantic, ValidationError, PydanticDelList
from .sqlalchemy_pagination import paginate


class ModelCRUDView:
    def __init__(self, model, **kwargs):
        self.model = model
        self.pydantic_model_base = sqlalchemy_to_pydantic(model)
        self.pydantic_model = sqlalchemy_to_pydantic(model, exclude=['id'])

    def prepare(self):
        pass

    @staticmethod
    def del_data(data) -> dict:
        for key in ['_index', '_rowKey', 'update_time']:
            data.pop(key, None)
        return data

    def handle_get(self, data: dict) -> dict:
        self.prepare()
        data_id = data.get('id')
        if not data_id:
            return dict(code=1, msg="缺少必要的 'id' 参数", data=None)

        try:
            with DBContext('r') as session:
                _info = session.query(self.model).filter(self.model.id == data_id).first()
                if not _info:
                    return dict(code=1, msg='数据未找到', data=None)
                return dict(code=0, msg='获取成功', data={
                    data: _info.to_dict()
                })
        except Exception as e:
            logging.error(f"Database query failed: {e}")
            return dict(code=2, msg='查询失败', data=None)

    def handle_list(self, params: dict, get_by_val_func=None) -> dict:
        self.prepare()

        value = params.get('searchValue', params.get('searchVal'))
        filter_map = params.pop('filter_map', {})
        params.setdefault('page_size', 300)  # 统一处理默认值

        # 如果未提供过滤函数，使用默认函数
        if get_by_val_func is None:
            def default_get_by_val(value: str):
                """默认返回不过滤"""
                return true()

            get_by_val_func = default_get_by_val

        if not callable(get_by_val_func):
            raise ValueError("The `get_by_val_func` parameter must be a callable function.")

        try:
            # 调用 get_by_val_func 生成过滤条件
            filter_condition = get_by_val_func(value)
            if not isinstance(filter_condition, (bool, type(true()))):
                raise ValueError("The `get_by_val_func` must return a SQLAlchemy filter condition or a boolean.")

        except Exception as e:
            raise ValueError(f"Error while executing `get_by_val_func`: {e}")

        with DBContext('r') as session:
            query = session.query(self.model).filter(filter_condition).filter_by(**filter_map)
            page = paginate(query, **params)

        return dict(
            code=0,
            msg='获取成功',
            data={
                'items': page.items,
                'current_page': page.page,  # 当前页
                'total_pages': page.pages,  # 总页数
                'count': page.total  # 总数
            }
        )

    def handle_add(self, data: dict) -> dict:
        self.prepare()
        data = self.del_data(data)
        try:
            self.pydantic_model(**data)
        except ValidationError as e:
            return dict(code=-1, msg=str(e))

        try:
            with DBContext('w', None, True) as db:
                db.add(self.model(**data))
        except IntegrityError as e:
            return dict(code=-2, msg='不要重复添加')

        except Exception as e:
            return dict(code=-3, msg=f'{e}')

        return dict(code=0, msg="创建成功")

    def handle_update(self, data: dict) -> dict:
        self.prepare()
        data = self.del_data(data)
        try:
            valid_data = self.pydantic_model_base(**data)
        except ValidationError as e:
            return dict(code=-1, msg=str(e))

        try:
            with DBContext('w', None, True) as db:
                db.query(self.model).filter(self.model.id == valid_data.id).update(data)

        except IntegrityError as e:
            return dict(code=-2, msg=f'修改失败，已存在')

        except Exception as err:
            return dict(code=-3, msg=f'修改失败, {err}')

        return dict(code=0, msg="修改成功")

    def handle_update_no_validation(self, data: dict) -> dict:
        """不进行校验的更新方法"""
        self.prepare()
        data_id = data.get('id')
        with DBContext('w', None, True) as db:
            db.query(self.model).filter(self.model.id == data_id).update(data)
        return dict(code=0, msg='更新成功')

    def handle_delete(self, data: dict) -> dict:
        self.prepare()
        try:
            valid_data = PydanticDelList(**data)
        except ValidationError as e:
            return dict(code=-1, msg=str(e))

        with DBContext('w', None, True) as session:
            session.query(self.model).filter(self.model.id.in_(valid_data.id_list)).delete(synchronize_session=False)
        return dict(code=0, msg=f"删除成功")
