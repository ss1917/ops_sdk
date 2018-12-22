## 安装
### python3.6 安装
[python链接](https://www.python.org/)
##### 在 CentOS 7 中安装 Python 依赖
```bash
$ yum -y groupinstall development
$ yum -y install zlib-devel
$ yum install -y python3-devel openssl-devel libxslt-devel libxml2-devel libcurl-devel
```
##### 在 Debian 中，我们需要安装 gcc、make 和 zlib 压缩/解压缩库
```bash
$ aptitude -y install gcc make zlib1g-dev
```
##### 运行下面的命令来安装 Python 3.6：
```bash
$ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
$ xz -d  Python-3.6.3.tar.xz
$ tar xvf Python-3.6.3.tar
$ cd Python-3.6.3/
$ ./configure
$ make && make install

# 查看安装
$ python3 -V
```

##### pip3安装
```bash
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py

# 查看安装
$ pip3 -V
```
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
    └── websdk      web开发使用
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

## logs
```python
import os
from opssdk.logs import Log
### 日志路径
log_path = '/log/yunwei/{0}.log'.format(os.path.basename(__file__))
### 添加日志标识
log_ins = Log('yunwei', log_path)
### 写日志 （'debug', 'info', 'warning', 'error', 'critical'）
log_ins.write_log('info', 'ceshi')
```

## operate
- exec_shell 执行shell命令
```python
from opssdk.operate import exec_shell
recode,stdout = exec_shell('ls')
# recode 为0 则代表成功，stdout 内容 为列表格式 半月逗号分隔
# recode 非0 则代表失败，stdout 内容 字符串格式
```
- exclusiveLock  脚本锁,防止脚本重复执行
```python
from opssdk.operate import exclusiveLock
exclusiveLock(脚本名称)
```
- MyCrypt  加密解密模块
```python
from opssdk.operate import MyCrypt
mc = MyCrypt()                  # 实例化
mc.my_encrypt('ceshi')          # 对字符串ceshi进行加密
mc.my_decrypt('')               # 对密文进行解密
```
- now_time 获取当前时间 '%Y-%m-%d-%H-%M-%S'格式
```python
from opssdk.operate import now_time
print(now_time())
```
- is_ip 判断是否是IP ,True代表是，False代表不是
```python
from opssdk.operate import is_ip
print(is_ip('192.168.1.11'))
```

## check
系统参数检查和获取
- check_disk 检查目录磁盘剩余空间是否大于10G
- 参数1 检查的目录 参数2 大于磁盘剩余量
```python
from opssdk.operate.check import check_disk
print(check_disk('/data1', 10))
```
- check_sys_version 检查系统版本
```python
from opssdk.operate.check import check_sys_version
print(check_sys_version())
```
- get_ip_address  根据网卡获取ip地址
```
from opssdk.operate.check import get_ip_address
print(get_ip_address('lo'))
```

## get_info
解析配置文件
- json_to_dict 根据json文件的路径 把内容转化成字典格式
```python
from opssdk.get_info import json_to_dict
print(json_to_dict('/tmp/conf.json'))
```
- IniToDict 根据ini文件的路径、节点 把内容转化成字典格式
```python
from opssdk.get_info import IniToDict
itd = IniToDict('/tmp/conf.ini','config') # 实例化
print(itd.get_option())
print(itd.get_option('v1'))
```

## mysql 操作
```python
from opssdk.operate.mysql import MysqlBase
mysql_dict = {"host": "172.16.0.223", "port": 3306, "user": "root", "passwd": "ljXrcyn7", "db": "zhi"}
mb = MysqlBase(**mysql_dict)
### 查询 返回查询值
mb.query(sql)
### 增删改 返回影响行
mb.change(sql)
```

## mail
发送邮件
```python
from opssdk.operate.mail import Mail
mailto_list = "191715030@qq.com, shenshuo@shinezone.com, 381759019@qq.com"
sm = Mail()
"""
:param to_list:  收件人以半角逗号分隔 必填
:param header:   发件名，必填
:param sub:      标题 必填。
:param content:  发件内容 必填。
:param subtype:  发件格式 默认plain，可选 html格式
:param att:      附件 只支持单附件，选填
:return:         True or False
"""
sm.send_mail(mailto_list, '运维', "标题", "内容")
sm.send_mail(mailto_list, '运维', "标题", "内容", 'plain', '/tmp/cof.ini')
```
## utils 实用工具

- timeit 装饰器，获取函数执行时长

## salt api 操作
```python
from  opssdk.operate.centralization import SaltApi
my_salt = SaltApi(url='https://127.0.0.1:8001/', username="saltapi", password="shenshuo")
### 主机  执行方法   命令
req = my_salt.run('*', 'cmd.run_all', 'w')
status, stdout, stderr = req[0], req[1], req[2]
print(status, stdout, stderr)
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).