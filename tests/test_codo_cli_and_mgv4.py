# -*- coding: utf-8 -*-
"""codo-cli 与 AdminV4APIS 兼容性 / 单元测试（不访问真实网关）。"""

import json
import os
import sys
import tempfile

import pytest


def test_legacy_admin_api_attrs_exist():
    """无 break change：历史属性名必须保留。"""
    from websdk2.apis.mgv4_apis import AdminV4APIS

    legacy = [
        'route_prefix',
        'get_user_list',
        'get_user_contact_info',
        'get_users',
        'opt_users',
        'get_biz',
        'get_biz_list',
        'get_normal_role_list',
        'get_all_base_role_list',
        'get_all_role_user_v4',
        'get_all_roles_users',
        'get_favorites_v4',
        'opt_favorites_v4',
    ]
    for name in legacy:
        assert hasattr(AdminV4APIS, name), name
    assert AdminV4APIS.route_prefix == '/api/p'
    assert AdminV4APIS.get_biz_list['url'] == '/api/p/v4/biz/list/'
    assert AdminV4APIS.get_biz_list['method'] == 'GET'


def test_new_admin_apis_and_list():
    from websdk2.apis.mgv4_apis import AdminV4APIS

    assert AdminV4APIS.get_openapi_accounts['url'].endswith('/v4/openapi/accounts/')
    assert AdminV4APIS.get_func_list['method'] == 'GET'
    items = AdminV4APIS.list_apis()
    names = {i['name'] for i in items}
    assert 'get_biz_list' in names
    assert 'get_openapi_credentials' in names
    assert len(items) >= 40
    api = AdminV4APIS.get_api('get_biz_list')
    assert api['url'] == '/api/p/v4/biz/list/'
    # 拷贝隔离
    api['params'] = {'x': 1}
    assert AdminV4APIS.get_biz_list.get('params') != {'x': 1}


def test_cli_help_and_list():
    from codo_cli.main import main
    import pytest

    with pytest.raises(SystemExit) as ei:
        main(['--help'])
    assert ei.value.code in (0, None)

    rc = main(['admin', 'list', '--quiet'])
    assert rc == 0


def test_cli_admin_list_filter(capsys):
    from codo_cli.main import main

    rc = main(['admin', 'list', '--filter', 'openapi', '--pretty'])
    assert rc == 0
    out = capsys.readouterr().out
    assert 'openapi' in out.lower()


def test_write_requires_yes(capsys):
    from codo_cli.main import main

    rc = main(['api', 'request', 'POST', '/api/p/v4/user/', '-d', '{}'])
    assert rc == 2
    err = capsys.readouterr().err
    assert '--yes' in err or '确认' in err


def test_config_init_and_no_secret_on_disk(monkeypatch, tmp_path):
    from codo_cli import config as conf

    monkeypatch.setattr(conf, 'CONFIG_DIR', str(tmp_path / '.codo'))
    monkeypatch.setattr(conf, 'CONFIG_PATH', str(tmp_path / '.codo' / 'config.yaml'))
    path, created = conf.init_config(force=True)
    assert created
    assert os.path.isfile(path)
    text = open(path, encoding='utf-8').read()
    assert 'secret_key' not in text or text.count('secret_key') == 0 or '禁止' in text or 'do not store' in text
    # 即使 doc 带 secret 也不应写出
    doc = conf.load_raw_config()
    doc['profiles']['default']['secret_key'] = 'SHOULD_NOT_SAVE'
    conf.save_raw_config(doc)
    text2 = open(path, encoding='utf-8').read()
    assert 'SHOULD_NOT_SAVE' not in text2

    monkeypatch.setenv('CODO_SECRET_KEY', 'sk-test-value')
    monkeypatch.setenv('CODO_ACCESS_KEY', 'ak-test')
    monkeypatch.setenv('CODO_ENDPOINT', 'https://gw.test')
    s = conf.resolve_settings()
    assert s['secret_key'] == 'sk-test-value'
    assert s['access_key'] == 'ak-test'
    view = conf.public_settings_view(s)
    assert 'sk-test-value' not in json.dumps(view)


def test_merge_api_spec():
    from codo_cli.client import merge_api_spec

    spec = {
        'method': 'GET',
        'url': '/api/p/v4/user/list/',
        'params': {'page': 1},
    }
    req = merge_api_spec(spec, param_overrides={'searchVal': 'a'})
    assert req['params']['searchVal'] == 'a'
    assert req['params']['page'] == 1
