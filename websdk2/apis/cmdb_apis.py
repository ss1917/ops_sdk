#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
codo-cmdb API 目录（网关前缀 /api/cmdb）
由服务路由自动补全，供 OpenAPIClient / codo-cli 使用。
"""


class CMDBAPIS:
    route_prefix = "/api/cmdb"
    cmdb_prefix = "/api/cmdb"  # 兼容旧字段名

    get_tag_list = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tag/list/',
        params={'page_number': '1', 'page_size': '200', 'tag_key': None},
        description='CMDB 获取标签key、value列表',
    )

    get_service_tree = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/',
        params={'biz_id': '0'},
        description='获取当前业务服务树',
    )

    get_dynamic_groups = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/dynamic_group/list/',
        params={'biz_id': ''},
        description='获取当前业务下动态分组',
    )

    get_dynamic_group_details = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/dynamic_group/preview/',
        params={},
        description='获取动态分组详细数据',
    )

    get_tree_asset_server = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/asset/server',
        params={},
        description='根据业务获取资源信息',
    )

    get_tree_asset_server_old = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/asset/',
        params={},
        description='根据业务获取资源信息，待废弃',
    )

    get_agent = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/agent/',
        params={},
        description='配置平台-资源管理-agent',
    )

    post_agent_batch_add_server = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/agent/batch_add_server/',
        params={},
        description='配置平台-资源管理-agent批量生成主机 [POST]',
    )

    get_are_you_ok = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/are_you_ok/',
        params={},
        description='/api/v2/cmdb/are_you_ok/',
    )

    get_audit_list = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/audit/list/',
        params={},
        description='配置平台-审计日志 [GET]',
    )

    get_biz = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/',
        params={},
        description='配置平台-业务-业务列表 [GET]',
    )

    get_biz_dynamic_group = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/dynamic_group/',
        params={},
        description='配置平台-业务-动态分组管理',
    )

    get_biz_perm_group = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/perm_group/',
        params={},
        description='配置平台-业务-权限分组管理',
    )

    get_biz_perm_group_preview = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/perm_group/preview/',
        params={},
        description='配置平台-业务-权限分组预览 [GET]',
    )

    post_biz_perm_group_sync = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/biz/perm_group/sync/',
        params={},
        description='配置平台-业务-权限分组同步 [POST]',
    )

    get_biz_set_temp = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/set_temp/',
        params={},
        description='配置平台-业务-集群模板',
    )

    get_biz_set_temp_batch = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/biz/set_temp/batch/',
        params={},
        description='配置平台-业务-批量使用集群模板',
    )

    get_cloud_billing_conf = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud/billing/conf/',
        params={},
        description='配置平台-云厂商-账单巡检',
    )

    get_cloud_conf = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud/conf/',
        params={},
        description='配置平台-多云配置',
    )

    get_cloud_sync = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud/sync/',
        params={},
        description='配置平台-多云配置-资产同步',
    )

    get_cloud_sync_log = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud/sync/log/',
        params={},
        description='配置平台-多云配置-查看同步日志 [GET]',
    )

    get_cloud_region = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud_region/',
        params={},
        description='配置平台-业务-云区域管理',
    )

    get_cloud_region_list = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud_region/list/',
        params={},
        description='配置平台-业务-云区域查看 [GET]',
    )

    get_cloud_region_preview = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud_region/preview/',
        params={},
        description='配置平台-业务-云区域主机预览 [GET]',
    )

    get_cloud_region_pro = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/cloud_region/pro/',
        params={},
        description='配置平台-业务-云区域管理解绑反查',
    )

    get_console_link = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/console/link/',
        params={},
        description='控制台链接查询 [GET]',
    )

    get_consul_instance = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/consul/instance/',
        params={},
        description='配置平台-监控-consul发现管理',
    )

    get_consul_service = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/consul/service/',
        params={},
        description='配置平台-监控-consul服务列表',
    )

    get_dns_domain = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/dns/domain/',
        params={},
        description='配置平台-DNS-域名管理',
    )

    get_dns_logs = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/dns/logs/',
        params={},
        description='配置平台-DNS-日志 [GET]',
    )

    get_dns_record = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/dns/record/',
        params={},
        description='配置平台-DNS-记录',
    )

    post_dns_remark = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/dns/remark/',
        params={},
        description='配置平台-DNS-说明文档 [POST]',
    )

    post_dns_sync = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/dns/sync/',
        params={},
        description='配置平台-DNS-同步 [POST]',
    )

    get_dynamic_rule = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/dynamic_rule/',
        params={},
        description='配置平台-业务-动态规则管理',
    )

    get_dynamic_rule_pro = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/dynamic_rule/pro/',
        params={},
        description='配置平台-业务-动态规则-预览变更,更新,删除关联',
    )

    get_events_aliyun = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/events/aliyun/',
        params={},
        description='配置平台-云商-事件管理-阿里云',
    )

    get_events_aws = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/events/aws/',
        params={},
        description='配置平台-云商-事件管理-AWS',
    )

    get_events_qcloud = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/events/qcloud/',
        params={},
        description='配置平台-云商-事件管理-腾讯云',
    )

    get_general_asset = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/general/asset/',
        params={},
        description='配置平台-通用资产管理',
    )

    post_general_asset_upsert = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/general/asset/upsert/',
        params={},
        description='配置平台-通用资产Upsert [POST]',
    )

    get_img = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/img/',
        params={},
        description='配置平台-云商-系统镜像管理',
    )

    get_img_list = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/img/list/',
        params={},
        description='配置平台-云商-系统镜像列表 [GET]',
    )

    get_jms_orgs_list = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/jms/orgs/list/',
        params={},
        description='配置平台-堡垒机组织列表 [GET]',
    )

    get_k8s_cluster = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/k8s/cluster/',
        params={},
        description='配置平台-云商-集群管理',
    )

    get_lb = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/lb/',
        params={},
        description='配置平台-云商-LB管理',
    )

    get_mongodb = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/mongodb/',
        params={},
        description='配置平台-云商-MongoDB管理',
    )

    get_mysql = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/mysql/',
        params={},
        description='配置平台-云商-MySQL管理',
    )

    get_nat = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/nat/',
        params={},
        description='配置平台-云商-NAT管理',
    )

    post_order_buy = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/order/buy/',
        params={},
        description='CMDB-资源采购-资源购买 [POST]',
    )

    post_order_callback = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/order/callback/',
        params={},
        description='CMDB-资源采购-资源购买后回调 [POST]',
    )

    get_order_info = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/order/info/',
        params={},
        description='CMDB-资源采购-采购列表',
    )

    post_order_query_cloud_bandwidth_pkg = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/order/query_cloud/bandwidth_pkg/',
        params={},
        description='CMDB-资源采购-带宽包 [POST]',
    )

    post_order_query_cloud_ins_type = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/order/query_cloud/ins_type/',
        params={},
        description='CMDB-资源采购-获取实例类型 [POST]',
    )

    post_order_query_cloud_price = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/order/query_cloud/price/',
        params={},
        description='CMDB-资源采购-获取实例价格 [POST]',
    )

    get_order_template = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/order/template/',
        params={},
        description='CMDB-资源采购-模板管理',
    )

    get_redis = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/redis/',
        params={},
        description='配置平台-云商-Redis管理',
    )

    get_role = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/role/',
        params={},
        description='配置平台-角色列表 [GET]',
    )

    get_search = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/search/',
        params={},
        description='配置平台-基础功能-统一查询 [GET]',
    )

    get_secret = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/secret/',
        params={},
        description='配置平台-欢乐剑-密钥',
    )

    get_security_group = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/security_group/',
        params={},
        description='配置平台-云商安全组管理',
    )

    get_security_group_refs = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/security_group/refs/',
        params={},
        description='配置平台-云商安全组关联信息',
    )

    get_server = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/server/',
        params={},
        description='配置平台-云商-主机管理',
    )

    get_server_batch = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/server/batch/',
        params={},
        description='配置平台-云商-主机批量管理',
    )

    post_server_main_agent = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/server/main_agent/',
        params={},
        description='配置平台-云商-主机绑定主Agent [POST]',
    )

    post_server_upsert = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/server/upsert/',
        params={},
        description='配置平台-云商-主机upsert [POST]',
    )

    get_switch = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/switch/',
        params={},
        description='配置平台-内网-交换机管理 [GET]',
    )

    post_switch_import = dict(
        method='POST',
        url='/api/cmdb/api/v2/cmdb/switch/import/',
        params={},
        description='配置平台-内网-交换机导入 [POST]',
    )

    get_tag = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tag/',
        params={},
        description='配置平台-业务-标签管理',
    )

    get_tag_asset_detail = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tag/asset_detail/',
        params={},
        description='配置平台-业务-标签资产关系详细信息 [GET]',
    )

    get_tag_asset_id = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tag/asset_id/',
        params={},
        description='配置平台-业务-获取资产ID [GET]',
    )

    get_tree_asset_relation = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/asset/relation/',
        params={},
        description='配置平台-树-查询所在拓扑结构',
    )

    get_tree_asset_server_2 = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/asset/server/',
        params={},
        description='配置平台-树-主机资产 [GET]',
    )

    get_tree_env = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/env/',
        params={},
        description='配置平台-树-获取业务下环境列表 [GET]',
    )

    get_tree_form_env = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/form/env/',
        params={},
        description='配置平台-树-获取业务环境列表-form [GET]',
    )

    get_tree_form_module = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/form/module/',
        params={},
        description='配置平台-树-获取业务环境集群下模块列表-form [GET]',
    )

    get_tree_form_set = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/form/set/',
        params={},
        description='配置平台-树-获取业务环境下集群列表-form [GET]',
    )

    get_tree_leaf = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/leaf/',
        params={},
        description='配置平台-树-叶子处理',
    )

    get_tree_module = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/module/',
        params={},
        description='配置平台-树-获取业务环境集群下模块数据 [GET]',
    )

    get_tree_register = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/register/',
        params={},
        description='配置平台-树-数据注册-未测试',
    )

    get_tree_search_info = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/search_info/',
        params={},
        description='配置平台-服务树-查询ID [GET]',
    )

    get_tree_server_relation = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/server/relation/',
        params={},
        description='配置平台-树-根据内网IP查询关联',
    )

    get_tree_v2_register = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/tree/v2/register/',
        params={},
        description='配置平台-树-数据注册V2-未测试',
    )

    get_user_field = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/user_field/',
        params={},
        description='配置平台-基础功能-用户字段配置',
    )

    get_vpc = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/vpc/',
        params={},
        description='CMDB-云商-虚拟局域网管理',
    )

    get_vswitch = dict(
        method='GET',
        url='/api/cmdb/api/v2/cmdb/vswitch/',
        params={},
        description='CMDB-云商-虚拟子网管理',
    )

    get_v2_interface = dict(
        method='GET',
        url='/api/cmdb/api/v2/interface/',
        params={},
        description='配置平台-内部-公司网络出口',
    )

    get_cbb_area_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/area/',
        params={},
        description='配置平台-区服管理',
    )

    get_cbb_area_big_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/big_area/',
        params={},
        description='配置平台-大区管理',
    )

    get_cbb_area_big_area_detail = dict(
        method='GET',
        url='/api/cmdb/cbb_area/big_area/detail/',
        params={},
        description='配置平台-大区详情 [GET]',
    )

    get_cbb_area_env = dict(
        method='GET',
        url='/api/cmdb/cbb_area/env/',
        params={},
        description='配置平台-环境管理',
    )

    post_cbb_area_env_idip_check = dict(
        method='POST',
        url='/api/cmdb/cbb_area/env/idip/check/',
        params={},
        description='配置平台-环境列表-IDIP连通性检测 [POST]',
    )

    get_cbb_area_env_list = dict(
        method='GET',
        url='/api/cmdb/cbb_area/env/list/',
        params={},
        description='配置平台-环境列表 [GET]',
    )

    get_cbb_area_gmt_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/gmt/area/',
        params={},
        description='配置平台-区服管理-GMT专用',
    )

    get_cbb_area_gmt_big_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/gmt/big_area/',
        params={},
        description='配置平台-大区管理-GMT专用',
    )

    get_cbb_area_gmt_big_area_detail = dict(
        method='GET',
        url='/api/cmdb/cbb_area/gmt/big_area/detail/',
        params={},
        description='配置平台-大区详情-GMT专用 [GET]',
    )

    get_cbb_area_gmt_env_list = dict(
        method='GET',
        url='/api/cmdb/cbb_area/gmt/env/list/',
        params={},
        description='配置平台-环境列表-GMT环境 [GET]',
    )

    get_cbb_area_na_env_list = dict(
        method='GET',
        url='/api/cmdb/cbb_area/na/env/list/',
        params={},
        description='配置平台-免鉴权环境列表 [GET]',
    )

    get_cbb_area_without_prd_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/without_prd/area/',
        params={},
        description='配置平台-区服管理-非生产环境',
    )

    get_cbb_area_without_prd_big_area = dict(
        method='GET',
        url='/api/cmdb/cbb_area/without_prd/big_area/',
        params={},
        description='配置平台-大区管理-非生产环境',
    )

    get_cbb_area_without_prd_big_area_detail = dict(
        method='GET',
        url='/api/cmdb/cbb_area/without_prd/big_area/detail/',
        params={},
        description='配置平台-大区详情-非生产环境 [GET]',
    )

    get_cbb_area_without_prd_env_list = dict(
        method='GET',
        url='/api/cmdb/cbb_area/without_prd/env/list/',
        params={},
        description='配置平台-环境列表-非生产环境 [GET]',
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
