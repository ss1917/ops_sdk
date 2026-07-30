#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
codo-cnmp 云原生管理 API 目录（网关前缀 /api/cnmp）
由服务路由自动补全，供 OpenAPIClient / codo-cli 使用。
"""


class CNMPAPIS:
    route_prefix = "/api/cnmp"

    post_agent_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/agent/create',
        params={},
        description='管理-云原生管理-Agent-创建',
    )

    post_agent_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/agent/delete',
        params={},
        description='管理-云原生管理-Agent-删除',
    )

    get_agent_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/agent/list',
        params={},
        description='查看-云原生管理-Agent-列表',
    )

    post_agent_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/agent/update',
        params={},
        description='管理-云原生管理-Agent-编辑',
    )

    get_apigroup_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/apigroup/list',
        params={},
        description='查看-云原生管理-APIGroup-列表',
    )

    get_audit_log_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/audit_log/detail',
        params={},
        description='查看-云原生管理-审计日志详情',
    )

    get_audit_log_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/audit_log/list',
        params={},
        description='查看-云原生管理-审计日志',
    )

    get_audit_log_query_condition_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/audit_log/query_condition/list',
        params={},
        description='查看-云原生管理-审计日志-查询条件',
    )

    get_cloneset_controller_reversion_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/cloneset/controller_reversion/list',
        params={},
        description='查看-云原生管理-CloneSet-历史版本',
    )

    post_cloneset_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-CloneSet-yaml创建更新',
    )

    post_cloneset_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/delete',
        params={},
        description='管理-云原生管理-CloneSet-删除',
    )

    get_cloneset_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/cloneset/detail',
        params={},
        description='查看-云原生管理-CloneSet-详情',
    )

    get_cloneset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/cloneset/list',
        params={},
        description='查看-云原生管理-CloneSet-列表',
    )

    post_cloneset_pod_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/pod/delete',
        params={},
        description='管理-云原生管理-CloneSet-删除pod',
    )

    post_cloneset_restart = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/restart',
        params={},
        description='管理-云原生管理-CloneSet-重启',
    )

    post_cloneset_rollback = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/rollback',
        params={},
        description='管理-云原生管理-CloneSet-回滚',
    )

    post_cloneset_scale = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/scale',
        params={},
        description='管理-云原生管理-CloneSet-伸缩',
    )

    post_cloneset_scale_stream = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/scale_stream',
        params={},
        description='管理-云原生管理-CloneSet-流式扩容',
    )

    post_cloneset_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/cloneset/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-CloneSet-升级策略',
    )

    post_cluster_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/cluster/create',
        params={},
        description='管理-云原生管理-集群-导入',
    )

    post_cluster_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/cluster/delete',
        params={},
        description='管理-云原生管理-集群-删除',
    )

    get_cluster_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/cluster/detail',
        params={},
        description='查看-云原生管理-集群-详情',
    )

    post_cluster_idip_ping = dict(
        method='POST',
        url='/api/cnmp/api/v1/cluster/idip/ping',
        params={},
        description='查看-云原生管理-集群-IdIP连通性',
    )

    post_cluster_kubeconfig_download = dict(
        method='POST',
        url='/api/cnmp/api/v1/cluster/kubeconfig/download',
        params={},
        description='管理-云原生管理-集群-下载kubeConfig',
    )

    get_cluster_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/cluster/list',
        params={},
        description='查看-云原生管理-集群-列表',
    )

    get_cluster_overview = dict(
        method='GET',
        url='/api/cnmp/api/v1/cluster/overview',
        params={},
        description='查看-云原生管理-集群-概览',
    )

    post_cluster_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/cluster/update',
        params={},
        description='管理-云原生管理-集群-编辑',
    )

    post_configmap_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/configmap/create',
        params={},
        description='管理-云原生管理-ConfigMap-创建',
    )

    post_configmap_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/configmap/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-ConfigMap-Yaml创建更新',
    )

    post_configmap_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/configmap/delete',
        params={},
        description='管理-云原生管理-ConfigMap-删除',
    )

    get_configmap_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/configmap/detail',
        params={},
        description='查看-云原生管理-ConfigMap-详情',
    )

    get_configmap_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/configmap/list',
        params={},
        description='查看-云原生管理-ConfigMap-列表',
    )

    post_configmap_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/configmap/update',
        params={},
        description='管理-云原生管理-ConfigMap-更新',
    )

    get_controller_pod_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/controller/pod/list',
        params={},
        description='查看-云原生管理-控制器-Pod列表',
    )

    post_crd_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/crd/delete',
        params={},
        description='管理-云原生管理-CRD-删除',
    )

    get_crd_instance_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/crd/instance/list',
        params={},
        description='查看-云原生管理-CRD实例-列表',
    )

    get_crd_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/crd/list',
        params={},
        description='查看-云原生管理-CRD-列表',
    )

    post_crr_batch_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/crr/batch/create',
        params={},
        description='管理-云原生管理-CRR-批量创建',
    )

    post_crr_batch_detail = dict(
        method='POST',
        url='/api/cnmp/api/v1/crr/batch/detail',
        params={},
        description='查看-云原生管理-CRR-批量查询重启状态',
    )

    post_crr_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/crr/create',
        params={},
        description='管理-云原生管理-CRR-创建',
    )

    get_crr_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/crr/detail',
        params={},
        description='查看-云原生管理-CRR-详情',
    )

    post_daemonset_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/daemonset/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-DaemonSet-Yaml创建更新',
    )

    post_daemonset_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/daemonset/delete',
        params={},
        description='管理-云原生管理-DaemonSet-删除',
    )

    get_daemonset_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/daemonset/detail',
        params={},
        description='查看-云原生管理-DaemonSet-详情',
    )

    get_daemonset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/daemonset/list',
        params={},
        description='查看-云原生管理-DaemonSet-列表',
    )

    post_daemonset_restart = dict(
        method='POST',
        url='/api/cnmp/api/v1/daemonset/restart',
        params={},
        description='管理-云原生管理-DaemonSet-重启',
    )

    get_daemonset_revisions = dict(
        method='GET',
        url='/api/cnmp/api/v1/daemonset/revisions',
        params={},
        description='查看-云原生管理-DaemonSet-历史版本',
    )

    post_daemonset_rollback = dict(
        method='POST',
        url='/api/cnmp/api/v1/daemonset/rollback',
        params={},
        description='管理-云原生管理-DaemonSet-回滚',
    )

    post_daemonset_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/daemonset/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-DaemonSet-更新策略',
    )

    post_deployment_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-Deployment-Yaml创建更新',
    )

    post_deployment_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/delete',
        params={},
        description='管理-云原生管理-Deployment-删除',
    )

    get_deployment_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/deployment/detail',
        params={},
        description='查看-云原生管理-Deployment-详情',
    )

    get_deployment_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/deployment/list',
        params={},
        description='查看-云原生管理-Deployment-列表',
    )

    get_deployment_replicaset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/deployment/replicaset/list',
        params={},
        description='查看-云原生管理-Deployment-历史版本',
    )

    post_deployment_restart = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/restart',
        params={},
        description='管理-云原生管理-Deployment-重启',
    )

    post_deployment_rollback = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/rollback',
        params={},
        description='管理-云原生管理-Deployment-回滚',
    )

    post_deployment_scale = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/scale',
        params={},
        description='管理-云原生管理-Deployment-扩缩容',
    )

    post_deployment_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/deployment/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-Deployment-更新策略',
    )

    get_event_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/event/list',
        params={},
        description='查看-云原生管理-Event-列表',
    )

    post_ezrollout_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/ezrollout/create',
        params={},
        description='查看-云原生管理-版本伸缩-创建',
    )

    post_ezrollout_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/ezrollout/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-版本伸缩-yaml创建/更新',
    )

    post_ezrollout_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/ezrollout/delete',
        params={},
        description='管理-云原生管理-版本伸缩-删除',
    )

    get_ezrollout_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/ezrollout/detail',
        params={},
        description='查看-云原生管理-版本伸缩-详情',
    )

    get_ezrollout_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/ezrollout/list',
        params={},
        description='查看-云原生管理-版本伸缩-列表',
    )

    post_ezrollout_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/ezrollout/update',
        params={},
        description='管理-云原生管理-版本伸缩-编辑',
    )

    post_gameserver_entity_batch_manage = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserver/entity/batch/manage',
        params={},
        description='管理-云原生管理-游戏进程-批量管理',
    )

    post_gameserver_entity_manage = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserver/entity/manage',
        params={},
        description='管理-云原生管理-游戏进程-Entity',
    )

    post_gameserver_lb_batch_manage = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserver/lb/batch/manage',
        params={},
        description='管理-云原生管理-LB-批量管理',
    )

    post_gameserver_lb_manage = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserver/lb/manage',
        params={},
        description='管理-云原生管理-游戏进程-LB',
    )

    get_gameserver_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/gameserver/list',
        params={},
        description='查看-云原生管理-游戏进程-列表',
    )

    get_gameserver_type_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/gameserver/type/list',
        params={},
        description='查看-云原生管理-游戏进程-进程类型',
    )

    get_gameserverset_controller_reversion_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/gameserverset/controller_reversion/list',
        params={},
        description='查看-云原生管理-GameServerSet-历史版本',
    )

    post_gameserverset_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-GameServerSet-Yaml创建更新',
    )

    post_gameserverset_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/delete',
        params={},
        description='管理-云原生管理-GameServerSet-删除',
    )

    get_gameserverset_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/gameserverset/detail',
        params={},
        description='查看-云原生管理-GameServerSet-详情',
    )

    get_gameserverset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/gameserverset/list',
        params={},
        description='查看-云原生管理-GameServerSet-列表',
    )

    post_gameserverset_pod_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/pod/delete',
        params={},
        description='管理-云原生管理-GameServerSet-删除Pod',
    )

    post_gameserverset_restart = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/restart',
        params={},
        description='管理-云原生管理-GameServerSet-重启',
    )

    post_gameserverset_rollback = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/rollback',
        params={},
        description='管理-云原生管理-GameServerSet-回滚',
    )

    post_gameserverset_scale = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/scale',
        params={},
        description='管理-云原生管理-GameServerSet-伸缩',
    )

    post_gameserverset_scale_stream = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/scale_stream',
        params={},
        description='管理-云原生管理-GameServerSet-扩容策略',
    )

    post_gameserverset_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/gameserverset/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-GameServerSet-升级策略',
    )

    post_hpa_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/hpa/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-HPA-Yaml创建更新',
    )

    post_hpa_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/hpa/delete',
        params={},
        description='管理-云原生管理-HPA-删除',
    )

    get_hpa_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/hpa/detail',
        params={},
        description='查看-云原生管理-HPA-详情',
    )

    get_hpa_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/hpa/list',
        params={},
        description='查看-云原生管理-HPA-列表',
    )

    post_ingress_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/ingress/create',
        params={},
        description='管理-云原生管理-Ingress-创建',
    )

    post_ingress_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/ingress/delete',
        params={},
        description='管理-云原生管理-Ingress-删除',
    )

    get_ingress_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/ingress/detail',
        params={},
        description='查看-云原生管理-Ingress-详情',
    )

    get_ingress_host_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/ingress/host/list',
        params={},
        description='查看-云原生管理-Ingress域名-列表',
    )

    get_ingress_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/ingress/list',
        params={},
        description='查看-云原生管理-Ingress-列表',
    )

    post_ingress_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/ingress/update',
        params={},
        description='管理-云原生管理-Ingress-编辑',
    )

    get_ingressclass_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/ingressclass/list',
        params={},
        description='查看-云原生管理-IngressClass-列表',
    )

    post_limitrange_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/limitrange/create',
        params={},
        description='管理-云原生管理-LimitRange-创建',
    )

    post_limitrange_create_or_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/limitrange/create_or_update',
        params={},
        description='管理-云原生管理-LimitRange-创建或编辑',
    )

    post_limitrange_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/limitrange/delete',
        params={},
        description='管理-云原生管理-LimitRange-删除',
    )

    get_limitrange_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/limitrange/detail',
        params={},
        description='查看-云原生管理-LimitRange-详情',
    )

    get_limitrange_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/limitrange/list',
        params={},
        description='查看-云原生管理-LimitRange-列表',
    )

    post_limitrange_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/limitrange/update',
        params={},
        description='管理-云原生管理-LimitRange-编辑',
    )

    post_namespace_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/namespace/create',
        params={},
        description='管理-云原生管理-命名空间-创建',
    )

    post_namespace_create_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/namespace/create_by_yaml',
        params={},
        description='管理-云原生管理-命名空间-YAML创建',
    )

    post_namespace_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/namespace/delete',
        params={},
        description='管理-云原生管理-命名空间-删除',
    )

    get_namespace_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/namespace/detail',
        params={},
        description='查看-云原生管理-命名空间-详情',
    )

    get_namespace_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/namespace/list',
        params={},
        description='查看-云原生管理-命名空间-列表',
    )

    get_namespace_pod_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/namespace/pod/detail',
        params={},
        description='查看-云原生管理-命名空间-Pod详情',
    )

    get_namespace_pod_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/namespace/pod/list',
        params={},
        description='查看-云原生管理-命名空间-Pod列表',
    )

    post_namespace_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/namespace/update',
        params={},
        description='管理-云原生管理-命名空间-编辑',
    )

    post_namespace_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/namespace/update_by_yaml',
        params={},
        description='管理-云原生管理-命名空间-YAML更新',
    )

    get_namespace_yaml = dict(
        method='GET',
        url='/api/cnmp/api/v1/namespace/yaml',
        params={},
        description='查看-云原生管理-命名空间-YAML',
    )

    post_node_create_or_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/node/create_or_update',
        params={},
        description='管理-云原生管理-节点-Yaml创建更新',
    )

    get_node_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/node/detail',
        params={},
        description='查看-云原生管理-节点-详情',
    )

    get_node_eviction_check = dict(
        method='GET',
        url='/api/cnmp/api/v1/node/eviction/check',
        params={},
        description='管理-云原生管理-节点-Pod驱逐检查',
    )

    post_node_handle = dict(
        method='POST',
        url='/api/cnmp/api/v1/node/handle',
        params={},
        description='管理-云原生管理-节点-操作',
    )

    get_node_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/node/list',
        params={},
        description='查看-云原生管理-节点-列表',
    )

    post_node_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/node/update',
        params={},
        description='管理-云原生管理-节点-编辑',
    )

    get_persistentvolume_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/persistentvolume/list',
        params={},
        description='查看-云原生管理-PersistentVolume-列表',
    )

    post_pod_batch_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/pod/batch/delete',
        params={},
        description='管理-云原生管理-Pod-批量重启',
    )

    get_pod_container_metrics = dict(
        method='GET',
        url='/api/cnmp/api/v1/pod/container/metrics',
        params={},
        description='查看-云原生管理-Pod-容器指标',
    )

    post_pod_create_or_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/pod/create_or_update',
        params={},
        description='管理-云原生管理-Pod-Yaml创建更新',
    )

    post_pod_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/pod/delete',
        params={},
        description='管理-云原生管理-Pod-删除',
    )

    post_pod_evict = dict(
        method='POST',
        url='/api/cnmp/api/v1/pod/evict',
        params={},
        description='管理-云原生管理-Pod-驱逐',
    )

    get_pod_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/pod/list',
        params={},
        description='查看-云原生管理-Pod-列表',
    )

    get_pod_logs_download = dict(
        method='GET',
        url='/api/cnmp/api/v1/pod/logs/download',
        params={},
        description='查看-云原生管理-Pod-下载日志',
    )

    get_pod_metrics_cpu = dict(
        method='GET',
        url='/api/cnmp/api/v1/pod/metrics/cpu',
        params={},
        description='查看-云原生管理-Pod-CPU指标',
    )

    get_pod_metrics_memory = dict(
        method='GET',
        url='/api/cnmp/api/v1/pod/metrics/memory',
        params={},
        description='查看-云原生管理-Pod-内存指标',
    )

    post_pvc_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/pvc/delete',
        params={},
        description='管理-云原生管理-PersistentVolumeClaim-删除',
    )

    get_pvc_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/pvc/list',
        params={},
        description='查看-云原生管理-PersistentVolumeClaim-列表',
    )

    post_resource_dry_run = dict(
        method='POST',
        url='/api/cnmp/api/v1/resource/dry_run',
        params={},
        description='管理-云原生管理-Resource-DryRun',
    )

    post_resource_from_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/resource/from_yaml',
        params={},
        description='管理-云原生管理-Resource-Yaml创建更新',
    )

    post_resourcequota_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/resourcequota/create',
        params={},
        description='管理-云原生管理-ResourceQuota-创建',
    )

    post_resourcequota_create_or_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/resourcequota/create_or_update',
        params={},
        description='管理-云原生管理-ResourceQuota-创建或编辑',
    )

    post_resourcequota_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/resourcequota/delete',
        params={},
        description='管理-云原生管理-ResourceQuota-删除',
    )

    get_resourcequota_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/resourcequota/detail',
        params={},
        description='查看-云原生管理-ResourceQuota-详情',
    )

    get_resourcequota_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/resourcequota/list',
        params={},
        description='查看-云原生管理-ResourceQuota-列表',
    )

    post_resourcequota_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/resourcequota/update',
        params={},
        description='管理-云原生管理-ResourceQuota-编辑',
    )

    get_role_binding_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/role/binding/list',
        params={},
        description='查看-云原生管理-角色绑定-列表',
    )

    post_role_binding_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/role/binding/update',
        params={},
        description='管理-云原生管理-角色绑定-编辑',
    )

    post_role_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/role/create',
        params={},
        description='管理-云原生管理-角色-新增',
    )

    post_role_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/role/delete',
        params={},
        description='管理-云原生管理-角色-删除',
    )

    get_role_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/role/detail',
        params={},
        description='查看-云原生管理-角色-详情',
    )

    get_role_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/role/list',
        params={},
        description='查看-云原生管理-角色-列表',
    )

    post_role_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/role/update',
        params={},
        description='管理-云原生管理-角色-编辑',
    )

    post_secret_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/secret/create',
        params={},
        description='管理-云原生管理-Secret-创建',
    )

    post_secret_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/secret/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-Secret-Yaml创建更新',
    )

    post_secret_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/secret/delete',
        params={},
        description='管理-云原生管理-Secret-删除',
    )

    get_secret_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/secret/detail',
        params={},
        description='查看-云原生管理-Secret-详情',
    )

    get_secret_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/secret/list',
        params={},
        description='查看-云原生管理-Secret-列表',
    )

    post_secret_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/secret/update',
        params={},
        description='管理-云原生管理-Secret-更新',
    )

    post_sidecarset_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/sidecarset/delete',
        params={},
        description='管理-云原生管理-SideCarSet-删除',
    )

    get_sidecarset_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/sidecarset/detail',
        params={},
        description='查看-云原生管理-SideCarSet-详情',
    )

    get_sidecarset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/sidecarset/list',
        params={},
        description='查看-云原生管理-SideCarSet-列表',
    )

    post_sidecarset_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/sidecarset/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-SideCarSet-更新策略',
    )

    post_statefulset_create_or_update_by_yaml = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/create_or_update_by_yaml',
        params={},
        description='管理-云原生管理-StatefulSet-Yaml创建更新',
    )

    post_statefulset_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/delete',
        params={},
        description='管理-云原生管理-StatefulSet-删除',
    )

    get_statefulset_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/statefulset/detail',
        params={},
        description='查看-云原生管理-StatefulSet-详情',
    )

    get_statefulset_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/statefulset/list',
        params={},
        description='查看-云原生管理-StatefulSet-列表',
    )

    post_statefulset_restart = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/restart',
        params={},
        description='管理-云原生管理-StatefulSet-重启',
    )

    get_statefulset_revisions = dict(
        method='GET',
        url='/api/cnmp/api/v1/statefulset/revisions',
        params={},
        description='查看-云原生管理-StatefulSet-历史版本',
    )

    post_statefulset_rollback = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/rollback',
        params={},
        description='管理-云原生管理-StatefulSet-回滚',
    )

    post_statefulset_scale = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/scale',
        params={},
        description='管理-云原生管理-StatefulSet-伸缩',
    )

    post_statefulset_upgrade_strategy_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/statefulset/upgrade_strategy/update',
        params={},
        description='管理-云原生管理-StatefulSet-更新策略',
    )

    get_storageclass_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/storageclass/list',
        params={},
        description='查看-云原生管理-StorageClass-列表',
    )

    post_svc_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/svc/create',
        params={},
        description='管理-云原生管理-Service-创建',
    )

    post_svc_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/svc/delete',
        params={},
        description='管理-云原生管理-Service-删除',
    )

    get_svc_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/svc/detail',
        params={},
        description='查看-云原生管理-Service-详情',
    )

    get_svc_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/svc/list',
        params={},
        description='查看-云原生管理-Service-列表',
    )

    post_svc_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/svc/update',
        params={},
        description='管理-云原生管理-Service-编辑',
    )

    post_user_follow_create = dict(
        method='POST',
        url='/api/cnmp/api/v1/user/follow/create',
        params={},
        description='管理-云原生管理-我的关注',
    )

    post_user_follow_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/user/follow/delete',
        params={},
        description='管理-云原生管理-取消关注',
    )

    get_user_follow_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/user/follow/list',
        params={},
        description='查看-云原生管理-用户关注列表',
    )

    get_user_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/user/list',
        params={},
        description='查看-云原生管理-用户列表',
    )

    post_usergroup_grant = dict(
        method='POST',
        url='/api/cnmp/api/v1/usergroup/grant',
        params={},
        description='管理-云原生管理-用户组-授权',
    )

    post_usergroup_granted_delete = dict(
        method='POST',
        url='/api/cnmp/api/v1/usergroup/granted/delete',
        params={},
        description='管理-云原生管理-用户组-删除授权',
    )

    get_usergroup_granted_detail = dict(
        method='GET',
        url='/api/cnmp/api/v1/usergroup/granted/detail',
        params={},
        description='查看-云原生管理-用户组-授权详情',
    )

    get_usergroup_granted_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/usergroup/granted/list',
        params={},
        description='查看-云原生管理-用户组-授权列表',
    )

    post_usergroup_granted_update = dict(
        method='POST',
        url='/api/cnmp/api/v1/usergroup/granted/update',
        params={},
        description='管理-云原生管理-用户组-编辑授权',
    )

    get_usergroup_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/usergroup/list',
        params={},
        description='查看-云原生管理-用户组-列表',
    )

    get_usergroup_users_list = dict(
        method='GET',
        url='/api/cnmp/api/v1/usergroup/users/list',
        params={},
        description='查看-云原生管理-用户组-成员列表',
    )

    get_ws_pod_command = dict(
        method='GET',
        url='/api/cnmp/api/v1/ws/pod/command',
        params={},
        description='执行-云原生管理-终端-Pod命令',
    )

    get_ws_pod_log = dict(
        method='GET',
        url='/api/cnmp/api/v1/ws/pod/log',
        params={},
        description='查看-云原生管理-终端-Pod日志',
    )

    get_helloworld_id = dict(
        method='GET',
        url='/api/cnmp/helloworld/{name}',
        params={},
        description='Sends a greeting',
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
