# CODO SDK

[![Python](https://img.shields.io/badge/Python-%3E%3D3.9-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Version](https://img.shields.io/badge/version-1.0.55-brightgreen)](https://pypi.org/project/codosdk/)

CODO项目的官方Python SDK，提供企业级Web应用开发框架和运维工具集成。基于Tornado，集成数据库、缓存、消息队列、认证等核心组件。

## 核心特性

- **Tornado Web框架** - 异步请求处理，内置认证和权限管理
- **数据库支持** - SQLAlchemy ORM，支持主从库配置
- **Redis缓存** - 多连接池管理
- **消息队列** - RabbitMQ集成
- **多种认证** - JWT、LDAP、Session
- **API集成** - 预定义CODO各平台API接口
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
├── websdk2/                        # Web开发SDK（主模块）
│   ├── apis/                       # CODO平台API集合
│   │   ├── admin_apis.py          # 用户管理API
│   │   ├── mgv4_apis.py           # 后台管理API
│   │   ├── cmdb_apis.py           # CMDB配置API
│   │   ├── agent_apis.py          # Agent代理API
│   │   ├── task_apis.py           # 任务调度API
│   │   ├── kerrigan_apis.py       # 配置文件管理API
│   │   └── notice_apis.py         # 通知告警API
│   │
│   ├── cloud/                     # 云厂商SDK
│   │
│   ├── utils/                     # 工具集
│   │   ├── pydantic_utils.py      # Pydantic数据验证
│   │   ├── date_format.py         # 日期格式化
│   │   └── cc_crypto.py           # 加密解密
│   │
│   ├── application.py              # Tornado应用定制
│   ├── base_handler.py             # 请求处理基类（认证、授权）
│   ├── db_context.py               # 数据库连接管理
│   ├── cache.py / cache_context.py # Redis缓存管理
│   ├── crud_utils.py               # CRUD工具（分页、验证）
│   ├── sqlalchemy_pagination.py    # ORM分页组件
│   ├── model_utils.py              # 模型转换工具
│   ├── jwt_token.py                # JWT认证
│   ├── mqhelper.py                 # RabbitMQ消息队列
│   ├── client.py                   # API调用客户端
│   ├── ldap.py                     # LDAP认证
│   ├── configs.py                  # 配置管理
│   ├── consts.py                   # 常量定义
│   ├── error.py                    # 自定义异常
│   ├── logger.py                   # 日志配置
│   └── ...                         # 其他工具模块
│
├── opssdk/                         # 运维SDK（原始模块）
│   └── utils/                      # 运维工具集
│
├── setup.py                        # 包配置
└── pyproject.toml                  # 项目配置
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).