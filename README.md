# CODO SDK

[![Python](https://img.shields.io/badge/Python-%3E%3D3.9-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Version](https://img.shields.io/badge/version-1.0.60-brightgreen)](https://pypi.org/project/codosdk/)

CODO项目的官方Python SDK，提供企业级Web应用开发框架和运维工具集成。基于Tornado，集成数据库、缓存、消息队列、认证等核心组件；并提供 **开放 API（AK/SK）客户端** 与 **`codo-cli` 命令行**。

## 核心特性

- **Tornado Web框架** - 异步请求处理，内置认证和权限管理
- **数据库支持** - SQLAlchemy ORM，支持主从库配置
- **Redis缓存** - 多连接池管理
- **消息队列** - RabbitMQ集成
- **多种认证** - JWT、LDAP、Session；开放 API AK/SK 签名
- **API集成** - 预定义 admin / cmdb / k2 / cnmp / iris 等平台接口
- **codo-cli** - 基于 AK/SK 的命令行调用
- **数据验证** - Pydantic模型验证
- **工具支持** - 各类常用工具封装

## 安装

```bash
# 从PyPI安装
pip install codosdk

# 从GitHub安装最新版
pip install -U git+https://github.com/ss1917/ops_sdk.git
```

## 快速开始

### 创建Web应用

```python
from websdk2.application import Application
from websdk2.base_handler import BaseHandler

class HelloHandler(BaseHandler):
    def get(self):
        self.write({'code': 0, 'msg': 'Hello CODO!'})

handlers = [
    (r'/api/hello/', HelloHandler, {'handle_name': '问候接口', 'method': ['GET']}),
]

app = Application(handlers)
app.start_server()
```

### 使用数据库

```python
from websdk2.db_context import DBContextV2 as DBContext
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)

# 查询
with DBContext('r') as session:
    user = session.query(User).filter(User.username == 'admin').first()

# 创建/更新
with DBContext('w') as session:
    user = User(username='new_user')
    session.add(user)
```

### 使用缓存

```python
from websdk2.cache_context import cache_conn

redis_conn = cache_conn()
redis_conn.set('key', 'value', ex=3600)
value = redis_conn.get('key')
```

### JWT认证

```python
from websdk2.jwt_token import AuthToken

auth = AuthToken()

# 生成Token
token = auth.encode_auth_token(
    user_id='123',
    username='admin',
    exp_time=7  # 7天过期
)

# 验证Token
user_info = auth.decode_auth_token(token)
```

### 开放 API（AK/SK）

适用于 CI、集成方等编程访问。网关校验 `CODO1-HMAC-SHA256` 签名后签发短时内部 JWT。

```python
from websdk2.openapi_client import OpenAPIClient

client = OpenAPIClient(
    endpoint="https://gw.example.com",
    access_key="your-ak",
    secret_key="your-sk",
)
resp = client.request("GET", "/api/p/v4/biz/list/")
print(resp.status_code, resp.text)
```

## codo-cli（开放 API 命令行）

通过 **AK/SK** 调用网关后的各业务服务。完整说明见 **[codo_cli/README.md](codo_cli/README.md)**。

### 快速开始

```bash
pip install -U codosdk          # 已含 codo-cli 入口；开发：pip install -e .
codo-cli config init
# 编辑 ~/.codo/config.yaml 的 endpoint、access_key
export CODO_SECRET_KEY='你的SK'  # 禁止写入配置文件

codo-cli admin list
codo-cli admin call get_biz_list --pretty
codo-cli admin biz-list
codo-cli api request GET /api/p/v4/biz/list/ --pretty
codo-cli api request POST /api/p/v4/user/ -d @body.json --yes   # 写操作必须 --yes

codo-cli cmdb list --quiet | head
codo-cli k2 list --filter project
codo-cli cnmp list --filter agent
codo-cli iris list --filter topology
```

### 消息队列

```python
from websdk2.mqhelper import MessageQueueBase
import json

# 发送消息（with语句自动管理连接）
msg = json.dumps({'task_id': '123', 'status': 'running'})
with MessageQueueBase('bpm_task_log', 'direct', 'the_log') as mq:
    mq.publish_message(msg)

# 消费消息（继承MessageQueueBase）
class TaskConsumer(MessageQueueBase):
    def __init__(self):
        super().__init__(
            exchange='bpm_task_log',
            exchange_type='direct',
            routing_key='the_log',
            queue_name='task_queue'
        )

    def on_message(self, body):
        """处理接收到的消息"""
        print(f"收到消息: {body}")

# 启动消费
consumer = TaskConsumer()
consumer.start_consuming()
```

## 配置示例

### 数据库配置

```python
from websdk2.consts import const

db_config = {
    const.DB_CONFIG_ITEM: {
        const.DEFAULT_DB_KEY: {
            const.DBHOST_KEY: 'localhost',
            const.DBPORT_KEY: 3306,
            const.DBUSER_KEY: 'root',
            const.DBPWD_KEY: 'password',
            const.DBNAME_KEY: 'codo_db',
        }
    }
}
```

### Redis配置

```python
from websdk2.consts import const
redis_config = {
    const.REDIS_CONFIG_ITEM: {
        const.DEFAULT_RD_KEY: {
            const.RD_HOST_KEY: 'localhost',
            const.RD_PORT_KEY: 6379,
            const.RD_DB_KEY: 0,
            const.RD_PASSWORD_KEY: 'password',
        }
    }
}
```

## 项目结构

```
ops_sdk/
├── codo_cli/                       # 开放 API 命令行（入口：codo-cli）
│   ├── README.md                   # CLI 完整使用文档
│   ├── main.py                     # argparse 子命令入口
│   ├── config.py                   # ~/.codo/config.yaml（SK 禁止落盘）
│   └── client.py                   # 封装 OpenAPIClient
│
├── websdk2/                        # Web 开发 SDK（主模块）
│   ├── apis/                       # 各服务 API 声明（供 SDK / codo-cli）
│   │   ├── __init__.py             # SERVICE_API_CLASSES 注册表
│   │   ├── mgv4_apis.py            # codo-admin（/api/p）AdminV4APIS
│   │   ├── admin_apis.py           # 历史 admin API
│   │   ├── cmdb_apis.py            # codo-cmdb（/api/cmdb）CMDBAPIS
│   │   ├── k2_apis.py              # codo-k2 配置中心 V2（/api/k2）K2APIS
│   │   ├── kerrigan_apis.py        # kerrigan 配置中心 V1 老（/api/kerrigan）
│   │   ├── cnmp_apis.py            # codo-cnmp 云原生（/api/cnmp）CNMPAPIS
│   │   ├── iris_apis.py            # codo-iris 拓扑/告警（/api/iris）IrisAPIS
│   │   ├── agent_apis.py           # Agent
│   │   ├── task_apis.py            # 任务调度
│   │   └── notice_apis.py          # 通知
│   │
│   ├── openapi_client.py           # AK/SK 签名 HTTP 客户端
│   ├── openapi_sign.py             # CODO1-HMAC-SHA256 签名
│   ├── client.py                   # 传统 JWT/Cookie API 客户端（AcsClient）
│   │
│   ├── cloud/                      # 云厂商 SDK
│   ├── utils/                      # 工具集
│   │   ├── pydantic_utils.py
│   │   ├── date_format.py
│   │   └── cc_crypto.py
│   │
│   ├── application.py              # Tornado 应用
│   ├── base_handler.py             # 请求处理基类
│   ├── db_context.py               # 数据库连接
│   ├── cache.py / cache_context.py # Redis
│   ├── crud_utils.py
│   ├── sqlalchemy_pagination.py
│   ├── model_utils.py
│   ├── jwt_token.py                # JWT
│   ├── mqhelper.py                 # RabbitMQ
│   ├── ldap.py
│   ├── configs.py / consts.py
│   ├── error.py / logger.py
│   └── ...
│
├── opssdk/                         # 运维 SDK（原始模块）
│   └── utils/
│
├── tests/                          # 单元测试
│   ├── test_codo_cli_and_mgv4.py
│   ├── test_multi_service_apis.py
│   └── test_openapi_sign.py
│
├── setup.py                        # 包配置（含 console_scripts: codo-cli）
├── pyproject.toml
└── README.md
```

网关 path 与服务对应关系见上文 **codo-cli** 表格；Python 调用示例：

```python
from websdk2.openapi_client import OpenAPIClient
from websdk2.apis.cmdb_apis import CMDBAPIS
from websdk2.apis.k2_apis import K2APIS
from websdk2.apis.cnmp_apis import CNMPAPIS
from websdk2.apis.iris_apis import IrisAPIS

client = OpenAPIClient(endpoint="https://gw.example.com", access_key="...", secret_key="...")
# 使用各 APIS 类中的 url / method 字段拼请求，或直接 client.request(...)
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).