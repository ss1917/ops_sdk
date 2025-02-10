#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
Date   : 2025年02月08日
Desc   : 存储类
"""
import json
import time
import logging
from sqlalchemy import true
from sqlalchemy.exc import IntegrityError
from typing import List, Union, Optional
from .db_context import DBContextV2 as DBContext
from .utils.pydantic_utils import sqlalchemy_to_pydantic, ValidationError, PydanticDelList
from .sqlalchemy_pagination import paginate
from .model_utils import model_to_dict


def get_millisecond_timestamp() -> int:
    """
    获取当前时间的毫秒级时间戳。
    :return: 毫秒级时间戳（int）
    """
    return int(time.time() * 1000)


class ModelCRUDView:
    def __init__(self, model, **kwargs):
        self.model = model
        self.pydantic_model_base = sqlalchemy_to_pydantic(model)
        self.pydantic_model = sqlalchemy_to_pydantic(model, exclude=['id'])

    def prepare(self):
        pass

    @staticmethod
    def parse_id_list(id_list: Union[str, List[int]]) -> Optional[List[int]]:
        """
        解析和验证 id_list 参数。
        """
        if isinstance(id_list, str):
            try:
                id_list = json.loads(id_list)
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse id_list: {e}, input: {id_list}")
                return None
        if isinstance(id_list, list):
            try:
                # 尝试将所有元素转换为整数
                id_list = [int(i) for i in id_list]
                return id_list
            except Exception as e:
                logging.error(f"Invalid id_list element: {e}, input: {id_list}")
                return None
        logging.error(f"Invalid id_list format: {id_list}")
        return None

    @staticmethod
    def del_data(data) -> dict:
        for key in ['_index', '_rowKey', 'update_time']:
            data.pop(key, None)
        return data

    def handle_get(self, data: dict) -> dict:
        self.prepare()
        data_id = data.get('id')
        if not data_id:
            return dict(code=1, msg="缺少必要的 'id' 参数", data=None, reason="", timestamp=get_millisecond_timestamp())

        try:
            with DBContext('r') as session:
                _info = session.query(self.model).filter(self.model.id == data_id).first()
                if not _info:
                    return dict(code=1, msg='数据未找到', data=None, reason="", timestamp=get_millisecond_timestamp())
                return dict(code=0,
                            msg='获取成功',
                            reason="",
                            timestamp=get_millisecond_timestamp(),
                            data={'item': model_to_dict(_info)}
                            )
        except Exception as e:
            logging.error(f"Database query failed: {e}")
            return dict(code=2, msg='查询失败', data=None, reason=str(e), timestamp=get_millisecond_timestamp())

    def handle_list(self, params: dict, get_by_val_func=None) -> dict:
        self.prepare()

        value = params.get('searchValue', params.get('searchVal'))
        id_list = params.get('id_list', [])
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

        try:
            with DBContext('r') as session:
                query = session.query(self.model).filter(filter_condition).filter_by(**filter_map)
                id_list = self.parse_id_list(id_list)
                if id_list:
                    query = query.filter(self.model.id.in_(id_list))

                page = paginate(query, **params)
        except Exception as e:
            return dict(code=2, msg='查询失败', data=None, reason=str(e), timestamp=get_millisecond_timestamp())

        return dict(
            code=0,
            msg='获取成功',
            reason="",
            timestamp=get_millisecond_timestamp(),
            data={
                'items': page.items,
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
            return dict(code=-1, msg='数据格式出错', reason=str(e), data=None, timestamp=get_millisecond_timestamp())

        data.pop("id", None)

        try:
            with DBContext('w', None, True) as db:
                __record = self.model(**data)
                db.add(__record)
                db.flush()
                new_id = __record.id
                return dict(code=0, msg="创建成功", data={"new_id": new_id}, reason="",
                            timestamp=get_millisecond_timestamp())
        except IntegrityError as e:
            return dict(code=-2, msg='不要重复添加', data=None, reason=str(e), timestamp=get_millisecond_timestamp())

        except Exception as e:
            return dict(code=-3, msg='创建失败', data=None, reason=str(e), timestamp=get_millisecond_timestamp())

    def handle_update(self, data: dict) -> dict:
        self.prepare()
        data = self.del_data(data)
        try:
            valid_data = self.pydantic_model_base(**data)
        except ValidationError as e:
            return dict(code=-1, msg="数据格式校验失败", reason=str(e), timestamp=get_millisecond_timestamp())

        try:
            with DBContext('w', None, True) as db:
                db.query(self.model).filter(self.model.id == valid_data.id).update(data)

        except IntegrityError as e:
            return dict(code=-2, msg=f'修改失败，已存在', reason=str(e), timestamp=get_millisecond_timestamp())

        except Exception as e:
            return dict(code=-3, msg=f'修改失败, {e}', reason=str(e), timestamp=get_millisecond_timestamp())

        return dict(code=0, msg="修改成功", reason='', timestamp=get_millisecond_timestamp())

    def handle_update_no_validation(self, data: dict) -> dict:
        """不进行校验的更新方法"""
        self.prepare()
        data_id = data.get('id')
        with DBContext('w', None, True) as db:
            db.query(self.model).filter(self.model.id == data_id).update(data)
        return dict(code=0, msg='更新成功', reason='', timestamp=get_millisecond_timestamp())

    def handle_delete(self, data: dict) -> dict:
        self.prepare()
        try:
            valid_data = PydanticDelList(**data)
        except ValidationError as e:
            return dict(code=-1, msg="数据格式校验失败", reason=str(e), timestamp=get_millisecond_timestamp())

        with DBContext('w', None, True) as session:
            session.query(self.model).filter(self.model.id.in_(valid_data.id_list)).delete(synchronize_session=False)
        return dict(code=0, msg=f"删除成功", reason='', timestamp=get_millisecond_timestamp())
