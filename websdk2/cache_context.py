#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/11/26
Desc    : Redis连接
"""
import threading
from typing import Dict, Optional

import redis
from .consts import const
from .configs import configs

_cache_conns: Dict[str, redis.Redis] = {}
_init_lock = threading.Lock()

# 固定默认值
_MAX_CONNECTIONS: int = 200
_POOL_TIMEOUT: float = 5.0
_SOCKET_CONNECT_TIMEOUT: float = 2.0
_SOCKET_TIMEOUT: float = 3.0
_RETRY_ON_TIMEOUT: bool = True
_HEALTH_CHECK_INTERVAL: int = 30


def _validate_basic_types(key: Optional[str], db: Optional[int]) -> None:
    if key is not None and not isinstance(key, str):
        raise TypeError(f"key 必须为 str 或 None，当前类型为 {type(key).__name__}")
    if db is not None and not isinstance(db, int):
        raise TypeError(f"db 必须为 int 或 None，当前类型为 {type(db).__name__}")
    # 可选：校验 db 合法范围（通常 0-15，取决于服务端配置）
    if isinstance(db, int) and db < 0:
        raise ValueError(f"db 不能为负数，当前值为 {db}")


def _extract_and_validate_cfg(key: str, db: Optional[int]) -> tuple[str, int, Optional[str], bool, bool, int]:
    # 读取配置字典并进行存在性校验
    redis_configs = configs[const.REDIS_CONFIG_ITEM]
    if key not in redis_configs:
        raise ValueError(f"Redis配置键 '{key}' 不存在")
    cfg = redis_configs[key]

    # 逐项提取并校验类型
    host = cfg[const.RD_HOST_KEY]
    port = cfg[const.RD_PORT_KEY]
    password = cfg.get(const.RD_PASSWORD_KEY)
    auth = cfg.get(const.RD_AUTH_KEY, bool(password))
    decode_responses = cfg.get(const.RD_DECODE_RESPONSES, False)
    db_num = db if db is not None else cfg[const.RD_DB_KEY]

    if not isinstance(host, str) or not host:
        raise TypeError(f"RD_HOST 必须为非空字符串，当前: {host!r}")
    if not isinstance(port, int) or port <= 0:
        raise TypeError(f"RD_PORT 必须为正整数，当前: {port!r}")
    if password is not None and not isinstance(password, str):
        raise TypeError(f"RD_PASSWORD 必须为 str 或 None，当前: {type(password).__name__}")
    if not isinstance(auth, bool):
        raise TypeError(f"RD_AUTH 必须为 bool，当前: {type(auth).__name__}")
    if not isinstance(decode_responses, bool):
        raise TypeError(f"RD_DECODE_RESPONSES 必须为 bool，当前: {type(decode_responses).__name__}")
    if not isinstance(db_num, int) or db_num < 0:
        raise TypeError(f"RD_DB 必须为非负整数，当前: {db_num!r}")

    return host, port, password, auth, decode_responses, db_num


def _build_conn(
    host: str,
    port: int,
    db_num: int,
    password: Optional[str],
    auth: bool,
    decode_responses: bool,
    cache_key: str,
) -> redis.Redis:
    # 快速路径（无锁）
    conn = _cache_conns.get(cache_key)
    if conn is not None:
        return conn

    # 慢路径：加锁 + 双重检查
    with _init_lock:
        conn = _cache_conns.get(cache_key)
        if conn is not None:
            return conn

        # 认证处理
        if isinstance(password, str) and password == "":
            password = None
        if not auth and password:
            auth = True
        if auth and not password:
            raise ValueError("Redis要求认证但未提供有效密码")

        # 阻塞连接池 + 固定默认值
        pool = redis.BlockingConnectionPool(
            host=host,
            port=port,
            db=db_num,
            password=password if auth else None,
            decode_responses=decode_responses,
            max_connections=_MAX_CONNECTIONS,
            timeout=_POOL_TIMEOUT,
            socket_connect_timeout=_SOCKET_CONNECT_TIMEOUT,
            socket_timeout=_SOCKET_TIMEOUT,
            retry_on_timeout=_RETRY_ON_TIMEOUT,
            health_check_interval=_HEALTH_CHECK_INTERVAL,
        )

        conn = redis.Redis(connection_pool=pool)
        _cache_conns[cache_key] = conn
        return conn


def cache_conn(key: Optional[str] = None, db: Optional[int] = None) -> redis.Redis:
    """
    获取 Redis 客户端（遵循配置中的 RD_DECODE_RESPONSES）
    - 老代码兼容：如果配置是 False，则返回 bytes；True 则返回 str
    """
    _validate_basic_types(key, db)

    # 默认 key
    if not key:
        from .consts import const as _const
        key = _const.DEFAULT_RD_KEY

    host, port, password, auth, decode_responses, db_num = _extract_and_validate_cfg(key, db)
    cache_key = f"{key}:{db_num}"
    return _build_conn(host, port, db_num, password, auth, decode_responses, cache_key)


def cache_conn_decode(key: Optional[str] = None, db: Optional[int] = None) -> redis.Redis:
    """
    获取 Redis 客户端（强制 decode_responses=True）
    - 所有返回值为 str
    - 与 cache_conn 共存，使用独立的缓存键后缀，避免类型混用
    """
    _validate_basic_types(key, db)

    # 默认 key
    if not key:
        from .consts import const as _const
        key = _const.DEFAULT_RD_KEY

    host, port, password, auth, _decode_responses_cfg, db_num = _extract_and_validate_cfg(key, db)
    cache_key = f"{key}:{db_num}:decode"
    # 强制字符串返回
    return _build_conn(host, port, db_num, password, auth, True, cache_key)
