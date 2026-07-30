# -*- coding: utf-8 -*-
def test_cmdb_legacy_and_prefix():
    from websdk2.apis.cmdb_apis import CMDBAPIS
    assert CMDBAPIS.cmdb_prefix == '/api/cmdb' or CMDBAPIS.route_prefix == '/api/cmdb'
    assert CMDBAPIS.get_tag_list['url'].startswith('/api/cmdb/')
    assert CMDBAPIS.get_service_tree['method'] == 'GET'
    assert len(CMDBAPIS.list_apis()) >= 50


def test_k2_prefix():
    from websdk2.apis.k2_apis import K2APIS
    assert K2APIS.route_prefix == '/api/k2'
    items = K2APIS.list_apis()
    assert len(items) >= 10
    assert all(i['url'].startswith('/api/k2/') for i in items)


def test_kerrigan_v1_separate_from_k2():
    """kerrigan=V1 老项目 /api/kerrigan；k2=V2 新项目 /api/k2，不可混用。"""
    from websdk2.apis.kerrigan_apis import KerriganAPIS
    from websdk2.apis.k2_apis import K2APIS

    assert hasattr(KerriganAPIS, 'get_publish_config')
    assert KerriganAPIS.kerrigan_prefix == '/api/kerrigan'
    assert KerriganAPIS.get_publish_config['url'].startswith('/api/kerrigan/')
    assert K2APIS.route_prefix == '/api/k2'
    # 不是继承关系
    assert not issubclass(KerriganAPIS, K2APIS)


def test_cnmp_prefix():
    from websdk2.apis.cnmp_apis import CNMPAPIS
    assert CNMPAPIS.route_prefix == '/api/cnmp'
    items = CNMPAPIS.list_apis()
    assert len(items) >= 50
    assert any('/api/cnmp/api/v1/' in i['url'] for i in items)


def test_iris_prefix():
    from websdk2.apis.iris_apis import IrisAPIS
    assert IrisAPIS.route_prefix == '/api/iris'
    items = IrisAPIS.list_apis()
    assert len(items) >= 50
    assert any(i['url'].startswith('/api/iris/') for i in items)


def test_service_registry():
    from websdk2.apis import get_service_api_class
    from websdk2.apis.k2_apis import K2APIS
    from websdk2.apis.kerrigan_apis import KerriganAPIS

    for s in ('admin', 'cmdb', 'k2', 'cnmp', 'iris', 'kerrigan'):
        assert get_service_api_class(s) is not None
    assert get_service_api_class('k2') is K2APIS
    assert get_service_api_class('kerrigan') is KerriganAPIS
    assert get_service_api_class('k2') is not get_service_api_class('kerrigan')


def test_cli_svc_list():
    from codo_cli.main import main
    for s in ('admin', 'cmdb', 'k2', 'kerrigan', 'cnmp', 'iris'):
        assert main([s, 'list', '--quiet']) == 0
