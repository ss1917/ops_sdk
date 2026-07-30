#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .admin_apis import AdminAPIS
from .task_apis import TaskAPIS
from .kerrigan_apis import KerriganAPIS
from .mgv4_apis import AdminV4APIS
from .cmdb_apis import CMDBAPIS
from .k2_apis import K2APIS
from .cnmp_apis import CNMPAPIS
from .iris_apis import IrisAPIS
from .agent_apis import AgentAPIS
from .notice_apis import NoticeAPIS

# 服务名 -> API 类（codo-cli 使用）
# kerrigan = 配置中心 V1（老）；k2 = 配置中心 V2（新项目 codo-k2），前缀不同
SERVICE_API_CLASSES = {
    'admin': AdminV4APIS,
    'cmdb': CMDBAPIS,
    'k2': K2APIS,              # /api/k2  — codo-k2 (V2)
    'kerrigan': KerriganAPIS,  # /api/kerrigan — 老 kerrigan (V1)
    'cnmp': CNMPAPIS,
    'iris': IrisAPIS,
}


def get_service_api_class(name: str):
    if not name:
        return None
    return SERVICE_API_CLASSES.get(name.lower())

