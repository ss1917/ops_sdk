# -*- coding: utf-8 -*-
"""封装 OpenAPIClient，供 CLI 使用。"""

from __future__ import print_function

import json

from websdk2.openapi_client import OpenAPIClient


def build_client(settings):
    endpoint = settings.get('endpoint') or ''
    ak = settings.get('access_key') or ''
    sk = settings.get('secret_key') or ''
    if not endpoint:
        raise SystemExit('缺少 endpoint：请配置 CODO_ENDPOINT 或 ~/.codo/config.yaml')
    if not ak:
        raise SystemExit('缺少 access_key：请配置 CODO_ACCESS_KEY 或 config profile')
    if not sk:
        raise SystemExit(
            '缺少 secret_key：请设置环境变量 CODO_SECRET_KEY（禁止写入配置文件）'
        )
    return OpenAPIClient(
        access_key=ak,
        secret_key=sk,
        endpoint=endpoint,
        request_timeout=int(settings.get('timeout') or 10),
    )


def do_request(client, method, path, params=None, data=None, json_body=None):
    return client.request(
        method=method,
        url=path,
        params=params,
        data=data,
        json_body=json_body,
    )


def merge_api_spec(spec, param_overrides=None, body_overrides=None, method=None):
    """把 AdminV4APIS 条目与 CLI 覆盖参数合并为 request kwargs。"""
    method = (method or spec.get('method') or 'GET').upper()
    path = spec.get('url')
    params = dict(spec.get('params') or {})
    if param_overrides:
        params.update(param_overrides)
    # 空 params 不传
    if not params:
        params = None

    json_body = None
    data = None
    if method in ('POST', 'PUT', 'PATCH', 'DELETE'):
        body = spec.get('body')
        if body_overrides is not None:
            json_body = body_overrides
        elif isinstance(body, dict):
            json_body = dict(body)
        elif body is not None:
            data = body
    return {
        'method': method,
        'path': path,
        'params': params,
        'json_body': json_body,
        'data': data,
    }


def print_response(resp, pretty=False, show_headers=False):
    text = resp.text
    if pretty:
        try:
            obj = resp.json()
            text = json.dumps(obj, ensure_ascii=False, indent=2)
        except Exception:
            pass
    if show_headers:
        print('HTTP', resp.status_code)
        for k, v in resp.headers.items():
            print('%s: %s' % (k, v))
        print()
    print(text)
    return 0 if 200 <= resp.status_code < 300 else 1
