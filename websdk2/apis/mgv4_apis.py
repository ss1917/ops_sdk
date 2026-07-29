#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018年2月5日13:37:54
Desc    ：记录API
"""


class AdminV4APIS:
    route_prefix = "/api/p"

    # ---------- 用户 ----------
    get_user_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/user/list/',
        params={'page': 1, 'limit': 201},
        field_help={},
        description='查看用户列表',
    )

    get_user_contact_info = dict(
        method='GET',
        url=f'{route_prefix}/v4/user/send_addr/',
        params={},
        field_help={
            'users_str': '用户id/用户名/昵称，半角逗号分隔',
            'roles_str': '角色id，半角逗号分隔',
        },
        description='获取用户的联系方式，手机/邮箱/钉钉ID/飞书ID',
    )

    get_users = dict(
        method='GET',
        url=f'{route_prefix}/v4/user/',
        params={'page': 1, 'limit': 201},
        field_help={},
        description='管理-查看用户列表',
    )

    opt_users = dict(
        method='POST',
        url=f'{route_prefix}/v4/user/',
        body={
            'username': None,
            'nickname': None,
            'password': None,
            'department': None,
            'tel': None,
            'email': None,
            'user_state': '20',
        },
        field_help={'user_state': '20'},
        description='操作用户数据，支持增删改，请修改 method 和 body',
    )

    reset_mfa = dict(
        method='PUT',
        url=f'{route_prefix}/v4/reset_mfa/',
        body={},
        field_help={},
        description='重置用户二次认证',
    )

    reset_password = dict(
        method='PUT',
        url=f'{route_prefix}/v4/reset_pw/',
        body={},
        field_help={},
        description='重置用户密码',
    )

    # ---------- 业务 ----------
    get_biz = dict(
        method='GET',
        url=f'{route_prefix}/v4/biz/',
        params={'page': 1, 'limit': 201},
        field_help={},
        description='权限中心-业务管理',
    )

    opt_biz = dict(
        method='POST',
        url=f'{route_prefix}/v4/biz/',
        body={},
        field_help={},
        description='业务增删改，请修改 method 和 body',
    )

    get_biz_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/biz/list/',
        params={},
        field_help={},
        description='PAAS基础功能-查看业务列表和切换',
    )

    get_biz_root_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/biz/root-list/',
        params={},
        field_help={},
        description='查看根业务列表',
    )

    # ---------- 角色 ----------
    get_normal_role_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/role/list/',
        params={},
        field_help={
            'page': '分页/第几页',
            'limit': '分页/每页多少个',
            'searchVal': '模糊查询',
        },
        description='查看常规角色列表',
    )

    get_all_base_role_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/role/base_list/',
        params={},
        field_help={},
        description='查看所有基础角色',
    )

    get_roles = dict(
        method='GET',
        url=f'{route_prefix}/v4/role/',
        params={'page_number': 1, 'page_size': 50},
        field_help={'role_type': 'normal|base'},
        description='角色管理-列表',
    )

    opt_roles = dict(
        method='POST',
        url=f'{route_prefix}/v4/role/',
        body={},
        field_help={},
        description='角色增删改，请修改 method 和 body',
    )

    sync_role = dict(
        method='POST',
        url=f'{route_prefix}/v4/role/sync/',
        body={},
        field_help={},
        description='角色权限同步/刷新缓存',
    )

    get_role_user = dict(
        method='GET',
        url=f'{route_prefix}/v4/role_user/',
        params={},
        field_help={'role_id': '角色ID'},
        description='查看角色关联用户',
    )

    opt_role_user = dict(
        method='POST',
        url=f'{route_prefix}/v4/role_user/',
        body={},
        field_help={},
        description='角色用户关联操作',
    )

    get_all_role_user_v4 = dict(
        method='GET',
        url=f'{route_prefix}/v4/all_role_user/',
        params={},
        field_help={},
        description='获取所有角色和角色内用户信息-待废弃',
    )

    get_all_roles_users = dict(
        method='GET',
        url=f'{route_prefix}/v4/all_roles_users/',
        params={},
        field_help={},
        description='获取所有角色和角色内用户信息',
    )

    # ---------- 接口权限 / 功能 ----------
    get_funcs = dict(
        method='GET',
        url=f'{route_prefix}/v4/func/',
        params={'page_number': 1, 'page_size': 50},
        field_help={},
        description='接口权限管理-列表',
    )

    opt_funcs = dict(
        method='POST',
        url=f'{route_prefix}/v4/func/',
        body={},
        field_help={},
        description='接口权限增删改',
    )

    get_func_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/func/list/',
        params={},
        field_help={},
        description='查看接口权限列表',
    )

    get_role_func = dict(
        method='GET',
        url=f'{route_prefix}/v4/role_func/',
        params={},
        field_help={'role_id': '角色ID'},
        description='角色-接口权限关联查询',
    )

    opt_role_func = dict(
        method='POST',
        url=f'{route_prefix}/v4/role_func/',
        body={},
        field_help={},
        description='角色-接口权限关联操作',
    )

    # ---------- 菜单 ----------
    get_menus = dict(
        method='GET',
        url=f'{route_prefix}/v4/menus/',
        params={},
        field_help={},
        description='菜单管理',
    )

    opt_menus = dict(
        method='POST',
        url=f'{route_prefix}/v4/menus/',
        body={},
        field_help={},
        description='菜单增删改',
    )

    get_menu_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/menus/list/',
        params={},
        field_help={},
        description='查看菜单列表',
    )

    get_role_menu = dict(
        method='GET',
        url=f'{route_prefix}/v4/role_menu/',
        params={},
        field_help={'role_id': '角色ID'},
        description='角色-菜单关联',
    )

    opt_role_menu = dict(
        method='POST',
        url=f'{route_prefix}/v4/role_menu/',
        body={},
        field_help={},
        description='角色-菜单关联操作',
    )

    # ---------- 组件 ----------
    get_components = dict(
        method='GET',
        url=f'{route_prefix}/v4/components/',
        params={},
        field_help={},
        description='组件管理',
    )

    opt_components = dict(
        method='POST',
        url=f'{route_prefix}/v4/components/',
        body={},
        field_help={},
        description='组件增删改',
    )

    get_comp_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/comp/list/',
        params={},
        field_help={},
        description='查看组件列表',
    )

    get_role_comp = dict(
        method='GET',
        url=f'{route_prefix}/v4/role_comp/',
        params={},
        field_help={'role_id': '角色ID'},
        description='角色-组件关联',
    )

    opt_role_comp = dict(
        method='POST',
        url=f'{route_prefix}/v4/role_comp/',
        body={},
        field_help={},
        description='角色-组件关联操作',
    )

    # ---------- 应用 ----------
    get_apps = dict(
        method='GET',
        url=f'{route_prefix}/v4/apps/',
        params={},
        field_help={},
        description='应用管理',
    )

    opt_apps = dict(
        method='POST',
        url=f'{route_prefix}/v4/apps/',
        body={},
        field_help={},
        description='应用增删改',
    )

    get_apps_list = dict(
        method='GET',
        url=f'{route_prefix}/v4/apps/list/',
        params={},
        field_help={},
        description='查看应用列表(待删除接口)',
    )

    get_role_app = dict(
        method='GET',
        url=f'{route_prefix}/v4/role_app/',
        params={},
        field_help={'role_id': '角色ID'},
        description='角色-应用关联',
    )

    opt_role_app = dict(
        method='POST',
        url=f'{route_prefix}/v4/role_app/',
        body={},
        field_help={},
        description='角色-应用关联操作',
    )

    # ---------- 令牌 / 登录链接 ----------
    get_tokens = dict(
        method='GET',
        url=f'{route_prefix}/v4/token/',
        params={},
        field_help={},
        description='长期令牌列表',
    )

    opt_tokens = dict(
        method='POST',
        url=f'{route_prefix}/v4/token/',
        body={},
        field_help={},
        description='长期令牌操作',
    )

    get_login_links = dict(
        method='GET',
        url=f'{route_prefix}/v4/login/link/',
        params={},
        field_help={},
        description='免密登录链接管理-列表',
    )

    opt_login_links = dict(
        method='POST',
        url=f'{route_prefix}/v4/login/link/',
        body={},
        field_help={},
        description='免密登录链接增删改',
    )

    # ---------- 开放 API（超管） ----------
    get_openapi_accounts = dict(
        method='GET',
        url=f'{route_prefix}/v4/openapi/accounts/',
        params={'page_number': 1, 'page_size': 50},
        field_help={},
        description='开放API账号列表',
    )

    opt_openapi_accounts = dict(
        method='POST',
        url=f'{route_prefix}/v4/openapi/accounts/',
        body={'name': None, 'details': ''},
        field_help={},
        description='开放API账号创建/修改/启停/删除',
    )

    get_openapi_account_roles = dict(
        method='GET',
        url=f'{route_prefix}/v4/openapi/accounts/roles/',
        params={},
        field_help={'account_id': '账号ID'},
        description='开放API账号已绑角色',
    )

    bind_openapi_account_roles = dict(
        method='POST',
        url=f'{route_prefix}/v4/openapi/accounts/roles/',
        body={'account_id': None, 'role_ids': []},
        field_help={},
        description='开放API账号绑定基础角色',
    )

    get_openapi_credentials = dict(
        method='GET',
        url=f'{route_prefix}/v4/openapi/credentials/',
        params={},
        field_help={'account_id': '账号ID'},
        description='开放API密钥列表',
    )

    opt_openapi_credentials = dict(
        method='POST',
        url=f'{route_prefix}/v4/openapi/credentials/',
        body={'account_id': None},
        field_help={},
        description='开放API密钥创建/启停/删除',
    )

    # ---------- IdP / 组织 ----------
    get_idp_department_tree = dict(
        method='GET',
        url=f'{route_prefix}/v4/idp/department/tree/',
        params={},
        field_help={},
        description='身份提供商部门树',
    )

    get_role_idp_department = dict(
        method='GET',
        url=f'{route_prefix}/v4/role/idp_department/',
        params={},
        field_help={'role_id': '角色ID'},
        description='角色绑定的 IdP 部门',
    )

    opt_role_idp_department = dict(
        method='POST',
        url=f'{route_prefix}/v4/role/idp_department/',
        body={},
        field_help={},
        description='角色绑定 IdP 部门',
    )

    # ---------- 系统 / 审计 / 首页 ----------
    get_opt_log = dict(
        method='GET',
        url=f'{route_prefix}/v4/app/opt_log/',
        params={},
        field_help={},
        description='操作审计日志',
    )

    get_ops_step_service = dict(
        method='GET',
        url=f'{route_prefix}/v4/ops-step-service/',
        params={},
        field_help={},
        description='首页步骤管理',
    )

    opt_ops_step_service = dict(
        method='POST',
        url=f'{route_prefix}/v4/ops-step-service/',
        body={},
        field_help={},
        description='首页步骤增删改',
    )

    get_ops_service_categories = dict(
        method='GET',
        url=f'{route_prefix}/v4/ops-service-categories/',
        params={},
        field_help={},
        description='首页服务分类',
    )

    opt_ops_service_categories = dict(
        method='POST',
        url=f'{route_prefix}/v4/ops-service-categories/',
        body={},
        field_help={},
        description='首页服务分类增删改',
    )

    get_ops_index_service = dict(
        method='GET',
        url=f'{route_prefix}/v4/ops-index-service/',
        params={},
        field_help={},
        description='首页服务管理',
    )

    opt_ops_index_service = dict(
        method='POST',
        url=f'{route_prefix}/v4/ops-index-service/',
        body={},
        field_help={},
        description='首页服务增删改',
    )

    # ---------- 收藏 ----------
    get_favorites_v4 = dict(
        method='GET',
        url=f'{route_prefix}/v4/favorites/',
        params={},
        field_help={},
        description='PAAS-基础功能-公用收藏接口-查看',
    )

    opt_favorites_v4 = dict(
        method='POST',
        url=f'{route_prefix}/v4/favorites/',
        body={'key': '', 'app_code': 'overall', 'value': {}},
        field_help={},
        description='PAAS-基础功能-公用收藏接口-添加修改',
    )

    # ---------- 存储 / CDN ----------
    storage_file_private = dict(
        method='POST',
        url=f'{route_prefix}/v4/storage/file/private/',
        body={},
        field_help={},
        description='私有文件存储',
    )

    storage_cos_private = dict(
        method='POST',
        url=f'{route_prefix}/v4/storage/cos/private/',
        body={},
        field_help={},
        description='COS 私有存储',
    )

    storage_file_public = dict(
        method='GET',
        url=f'{route_prefix}/v4/storage/file/public/',
        params={},
        field_help={},
        description='公共读文件存储',
    )

    cdn_auth = dict(
        method='GET',
        url=f'{route_prefix}/v4/cdn/auth/',
        params={},
        field_help={},
        description='CDN 鉴权',
    )

    @classmethod
    def list_apis(cls):
        """返回可调用的 API 名与描述（排除内部/非 dict 属性）。"""
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
    def get_api(cls, name: str):
        if not name or name.startswith('_'):
            return None
        val = getattr(cls, name, None)
        if not isinstance(val, dict) or 'url' not in val:
            return None
        # 浅拷贝，避免调用方改到类属性
        out = dict(val)
        if 'params' in out and isinstance(out['params'], dict):
            out['params'] = dict(out['params'])
        if 'body' in out and isinstance(out['body'], dict):
            out['body'] = dict(out['body'])
        return out
