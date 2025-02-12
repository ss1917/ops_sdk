## 安装

### python3安装

[python链接](https://www.python.org/)

##### python3.9以上

##### SDK 安装

```bash
$ pip3 install -U git+https://github.com/ss1917/ops_sdk.git
```

## 结构

```
├── README.md    项目readme
└── opssdk
    ├── logs     日志模块
    ├── install  安装模块
    ├── get_info 配置获取
    └── operate  运维操作
        ├── check           系统参数检查和获取
        ├── mysql           mysql 操作
        ├── mail            发送邮件
        └── centralization  集中化管理工具 salt
    ├── websdk2      web开发使用
    ├── application.py           tornado application
    ├── base_handler.py          tornado  基类
    ├── cache.py                 处理redis缓存
    ├── configs.py               配置文件管理
    ├── consts.py                常量
    ├── db_context.py            MySQL 处理类
    ├── error.py                 异常
    ├── crud_utils.py            API CRUD类
    ├── model_utils.py           数据库模型处理类 sqlalchemy_pagination
    ├── sqlalchemy_pagination.py 分页
    ├── fetch_coroutine.py      
    ├── jwt_token.py             JWT处理
    ├── mqhelper.py              MQ 处理类
    ├── program.py              
    ├── salt_api.py              salt 处理类 可以移到工具类
    ├── ldap.py                  LDAP 处理
    ├── sms.py                   发送短信     可以移到工具类
    ├── tools.py                 工具类
    ├── clent.py                 API调用客户端封装
    └── apis                     API集合
        ├── mgv4_apis       后台API集合
        ├── cmdb_apis       配置平台API
        ├── agent_apis      Agent
        ├── kerrigan_apis   配置文件管理
        └── notice_apis       待补充
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).