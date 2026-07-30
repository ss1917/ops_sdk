#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
codo-k2 配置中心 API 目录（网关前缀 /api/k2）

codo-k2 是配置中心 V2 新项目，与老项目 kerrigan（/api/kerrigan，KerriganAPIS）分离。
由服务路由自动补全，供 OpenAPIClient / codo-cli 使用。
"""


class K2APIS:
    route_prefix = "/api/k2"
    # 显式标注：非 kerrigan
    service = "codo-k2"

    post_public_v1_project_config_approval_agree = dict(
        method='POST',
        url='/api/k2/public/v1/project/config/approval/agree/',
        params={},
        description='配置中心-配置版本-审批同意 [POST]',
    )

    post_public_v1_project_config_approval_reject = dict(
        method='POST',
        url='/api/k2/public/v1/project/config/approval/reject/',
        params={},
        description='配置中心-配置版本-审批驳回 [POST]',
    )

    post_public_v1_project_config_deletion_audit_agree = dict(
        method='POST',
        url='/api/k2/public/v1/project/config/deletion_audit/agree/',
        params={},
        description='配置中心-配置删除-审核同意 [POST]',
    )

    post_public_v1_project_config_deletion_audit_reject = dict(
        method='POST',
        url='/api/k2/public/v1/project/config/deletion_audit/reject/',
        params={},
        description='配置中心-配置删除-审核驳回 [POST]',
    )

    get_public_v1_project_published_shared_all_config = dict(
        method='GET',
        url='/api/k2/public/v1/project/published/shared/all/config/',
        params={},
        description='配置中心-已发布项目配置 [GET]',
    )

    get_public_v1_project_published_shared_config = dict(
        method='GET',
        url='/api/k2/public/v1/project/published/shared/config/',
        params={},
        description='配置中心-已发布配置 [GET]',
    )

    get_public_v1_project_published_shared_service_config = dict(
        method='GET',
        url='/api/k2/public/v1/project/published/shared/service/config/',
        params={},
        description='配置中心-已发布服务 [GET]',
    )

    get_v1_healthy = dict(
        method='GET',
        url='/api/k2/v1/healthy/',
        params={},
        description='配置中心-健康检查 [GET]',
    )

    get_v1_project = dict(
        method='GET',
        url='/api/k2/v1/project/',
        params={},
        description='配置中心-项目管理',
    )

    post_v1_project_approval = dict(
        method='POST',
        url='/api/k2/v1/project/approval/',
        params={},
        description='配置中心-审批配置管理 [POST]',
    )

    put_v1_project_approval = dict(
        method='PUT',
        url='/api/k2/v1/project/approval/',
        params={},
        description='配置中心-审批配置管理 [PUT]',
    )

    get_v1_project_approval = dict(
        method='GET',
        url='/api/k2/v1/project/approval/',
        params={},
        description='配置中心-审批配置管理 [GET]',
    )

    get_v1_project_approval_detail = dict(
        method='GET',
        url='/api/k2/v1/project/approval/detail/',
        params={},
        description='配置中心-审批配置-查看详情 [GET]',
    )

    get_v1_project_config = dict(
        method='GET',
        url='/api/k2/v1/project/config/',
        params={},
        description='配置中心-项目配置管理',
    )

    get_v1_project_config_deletion_audit = dict(
        method='GET',
        url='/api/k2/v1/project/config/deletion_audit/',
        params={},
        description='配置中心-配置删除-审核列表 [GET]',
    )

    post_v1_project_config_deletion_audit = dict(
        method='POST',
        url='/api/k2/v1/project/config/deletion_audit/',
        params={},
        description='配置中心-配置删除-审核列表 [POST]',
    )

    get_v1_project_config_detail = dict(
        method='GET',
        url='/api/k2/v1/project/config/detail/',
        params={},
        description='配置中心-项目配置-查看详情 [GET]',
    )

    get_v1_project_config_version = dict(
        method='GET',
        url='/api/k2/v1/project/config/version/',
        params={},
        description='配置中心-配置版本 [GET]',
    )

    post_v1_project_config_version_rollback = dict(
        method='POST',
        url='/api/k2/v1/project/config/version/rollback/',
        params={},
        description='配置中心-配置版本-回滚 [POST]',
    )

    get_v1_project_detail = dict(
        method='GET',
        url='/api/k2/v1/project/detail/',
        params={},
        description='配置中心-项目管理-查看详情 [GET]',
    )

    post_v1_project_etcd = dict(
        method='POST',
        url='/api/k2/v1/project/etcd/',
        params={},
        description='配置中心-关联ETCD [POST]',
    )

    put_v1_project_etcd = dict(
        method='PUT',
        url='/api/k2/v1/project/etcd/',
        params={},
        description='配置中心-关联ETCD [PUT]',
    )

    get_v1_project_etcd_detail = dict(
        method='GET',
        url='/api/k2/v1/project/etcd/detail/',
        params={},
        description='配置中心-关联ETCD-查看详情 [GET]',
    )

    get_v1_project_published_all_config = dict(
        method='GET',
        url='/api/k2/v1/project/published/all/config/',
        params={},
        description='配置中心-所有已发布配置 [GET]',
    )

    get_v1_project_published_config = dict(
        method='GET',
        url='/api/k2/v1/project/published/config/',
        params={},
        description='配置中心-已发布配置 [GET]',
    )

    get_v1_project_published_service_config = dict(
        method='GET',
        url='/api/k2/v1/project/published/service/config/',
        params={},
        description='配置中心-已发布服务 [GET]',
    )

    get_v1_project_published_shared_all_config_url = dict(
        method='GET',
        url='/api/k2/v1/project/published/shared/all/config/url/',
        params={},
        description='配置中心-已发布项目配置地址 [GET]',
    )

    get_v1_project_published_shared_config_url = dict(
        method='GET',
        url='/api/k2/v1/project/published/shared/config/url/',
        params={},
        description='配置中心-已发布配置地址 [GET]',
    )

    get_v1_project_published_shared_service_config_url = dict(
        method='GET',
        url='/api/k2/v1/project/published/shared/service/config/url/',
        params={},
        description='配置中心-已发布服务地址 [GET]',
    )

    @classmethod
    def list_apis(cls):
        items = []
        for name in sorted(dir(cls)):
            if name.startswith('_'):
                continue
            val = getattr(cls, name)
            if not isinstance(val, dict) or 'url' not in val:
                continue
            items.append({
                'name': name,
                'method': val.get('method'),
                'url': val.get('url'),
                'description': val.get('description') or '',
            })
        return items

    @classmethod
    def get_api(cls, name):
        if not name or name.startswith('_'):
            return None
        val = getattr(cls, name, None)
        if not isinstance(val, dict) or 'url' not in val:
            return None
        out = dict(val)
        if isinstance(out.get('params'), dict):
            out['params'] = dict(out['params'])
        if isinstance(out.get('body'), dict):
            out['body'] = dict(out['body'])
        return out
