# -*- coding: utf-8 -*-
"""codo-cli 入口：argparse；默认随 codosdk 安装即可用。"""
from __future__ import print_function

import argparse
import json
import sys

from codo_cli import __version__
from codo_cli import config as conf
from codo_cli.client import build_client, do_request, merge_api_spec, print_response


WRITE_METHODS = frozenset(['POST', 'PUT', 'PATCH', 'DELETE'])


def _parse_kv_list(items):
    """['a=1', 'b=2'] -> dict"""
    out = {}
    if not items:
        return out
    for it in items:
        if '=' not in it:
            raise SystemExit('参数格式错误，应为 key=value: %s' % it)
        k, v = it.split('=', 1)
        out[k.strip()] = v
    return out


def _load_json_arg(raw):
    if raw is None:
        return None
    if raw.startswith('@'):
        path = raw[1:]
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return json.loads(raw)


def _settings_from_ns(ns):
    return conf.resolve_settings(
        profile=getattr(ns, 'profile', None),
        endpoint=getattr(ns, 'endpoint', None),
        access_key=getattr(ns, 'access_key', None),
        secret_key=getattr(ns, 'secret_key', None),
        timeout=getattr(ns, 'timeout', None),
    )


def cmd_config_init(ns):
    path, created = conf.init_config(force=ns.force)
    if created:
        print('已创建配置: %s' % path)
        print('请编辑 endpoint/access_key，并 export CODO_SECRET_KEY=...')
    else:
        print('配置已存在: %s （使用 --force 覆盖）' % path)
    return 0


def cmd_config_show(ns):
    s = _settings_from_ns(ns)
    view = conf.public_settings_view(s)
    print(json.dumps(view, ensure_ascii=False, indent=2))
    return 0


def cmd_config_path(ns):
    print(conf.CONFIG_PATH)
    return 0


def cmd_api_request(ns):
    method = ns.method.upper()
    path = ns.path
    if not path.startswith('/'):
        path = '/' + path

    if method in WRITE_METHODS and not ns.yes:
        print(
            '写操作 %s 需要显式确认，请添加 --yes' % method,
            file=sys.stderr,
        )
        return 2

    params = _parse_kv_list(ns.param)
    json_body = None
    data = None
    if ns.data is not None:
        try:
            json_body = _load_json_arg(ns.data)
        except json.JSONDecodeError:
            # 非 JSON 当原始 body
            if ns.data.startswith('@'):
                with open(ns.data[1:], 'rb') as f:
                    data = f.read()
            else:
                data = ns.data

    settings = _settings_from_ns(ns)
    client = build_client(settings)
    resp = do_request(
        client,
        method,
        path,
        params=params or None,
        data=data,
        json_body=json_body,
    )
    return print_response(resp, pretty=ns.pretty, show_headers=ns.headers)


def cmd_admin_list(ns):
    from websdk2.apis.mgv4_apis import AdminV4APIS

    items = AdminV4APIS.list_apis()
    if ns.filter:
        kw = ns.filter.lower()
        items = [
            i for i in items
            if kw in i['name'].lower()
            or kw in (i.get('description') or '').lower()
            or kw in (i.get('url') or '').lower()
        ]
    if ns.pretty or not ns.quiet:
        print(json.dumps(items, ensure_ascii=False, indent=2 if ns.pretty else None))
    else:
        for i in items:
            print(i['name'])
    return 0


def cmd_admin_call(ns):
    from websdk2.apis.mgv4_apis import AdminV4APIS

    spec = AdminV4APIS.get_api(ns.name)
    if not spec:
        print('未知 API: %s （codo-cli admin list 查看）' % ns.name, file=sys.stderr)
        return 2

    method = (ns.method or spec.get('method') or 'GET').upper()
    if method in WRITE_METHODS and not ns.yes:
        print(
            '写操作 %s (%s) 需要显式确认，请添加 --yes' % (method, ns.name),
            file=sys.stderr,
        )
        return 2

    param_overrides = _parse_kv_list(ns.param)
    body_overrides = None
    if ns.data is not None:
        body_overrides = _load_json_arg(ns.data)

    req = merge_api_spec(
        spec,
        param_overrides=param_overrides,
        body_overrides=body_overrides,
        method=method,
    )
    settings = _settings_from_ns(ns)
    client = build_client(settings)
    resp = do_request(
        client,
        req['method'],
        req['path'],
        params=req['params'],
        data=req['data'],
        json_body=req['json_body'],
    )
    return print_response(resp, pretty=ns.pretty, show_headers=ns.headers)


def cmd_admin_user_list(ns):
    ns.name = 'get_user_list'
    ns.method = None
    ns.data = None
    ns.param = ns.param or []
    if ns.search:
        ns.param = list(ns.param) + ['searchVal=%s' % ns.search]
    return cmd_admin_call(ns)


def cmd_admin_biz_list(ns):
    ns.name = 'get_biz_list'
    ns.method = None
    ns.data = None
    ns.param = ns.param or []
    return cmd_admin_call(ns)


def cmd_admin_role_base_list(ns):
    ns.name = 'get_all_base_role_list'
    ns.method = None
    ns.data = None
    ns.param = ns.param or []
    return cmd_admin_call(ns)


def _add_global_auth_args(p):
    p.add_argument('--profile', default=None, help='配置 profile 名')
    p.add_argument('--endpoint', default=None, help='网关地址，覆盖配置')
    p.add_argument('--access-key', default=None, dest='access_key', help='AccessKey')
    p.add_argument(
        '--secret-key',
        default=None,
        dest='secret_key',
        help='SecretKey（更推荐环境变量 CODO_SECRET_KEY）',
    )
    p.add_argument('--timeout', type=int, default=None, help='请求超时秒')
    p.add_argument('--pretty', action='store_true', help='JSON 缩进输出')
    p.add_argument('--headers', action='store_true', help='打印响应头')


def build_parser():
    parser = argparse.ArgumentParser(
        prog='codo-cli',
        description='CODO 开放 API 命令行（AK/SK）。一期支持 admin /api/p',
    )
    parser.add_argument('--version', action='version', version='codo-cli %s' % __version__)
    sub = parser.add_subparsers(dest='command')

    # config
    p_cfg = sub.add_parser('config', help='配置管理')
    cfg_sub = p_cfg.add_subparsers(dest='config_cmd')
    p_init = cfg_sub.add_parser('init', help='初始化 ~/.codo/config.yaml')
    p_init.add_argument('--force', action='store_true', help='覆盖已有配置')
    p_init.set_defaults(func=cmd_config_init)

    p_show = cfg_sub.add_parser('show', help='显示当前生效配置（隐藏 SK）')
    _add_global_auth_args(p_show)
    p_show.set_defaults(func=cmd_config_show)

    p_path = cfg_sub.add_parser('path', help='打印配置文件路径')
    p_path.set_defaults(func=cmd_config_path)

    # api request
    p_api = sub.add_parser('api', help='通用 HTTP 请求')
    api_sub = p_api.add_subparsers(dest='api_cmd')
    p_req = api_sub.add_parser('request', help='签名请求 METHOD PATH')
    p_req.add_argument('method', help='GET/POST/PUT/PATCH/DELETE')
    p_req.add_argument('path', help='网关 path，如 /api/p/v4/biz/list/')
    p_req.add_argument(
        '-p', '--param', action='append', default=[], help='query: key=value，可多次'
    )
    p_req.add_argument(
        '-d',
        '--data',
        default=None,
        help='JSON body 或 @file.json；写操作需 --yes',
    )
    p_req.add_argument(
        '-y', '--yes', action='store_true', help='确认执行写操作'
    )
    _add_global_auth_args(p_req)
    p_req.set_defaults(func=cmd_api_request)

    # admin
    p_adm = sub.add_parser('admin', help='codo-admin API')
    adm_sub = p_adm.add_subparsers(dest='admin_cmd')

    p_list = adm_sub.add_parser('list', help='列出 AdminV4APIS 已声明接口')
    p_list.add_argument('--filter', default=None, help='按名称/描述/url 过滤')
    p_list.add_argument('--pretty', action='store_true')
    p_list.add_argument('--quiet', action='store_true', help='只打印 API 名')
    p_list.set_defaults(func=cmd_admin_list)

    p_call = adm_sub.add_parser('call', help='按 API 名调用，如 get_biz_list')
    p_call.add_argument('name', help='AdminV4APIS 属性名')
    p_call.add_argument('--method', default=None, help='覆盖 method')
    p_call.add_argument(
        '-p', '--param', action='append', default=[], help='query: key=value'
    )
    p_call.add_argument('-d', '--data', default=None, help='JSON body 或 @file')
    p_call.add_argument('-y', '--yes', action='store_true', help='确认写操作')
    _add_global_auth_args(p_call)
    p_call.set_defaults(func=cmd_admin_call)

    # sugar
    p_ul = adm_sub.add_parser('user-list', help='用户列表（get_user_list）')
    p_ul.add_argument('--search', default=None, help='searchVal')
    p_ul.add_argument('-p', '--param', action='append', default=[])
    p_ul.add_argument('-y', '--yes', action='store_true')
    _add_global_auth_args(p_ul)
    p_ul.set_defaults(func=cmd_admin_user_list)

    p_bl = adm_sub.add_parser('biz-list', help='业务列表（get_biz_list）')
    p_bl.add_argument('-p', '--param', action='append', default=[])
    p_bl.add_argument('-y', '--yes', action='store_true')
    _add_global_auth_args(p_bl)
    p_bl.set_defaults(func=cmd_admin_biz_list)

    p_rl = adm_sub.add_parser('role-base-list', help='基础角色列表')
    p_rl.add_argument('-p', '--param', action='append', default=[])
    p_rl.add_argument('-y', '--yes', action='store_true')
    _add_global_auth_args(p_rl)
    p_rl.set_defaults(func=cmd_admin_role_base_list)

    return parser


def main(argv=None):
    parser = build_parser()
    ns = parser.parse_args(argv)
    if not getattr(ns, 'func', None):
        parser.print_help()
        return 2
    try:
        return int(ns.func(ns) or 0)
    except KeyboardInterrupt:
        return 130
    except SystemExit as e:
        # build_client 等
        if e.code is None:
            return 0
        if isinstance(e.code, int):
            return e.code
        print(e.code, file=sys.stderr)
        return 2
    except Exception as e:
        print('error: %s' % e, file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())