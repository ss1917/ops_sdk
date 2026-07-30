#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
codo-iris 集成化管理 API 目录（网关前缀 /api/iris）
由服务路由自动补全，供 OpenAPIClient / codo-cli 使用。
"""


class IrisAPIS:
    route_prefix = "/api/iris"

    post_alarm_analysis_convergence_funnel = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/convergence_funnel',
        params={},
        description='POST /api/alarm_analysis/convergence_funnel',
    )

    post_alarm_analysis_distribution = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/distribution',
        params={},
        description='POST /api/alarm_analysis/distribution',
    )

    post_alarm_analysis_process_matrix = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/process_matrix',
        params={},
        description='POST /api/alarm_analysis/process_matrix',
    )

    post_alarm_analysis_process_trend = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/process_trend',
        params={},
        description='POST /api/alarm_analysis/process_trend',
    )

    post_alarm_analysis_refresh = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/refresh',
        params={},
        description='POST /api/alarm_analysis/refresh',
    )

    post_alarm_analysis_volume_trend = dict(
        method='POST',
        url='/api/iris/api/alarm_analysis/volume_trend',
        params={},
        description='POST /api/alarm_analysis/volume_trend',
    )

    get_alarm_convergence_rule_ai_analysis = dict(
        method='GET',
        url='/api/iris/api/alarm_convergence_rule/ai_analysis',
        params={},
        description='GET /api/alarm_convergence_rule/ai_analysis',
    )

    post_alarm_convergence_rule_ai_analyze = dict(
        method='POST',
        url='/api/iris/api/alarm_convergence_rule/ai_analyze',
        params={},
        description='POST /api/alarm_convergence_rule/ai_analyze',
    )

    post_alarm_convergence_rule_delete = dict(
        method='POST',
        url='/api/iris/api/alarm_convergence_rule/delete',
        params={},
        description='POST /api/alarm_convergence_rule/delete',
    )

    get_alarm_convergence_rule_detail = dict(
        method='GET',
        url='/api/iris/api/alarm_convergence_rule/detail',
        params={},
        description='GET /api/alarm_convergence_rule/detail',
    )

    get_alarm_convergence_rule_get_by_topo_biz = dict(
        method='GET',
        url='/api/iris/api/alarm_convergence_rule/get_by_topo_biz',
        params={},
        description='GET /api/alarm_convergence_rule/get_by_topo_biz',
    )

    get_alarm_convergence_rule_list = dict(
        method='GET',
        url='/api/iris/api/alarm_convergence_rule/list',
        params={},
        description='GET /api/alarm_convergence_rule/list',
    )

    post_alarm_convergence_rule_upsert = dict(
        method='POST',
        url='/api/iris/api/alarm_convergence_rule/upsert',
        params={},
        description='POST /api/alarm_convergence_rule/upsert',
    )

    post_alarm_event_close = dict(
        method='POST',
        url='/api/iris/api/alarm_event/close',
        params={},
        description='POST /api/alarm_event/close',
    )

    get_alarm_event_detail = dict(
        method='GET',
        url='/api/iris/api/alarm_event/detail',
        params={},
        description='GET /api/alarm_event/detail',
    )

    post_alarm_event_list = dict(
        method='POST',
        url='/api/iris/api/alarm_event/list',
        params={},
        description='POST /api/alarm_event/list',
    )

    post_alarm_event_list_by_node = dict(
        method='POST',
        url='/api/iris/api/alarm_event/list_by_node',
        params={},
        description='POST /api/alarm_event/list_by_node',
    )

    post_alarm_event_manual_resolve = dict(
        method='POST',
        url='/api/iris/api/alarm_event/manual_resolve',
        params={},
        description='POST /api/alarm_event/manual_resolve',
    )

    post_alarm_event_process = dict(
        method='POST',
        url='/api/iris/api/alarm_event/process',
        params={},
        description='POST /api/alarm_event/process',
    )

    post_alarm_event_process_records = dict(
        method='POST',
        url='/api/iris/api/alarm_event/process_records',
        params={},
        description='POST /api/alarm_event/process_records',
    )

    get_alarm_event_select_option = dict(
        method='GET',
        url='/api/iris/api/alarm_event/select_option',
        params={},
        description='GET /api/alarm_event/select_option',
    )

    post_alarm_event_stats_by_level = dict(
        method='POST',
        url='/api/iris/api/alarm_event/stats_by_level',
        params={},
        description='POST /api/alarm_event/stats_by_level',
    )

    post_alarm_incident_close = dict(
        method='POST',
        url='/api/iris/api/alarm_incident/close',
        params={},
        description='POST /api/alarm_incident/close',
    )

    get_alarm_incident_detail = dict(
        method='GET',
        url='/api/iris/api/alarm_incident/detail',
        params={},
        description='GET /api/alarm_incident/detail',
    )

    post_alarm_incident_list = dict(
        method='POST',
        url='/api/iris/api/alarm_incident/list',
        params={},
        description='POST /api/alarm_incident/list',
    )

    post_alarm_incident_process = dict(
        method='POST',
        url='/api/iris/api/alarm_incident/process',
        params={},
        description='POST /api/alarm_incident/process',
    )

    post_alarm_incident_process_records = dict(
        method='POST',
        url='/api/iris/api/alarm_incident/process_records',
        params={},
        description='POST /api/alarm_incident/process_records',
    )

    post_alarm_notification_create = dict(
        method='POST',
        url='/api/iris/api/alarm_notification/create',
        params={},
        description='POST /api/alarm_notification/create',
    )

    post_alarm_notification_delete = dict(
        method='POST',
        url='/api/iris/api/alarm_notification/delete',
        params={},
        description='POST /api/alarm_notification/delete',
    )

    get_alarm_notification_detail = dict(
        method='GET',
        url='/api/iris/api/alarm_notification/detail',
        params={},
        description='GET /api/alarm_notification/detail',
    )

    get_alarm_notification_list = dict(
        method='GET',
        url='/api/iris/api/alarm_notification/list',
        params={},
        description='GET /api/alarm_notification/list',
    )

    post_alarm_notification_update = dict(
        method='POST',
        url='/api/iris/api/alarm_notification/update',
        params={},
        description='POST /api/alarm_notification/update',
    )

    post_audit_log_list = dict(
        method='POST',
        url='/api/iris/api/audit_log/list',
        params={},
        description='POST /api/audit_log/list',
    )

    get_audit_log_select_option = dict(
        method='GET',
        url='/api/iris/api/audit_log/select_option',
        params={},
        description='GET /api/audit_log/select_option',
    )

    get_cloud_bill_summary_list = dict(
        method='GET',
        url='/api/iris/api/cloud/bill_summary/list',
        params={},
        description='GET /api/cloud/bill_summary/list',
    )

    post_cloud_bill_summary_sync = dict(
        method='POST',
        url='/api/iris/api/cloud/bill_summary/sync',
        params={},
        description='POST /api/cloud/bill_summary/sync',
    )

    get_cloud_costs_detail = dict(
        method='GET',
        url='/api/iris/api/cloud/costs/detail',
        params={},
        description='GET /api/cloud/costs/detail',
    )

    get_cloud_costs_list = dict(
        method='GET',
        url='/api/iris/api/cloud/costs/list',
        params={},
        description='GET /api/cloud/costs/list',
    )

    get_cloud_costs_summary = dict(
        method='GET',
        url='/api/iris/api/cloud/costs/summary',
        params={},
        description='GET /api/cloud/costs/summary',
    )

    post_conf_template_apply = dict(
        method='POST',
        url='/api/iris/api/conf_template/apply',
        params={},
        description='POST /api/conf_template/apply',
    )

    post_conf_template_clone = dict(
        method='POST',
        url='/api/iris/api/conf_template/clone',
        params={},
        description='POST /api/conf_template/clone',
    )

    post_conf_template_create = dict(
        method='POST',
        url='/api/iris/api/conf_template/create',
        params={},
        description='POST /api/conf_template/create',
    )

    post_conf_template_delete = dict(
        method='POST',
        url='/api/iris/api/conf_template/delete',
        params={},
        description='POST /api/conf_template/delete',
    )

    get_conf_template_detail = dict(
        method='GET',
        url='/api/iris/api/conf_template/detail',
        params={},
        description='GET /api/conf_template/detail',
    )

    get_conf_template_list = dict(
        method='GET',
        url='/api/iris/api/conf_template/list',
        params={},
        description='GET /api/conf_template/list',
    )

    post_conf_template_submit_audit = dict(
        method='POST',
        url='/api/iris/api/conf_template/submit_audit',
        params={},
        description='POST /api/conf_template/submit_audit',
    )

    post_conf_template_update = dict(
        method='POST',
        url='/api/iris/api/conf_template/update',
        params={},
        description='POST /api/conf_template/update',
    )

    post_conf_template_version_audit = dict(
        method='POST',
        url='/api/iris/api/conf_template_version/audit',
        params={},
        description='POST /api/conf_template_version/audit',
    )

    get_conf_template_version_detail = dict(
        method='GET',
        url='/api/iris/api/conf_template_version/detail',
        params={},
        description='GET /api/conf_template_version/detail',
    )

    get_conf_template_version_latest_detail = dict(
        method='GET',
        url='/api/iris/api/conf_template_version/latest/detail',
        params={},
        description='GET /api/conf_template_version/latest/detail',
    )

    get_conf_template_version_list = dict(
        method='GET',
        url='/api/iris/api/conf_template_version/list',
        params={},
        description='GET /api/conf_template_version/list',
    )

    post_conf_template_version_rollback = dict(
        method='POST',
        url='/api/iris/api/conf_template_version/rollback',
        params={},
        description='POST /api/conf_template_version/rollback',
    )

    get_current_user = dict(
        method='GET',
        url='/api/iris/api/current_user',
        params={},
        description='GET /api/current_user',
    )

    get_events = dict(
        method='GET',
        url='/api/iris/api/events',
        params={},
        description='GET /api/events',
    )

    get_form_template_kind = dict(
        method='GET',
        url='/api/iris/api/form_template/kind',
        params={},
        description='GET /api/form_template/kind',
    )

    get_form_template_meta = dict(
        method='GET',
        url='/api/iris/api/form_template/meta',
        params={},
        description='GET /api/form_template/meta',
    )

    post_log_alarm_close = dict(
        method='POST',
        url='/api/iris/api/log_alarm/close',
        params={},
        description='POST /api/log_alarm/close',
    )

    get_log_alarm_detail = dict(
        method='GET',
        url='/api/iris/api/log_alarm/detail',
        params={},
        description='GET /api/log_alarm/detail',
    )

    post_log_alarm_list = dict(
        method='POST',
        url='/api/iris/api/log_alarm/list',
        params={},
        description='POST /api/log_alarm/list',
    )

    post_log_alarm_process = dict(
        method='POST',
        url='/api/iris/api/log_alarm/process',
        params={},
        description='POST /api/log_alarm/process',
    )

    post_log_alarm_process_records = dict(
        method='POST',
        url='/api/iris/api/log_alarm/process_records',
        params={},
        description='POST /api/log_alarm/process_records',
    )

    get_log_alarm_select_option = dict(
        method='GET',
        url='/api/iris/api/log_alarm/select_option',
        params={},
        description='GET /api/log_alarm/select_option',
    )

    get_monthly_cloud_bill_detail_by_node = dict(
        method='GET',
        url='/api/iris/api/monthly_cloud_bill/detail_by_node',
        params={},
        description='GET /api/monthly_cloud_bill/detail_by_node',
    )

    post_monthly_cloud_bill_export = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/export',
        params={},
        description='POST /api/monthly_cloud_bill/export',
    )

    post_monthly_cloud_bill_import = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/import',
        params={},
        description='POST /api/monthly_cloud_bill/import',
    )

    post_monthly_cloud_bill_list = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/list',
        params={},
        description='POST /api/monthly_cloud_bill/list',
    )

    get_monthly_cloud_bill_list_by_node = dict(
        method='GET',
        url='/api/iris/api/monthly_cloud_bill/list_by_node',
        params={},
        description='GET /api/monthly_cloud_bill/list_by_node',
    )

    post_monthly_cloud_bill_split_batch_create = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/split/batch_create',
        params={},
        description='POST /api/monthly_cloud_bill/split/batch_create',
    )

    post_monthly_cloud_bill_split_batch_create_by_bills = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/split/batch_create_by_bills',
        params={},
        description='POST /api/monthly_cloud_bill/split/batch_create_by_bills',
    )

    post_monthly_cloud_bill_split_list = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/split/list',
        params={},
        description='POST /api/monthly_cloud_bill/split/list',
    )

    post_monthly_cloud_bill_split_binding_sync = dict(
        method='POST',
        url='/api/iris/api/monthly_cloud_bill/split_binding/sync',
        params={},
        description='POST /api/monthly_cloud_bill/split_binding/sync',
    )

    get_monthly_cloud_bill_summary_by_node = dict(
        method='GET',
        url='/api/iris/api/monthly_cloud_bill/summary_by_node',
        params={},
        description='GET /api/monthly_cloud_bill/summary_by_node',
    )

    get_monthly_cloud_bill_summary_child_nodes_cost = dict(
        method='GET',
        url='/api/iris/api/monthly_cloud_bill/summary_child_nodes_cost',
        params={},
        description='GET /api/monthly_cloud_bill/summary_child_nodes_cost',
    )

    get_node_operation_item_status = dict(
        method='GET',
        url='/api/iris/api/node/operation_item/status',
        params={},
        description='GET /api/node/operation_item/status',
    )

    get_node_operation_record = dict(
        method='GET',
        url='/api/iris/api/node/operation_record',
        params={},
        description='GET /api/node/operation_record',
    )

    post_node_operation_record_audit = dict(
        method='POST',
        url='/api/iris/api/node/operation_record/audit',
        params={},
        description='POST /api/node/operation_record/audit',
    )

    get_node_operation_record_detail = dict(
        method='GET',
        url='/api/iris/api/node/operation_record/detail',
        params={},
        description='GET /api/node/operation_record/detail',
    )

    get_node_operation_record_latest = dict(
        method='GET',
        url='/api/iris/api/node/operation_record/latest',
        params={},
        description='GET /api/node/operation_record/latest',
    )

    post_node_operation_record_list = dict(
        method='POST',
        url='/api/iris/api/node/operation_record/list',
        params={},
        description='POST /api/node/operation_record/list',
    )

    get_node_operation_record_log_latest = dict(
        method='GET',
        url='/api/iris/api/node/operation_record/log/latest',
        params={},
        description='GET /api/node/operation_record/log/latest',
    )

    get_node_operation_record_progress = dict(
        method='GET',
        url='/api/iris/api/node/operation_record/progress',
        params={},
        description='GET /api/node/operation_record/progress',
    )

    post_node_operation_record_terminate = dict(
        method='POST',
        url='/api/iris/api/node/operation_record/terminate',
        params={},
        description='POST /api/node/operation_record/terminate',
    )

    post_node_operation_record_update_diff = dict(
        method='POST',
        url='/api/iris/api/node/operation_record/update_diff',
        params={},
        description='POST /api/node/operation_record/update_diff',
    )

    post_permission_group_create = dict(
        method='POST',
        url='/api/iris/api/permission_group/create',
        params={},
        description='POST /api/permission_group/create',
    )

    post_permission_group_delete = dict(
        method='POST',
        url='/api/iris/api/permission_group/delete',
        params={},
        description='POST /api/permission_group/delete',
    )

    get_permission_group_list = dict(
        method='GET',
        url='/api/iris/api/permission_group/list',
        params={},
        description='GET /api/permission_group/list',
    )

    post_permission_group_update = dict(
        method='POST',
        url='/api/iris/api/permission_group/update',
        params={},
        description='POST /api/permission_group/update',
    )

    get_proxy_agent_info = dict(
        method='GET',
        url='/api/iris/api/proxy/agent/info',
        params={},
        description='GET /api/proxy/agent/info',
    )

    post_proxy_floating_ci_pipeline_task_list_by_view = dict(
        method='POST',
        url='/api/iris/api/proxy/floating/ci/api/v1/pipeline-task/list-by-view',
        params={},
        description='POST /api/proxy/floating/ci/api/v1/pipeline-task/list-by-view',
    )

    get_proxy_floating_code_resource_remote_branches_for_form = dict(
        method='GET',
        url='/api/iris/api/proxy/floating/code-resource/api/remote-branches-for-form',
        params={},
        description='GET /api/proxy/floating/code-resource/api/remote-branches-for-form',
    )

    post_proxy_grafana_metrics = dict(
        method='POST',
        url='/api/iris/api/proxy/grafana/metrics',
        params={},
        description='POST /api/proxy/grafana/metrics',
    )

    get_proxy_lark_chat_list = dict(
        method='GET',
        url='/api/iris/api/proxy/lark/chat/list',
        params={},
        description='GET /api/proxy/lark/chat/list',
    )

    get_proxy_lark_chat_search = dict(
        method='GET',
        url='/api/iris/api/proxy/lark/chat/search',
        params={},
        description='GET /api/proxy/lark/chat/search',
    )

    get_proxy_lark_ticket = dict(
        method='GET',
        url='/api/iris/api/proxy/lark/ticket',
        params={},
        description='GET /api/proxy/lark/ticket',
    )

    get_proxy_mg_biz_authorized_list = dict(
        method='GET',
        url='/api/iris/api/proxy/mg/biz/authorized_list',
        params={},
        description='GET /api/proxy/mg/biz/authorized_list',
    )

    get_proxy_mg_biz_list = dict(
        method='GET',
        url='/api/iris/api/proxy/mg/biz/list',
        params={},
        description='GET /api/proxy/mg/biz/list',
    )

    get_proxy_mg_biz_root_list = dict(
        method='GET',
        url='/api/iris/api/proxy/mg/biz/root_list',
        params={},
        description='GET /api/proxy/mg/biz/root_list',
    )

    get_proxy_mg_role_list = dict(
        method='GET',
        url='/api/iris/api/proxy/mg/role/list',
        params={},
        description='GET /api/proxy/mg/role/list',
    )

    get_proxy_mg_user_list = dict(
        method='GET',
        url='/api/iris/api/proxy/mg/user/list',
        params={},
        description='GET /api/proxy/mg/user/list',
    )

    get_resource_metrics = dict(
        method='GET',
        url='/api/iris/api/resource/metrics',
        params={},
        description='GET /api/resource/metrics',
    )

    post_task_event_create = dict(
        method='POST',
        url='/api/iris/api/task_event/create',
        params={},
        description='POST /api/task_event/create',
    )

    get_task_event_list = dict(
        method='GET',
        url='/api/iris/api/task_event/list',
        params={},
        description='GET /api/task_event/list',
    )

    post_task_trigger_create = dict(
        method='POST',
        url='/api/iris/api/task_trigger/create',
        params={},
        description='POST /api/task_trigger/create',
    )

    post_task_trigger_delete = dict(
        method='POST',
        url='/api/iris/api/task_trigger/delete',
        params={},
        description='POST /api/task_trigger/delete',
    )

    post_task_trigger_enabled = dict(
        method='POST',
        url='/api/iris/api/task_trigger/enabled',
        params={},
        description='POST /api/task_trigger/enabled',
    )

    get_task_trigger_history_list = dict(
        method='GET',
        url='/api/iris/api/task_trigger/history/list',
        params={},
        description='GET /api/task_trigger/history/list',
    )

    get_task_trigger_list = dict(
        method='GET',
        url='/api/iris/api/task_trigger/list',
        params={},
        description='GET /api/task_trigger/list',
    )

    post_task_trigger_update = dict(
        method='POST',
        url='/api/iris/api/task_trigger/update',
        params={},
        description='POST /api/task_trigger/update',
    )

    post_user_favorites_create = dict(
        method='POST',
        url='/api/iris/api/user/favorites/create',
        params={},
        description='POST /api/user/favorites/create',
    )

    post_user_favorites_delete = dict(
        method='POST',
        url='/api/iris/api/user/favorites/delete',
        params={},
        description='POST /api/user/favorites/delete',
    )

    get_user_favorites_list = dict(
        method='GET',
        url='/api/iris/api/user/favorites/list',
        params={},
        description='GET /api/user/favorites/list',
    )

    post_resource_meta_create = dict(
        method='POST',
        url='/api/iris/api/v1/resource/meta/create',
        params={},
        description='POST /api/v1/resource/meta/create',
    )

    post_resource_meta_delete = dict(
        method='POST',
        url='/api/iris/api/v1/resource/meta/delete',
        params={},
        description='POST /api/v1/resource/meta/delete',
    )

    get_resource_meta_detail = dict(
        method='GET',
        url='/api/iris/api/v1/resource/meta/detail',
        params={},
        description='GET /api/v1/resource/meta/detail',
    )

    get_resource_meta_list = dict(
        method='GET',
        url='/api/iris/api/v1/resource/meta/list',
        params={},
        description='GET /api/v1/resource/meta/list',
    )

    post_resource_meta_update = dict(
        method='POST',
        url='/api/iris/api/v1/resource/meta/update',
        params={},
        description='POST /api/v1/resource/meta/update',
    )

    post_resource_meta_upsert = dict(
        method='POST',
        url='/api/iris/api/v1/resource/meta/upsert',
        params={},
        description='POST /api/v1/resource/meta/upsert',
    )

    get_topology_conf_detail = dict(
        method='GET',
        url='/api/iris/api/v1/topology/conf/detail',
        params={},
        description='GET /api/v1/topology/conf/detail',
    )

    get_topology_conf_list = dict(
        method='GET',
        url='/api/iris/api/v1/topology/conf/list',
        params={},
        description='GET /api/v1/topology/conf/list',
    )

    post_topology_conf_upsert = dict(
        method='POST',
        url='/api/iris/api/v1/topology/conf/upsert',
        params={},
        description='POST /api/v1/topology/conf/upsert',
    )

    post_topology_create = dict(
        method='POST',
        url='/api/iris/api/v1/topology/create',
        params={},
        description='POST /api/v1/topology/create',
    )

    post_topology_delete = dict(
        method='POST',
        url='/api/iris/api/v1/topology/delete',
        params={},
        description='POST /api/v1/topology/delete',
    )

    get_topology_detail = dict(
        method='GET',
        url='/api/iris/api/v1/topology/detail',
        params={},
        description='GET /api/v1/topology/detail',
    )

    get_topology_detail_summary = dict(
        method='GET',
        url='/api/iris/api/v1/topology/detail/summary',
        params={},
        description='GET /api/v1/topology/detail/summary',
    )

    get_topology_list = dict(
        method='GET',
        url='/api/iris/api/v1/topology/list',
        params={},
        description='GET /api/v1/topology/list',
    )

    get_topology_node_available_operations = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/available_operations',
        params={},
        description='GET /api/v1/topology/node/available_operations',
    )

    get_topology_node_change_latest = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/change/latest',
        params={},
        description='GET /api/v1/topology/node/change/latest',
    )

    get_topology_node_change_list = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/change/list',
        params={},
        description='GET /api/v1/topology/node/change/list',
    )

    post_topology_node_change_parent = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/change_parent',
        params={},
        description='POST /api/v1/topology/node/change_parent',
    )

    post_topology_node_clone = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/clone',
        params={},
        description='POST /api/v1/topology/node/clone',
    )

    post_topology_node_conf_bind = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/conf/bind',
        params={},
        description='POST /api/v1/topology/node/conf/bind',
    )

    get_topology_node_conf_template = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/conf/template',
        params={},
        description='GET /api/v1/topology/node/conf/template',
    )

    get_topology_node_config_render = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/config/render',
        params={},
        description='GET /api/v1/topology/node/config/render',
    )

    post_topology_node_create = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/create',
        params={},
        description='POST /api/v1/topology/node/create',
    )

    post_topology_node_delete = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/delete',
        params={},
        description='POST /api/v1/topology/node/delete',
    )

    get_topology_node_detail = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/detail',
        params={},
        description='GET /api/v1/topology/node/detail',
    )

    post_topology_node_do_operation = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/do_operation',
        params={},
        description='POST /api/v1/topology/node/do_operation',
    )

    get_topology_node_healthy = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/healthy',
        params={},
        description='GET /api/v1/topology/node/healthy',
    )

    get_topology_node_info = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/info',
        params={},
        description='GET /api/v1/topology/node/info',
    )

    get_topology_node_init_fields = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/init_fields',
        params={},
        description='GET /api/v1/topology/node/init_fields',
    )

    post_topology_node_kind_modify = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/kind/modify',
        params={},
        description='POST /api/v1/topology/node/kind/modify',
    )

    post_topology_node_lock = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/lock',
        params={},
        description='POST /api/v1/topology/node/lock',
    )

    get_topology_node_log_config = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/log_config',
        params={},
        description='GET /api/v1/topology/node/log_config',
    )

    get_topology_node_monitor_config = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/monitor_config',
        params={},
        description='GET /api/v1/topology/node/monitor_config',
    )

    get_topology_node_operation_info = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/operation_info',
        params={},
        description='GET /api/v1/topology/node/operation_info',
    )

    post_topology_node_owner_update = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/owner/update',
        params={},
        description='POST /api/v1/topology/node/owner/update',
    )

    post_topology_node_partial_update = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/partial_update',
        params={},
        description='POST /api/v1/topology/node/partial_update',
    )

    post_topology_node_rollback = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/rollback',
        params={},
        description='POST /api/v1/topology/node/rollback',
    )

    post_topology_node_sort = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/sort',
        params={},
        description='POST /api/v1/topology/node/sort',
    )

    post_topology_node_state = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/state',
        params={},
        description='POST /api/v1/topology/node/state',
    )

    get_topology_node_summary = dict(
        method='GET',
        url='/api/iris/api/v1/topology/node/summary',
        params={},
        description='GET /api/v1/topology/node/summary',
    )

    post_topology_node_update = dict(
        method='POST',
        url='/api/iris/api/v1/topology/node/update',
        params={},
        description='POST /api/v1/topology/node/update',
    )

    post_topology_rename = dict(
        method='POST',
        url='/api/iris/api/v1/topology/rename',
        params={},
        description='POST /api/v1/topology/rename',
    )

    get_topology_select_list = dict(
        method='GET',
        url='/api/iris/api/v1/topology/select_list',
        params={},
        description='GET /api/v1/topology/select_list',
    )

    post_topology_update = dict(
        method='POST',
        url='/api/iris/api/v1/topology/update',
        params={},
        description='POST /api/v1/topology/update',
    )

    get_topology_version_detail = dict(
        method='GET',
        url='/api/iris/api/v1/topology/version/detail',
        params={},
        description='GET /api/v1/topology/version/detail',
    )

    get_topology_version_list = dict(
        method='GET',
        url='/api/iris/api/v1/topology/version/list',
        params={},
        description='GET /api/v1/topology/version/list',
    )

    get_topology_view = dict(
        method='GET',
        url='/api/iris/api/v1/topology/view',
        params={},
        description='GET /api/v1/topology/view',
    )

    get_v2_topology_detail = dict(
        method='GET',
        url='/api/iris/api/v2/topology/detail',
        params={},
        description='GET /api/v2/topology/detail',
    )

    post_v2_topology_update = dict(
        method='POST',
        url='/api/iris/api/v2/topology/update',
        params={},
        description='POST /api/v2/topology/update',
    )

    post_public_alarm_event_close = dict(
        method='POST',
        url='/api/iris/public/api/alarm_event/close',
        params={},
        description='POST /public/api/alarm_event/close',
    )

    get_public_alarm_event_detail = dict(
        method='GET',
        url='/api/iris/public/api/alarm_event/detail',
        params={},
        description='GET /public/api/alarm_event/detail',
    )

    post_public_alarm_event_list = dict(
        method='POST',
        url='/api/iris/public/api/alarm_event/list',
        params={},
        description='POST /public/api/alarm_event/list',
    )

    post_public_alarm_event_process = dict(
        method='POST',
        url='/api/iris/public/api/alarm_event/process',
        params={},
        description='POST /public/api/alarm_event/process',
    )

    get_public_alarm_event_process_records = dict(
        method='GET',
        url='/api/iris/public/api/alarm_event/process_records',
        params={},
        description='GET /public/api/alarm_event/process_records',
    )

    post_public_alarm_incident_close = dict(
        method='POST',
        url='/api/iris/public/api/alarm_incident/close',
        params={},
        description='POST /public/api/alarm_incident/close',
    )

    get_public_alarm_incident_detail = dict(
        method='GET',
        url='/api/iris/public/api/alarm_incident/detail',
        params={},
        description='GET /public/api/alarm_incident/detail',
    )

    post_public_alarm_incident_list = dict(
        method='POST',
        url='/api/iris/public/api/alarm_incident/list',
        params={},
        description='POST /public/api/alarm_incident/list',
    )

    post_public_alarm_incident_process = dict(
        method='POST',
        url='/api/iris/public/api/alarm_incident/process',
        params={},
        description='POST /public/api/alarm_incident/process',
    )

    get_public_alarm_incident_process_records = dict(
        method='GET',
        url='/api/iris/public/api/alarm_incident/process_records',
        params={},
        description='GET /public/api/alarm_incident/process_records',
    )

    post_public_lark_mobile_login = dict(
        method='POST',
        url='/api/iris/public/api/lark/mobile/login',
        params={},
        description='POST /public/api/lark/mobile/login',
    )

    post_public_log_alarm_close = dict(
        method='POST',
        url='/api/iris/public/api/log_alarm/close',
        params={},
        description='POST /public/api/log_alarm/close',
    )

    get_public_log_alarm_detail = dict(
        method='GET',
        url='/api/iris/public/api/log_alarm/detail',
        params={},
        description='GET /public/api/log_alarm/detail',
    )

    post_public_log_alarm_list = dict(
        method='POST',
        url='/api/iris/public/api/log_alarm/list',
        params={},
        description='POST /public/api/log_alarm/list',
    )

    post_public_log_alarm_process = dict(
        method='POST',
        url='/api/iris/public/api/log_alarm/process',
        params={},
        description='POST /public/api/log_alarm/process',
    )

    get_public_log_alarm_process_records = dict(
        method='GET',
        url='/api/iris/public/api/log_alarm/process_records',
        params={},
        description='GET /public/api/log_alarm/process_records',
    )

    post_public_node_operation_record_audit_callback_agree = dict(
        method='POST',
        url='/api/iris/public/api/node/operation_record/audit_callback/agree',
        params={},
        description='POST /public/api/node/operation_record/audit_callback/agree',
    )

    post_public_node_operation_record_audit_callback_reject = dict(
        method='POST',
        url='/api/iris/public/api/node/operation_record/audit_callback/reject',
        params={},
        description='POST /public/api/node/operation_record/audit_callback/reject',
    )

    post_public_topology_node_webhook_update = dict(
        method='POST',
        url='/api/iris/public/api/v1/topology/node/webhook/update',
        params={},
        description='POST /public/api/v1/topology/node/webhook/update',
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
