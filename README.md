## 安装

### python3安装

[python链接](https://www.python.org/)

##### python3.9以上

##### SDK 安装

```bash
$ pip3 install -U git+https://github.com/ss1917/ops_sdk.git
```

## 结构

```shell
.
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
    └── websdk2      web开发使用
    ├── application.py          tornado application
    ├── base_handler.py         tornado  基类
    ├── cache.py                处理redis缓存
    ├── configs.py              配置文件管理
    ├── consts.py               常量
    ├── db_context.py           MySQL 处理类
    ├── error.py                异常
    ├── fetch_coroutine.py      
    ├── __init__.py
    ├── jwt_token.py            jwt
    ├── mqhelper.py             MQ 处理类
    ├── program.py
    ├── salt_api.py             salt 处理类 可以移到工具类
    ├── sms.py                  发送短信     可以移到工具类
    ├── tools.py                工具类
    └── web_logs.py             日志处理
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).