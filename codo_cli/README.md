# codo-cli

CODO **开放 API** 命令行客户端。通过网关使用 **AK/SK + HMAC 签名** 调用后端（一期：`codo-admin`，路径前缀 `/api/p`）。

| 项 | 说明 |
|---|---|
| 命令名 | `codo-cli` |
| 鉴权 | 仅 OpenAPI AccessKey / SecretKey（不走控制台密码登录） |
| HTTP | 复用 `websdk2.openapi_client.OpenAPIClient`，不重复实现签名 |
| API 目录 | admin/cmdb/k2/cnmp/iris 见 `websdk2/apis/*_apis.py` |
| 配置文件 | `~/.codo/config.yaml` |
| SecretKey | **禁止写入配置文件**，只用环境变量或一次性参数 |

---

## 目录结构

```text
codo_cli/
  README.md       # 本文档
  __init__.py     # 包版本
  main.py         # argparse 入口
  config.py       # 配置加载 / 展示（打码 SK）
  client.py       # 封装 OpenAPIClient、合并 AdminV4APIS 声明
```

与库代码关系：

```text
codo_cli ──► websdk2.openapi_client ──► 网关 ──► codo-admin
         └─► websdk2.apis.mgv4_apis.AdminV4APIS
```

---

## 安装

**默认安装即可使用 CLI**（包内已带 `codo-cli` 入口）：

```bash
pip install -U codosdk

# 开发（仓库根目录）
pip install -e .
```

验证：

```bash
codo-cli --version
codo-cli --help
```

无全局安装时也可：

```bash
cd /path/to/ops_sdk
PYTHONPATH=. python -m codo_cli.main --help
```

> 可选：若希望配置文件用完整 YAML 解析，可再装 `PyYAML`（`pip install PyYAML`，或 `pip install "codosdk[cli]"`）。不装也能用：环境变量 + 本工具生成的简单 config 即可。

---

## 快速开始

### 1. 准备开放 API 凭证

在管理后台 **权限中心 → 开放API**：

1. 创建账号  
2. 绑定**基础角色**（角色需具备要调用的 admin 接口权限）  
3. 创建 AK/SK，保存 SK（只展示/可回看策略以线上为准）  
4. 等待权限同步到网关（约数分钟，或后台刷新权限）

### 2. 初始化配置

```bash
codo-cli config init
```

编辑 `~/.codo/config.yaml`（示例）：

```yaml
current: default
profiles:
  default:
    endpoint: https://gw.example.com   # 网关地址，不要末尾多余路径
    access_key: "codoAKxxxxxxxx"
    timeout: 10
```

**不要**在 yaml 里写 `secret_key`。设置：

```bash
export CODO_SECRET_KEY='你的SecretKey'
```

### 3. 调用

```bash
codo-cli config show
codo-cli admin biz-list --pretty
codo-cli admin call get_biz_list --pretty
codo-cli api request GET /api/p/v4/biz/list/ --pretty
```

---


## 多服务命令

网关前缀（与产品约定一致）：

| 服务 | 网关前缀 | CLI | API 类 |
|---|---|---|---|
| codo-admin | `/api/p` | `codo-cli admin` | `AdminV4APIS` |
| codo-cmdb | `/api/cmdb` | `codo-cli cmdb` | `CMDBAPIS` |
| codo-k2（配置中心 **V2 新项目**） | `/api/k2` | `codo-cli k2` | `K2APIS` |
| kerrigan（配置中心 **V1 老项目**） | `/api/kerrigan` | `codo-cli kerrigan` | `KerriganAPIS` |
| codo-cnmp | `/api/cnmp` | `codo-cli cnmp` | `CNMPAPIS` |
| codo-iris | `/api/iris` | `codo-cli iris` | `IrisAPIS` |

```bash
codo-cli cmdb list --quiet | head
codo-cli cmdb call get_service_tree -p biz_id=1 --pretty
codo-cli k2 list --filter project          # V2 新项目 /api/k2
codo-cli k2 call get_v1_project_ --pretty
codo-cli kerrigan list                     # V1 老项目 /api/kerrigan
codo-cli kerrigan call get_publish_config -p project_code=demo --pretty
codo-cli cnmp list --filter agent
codo-cli cnmp call get_api_v1_agent_list --pretty
codo-cli iris list --filter topology
codo-cli iris call get_api_v1_topology_list --pretty
codo-cli api request GET /api/cmdb/api/v2/cmdb/server/ --pretty
```

> **kerrigan vs k2：** kerrigan 是配置中心老版本（`/api/kerrigan`）；k2（codo-k2）是 V2 新项目（`/api/k2`）。CLI 与 API 类均分开，不要混用路径。


## 配置说明

### 文件位置

| 项 | 路径 |
|---|---|
| 目录 | `~/.codo/`（权限建议 700） |
| 文件 | `~/.codo/config.yaml`（建议 600） |
| 打印路径 | `codo-cli config path` |

### 配置优先级（从高到低）

1. 命令行参数：`--endpoint` / `--access-key` / `--secret-key` / `--profile` / `--timeout`  
2. 环境变量（见下表）  
3. `~/.codo/config.yaml` 中当前 profile  

### 环境变量

| 变量 | 含义 |
|---|---|
| `CODO_ENDPOINT` | 网关 Base URL，如 `https://gw.example.com` |
| `CODO_ACCESS_KEY` | AccessKey |
| `CODO_SECRET_KEY` | SecretKey（**必填来源之一**，不进配置文件） |
| `CODO_TIMEOUT` | 超时秒数 |
| `CODO_PROFILE` | 使用的 profile 名 |

### SecretKey 策略

- 解析时**只**使用：`--secret-key` 或 `CODO_SECRET_KEY`  
- `config init` / `save` 会去掉任何误写的 `secret_key` 字段  
- `config show` 仅显示是否已设置及打码后的片段  

### 多环境示例

```yaml
current: prod
profiles:
  prod:
    endpoint: https://gw.prod.example.com
    access_key: "codoAKprod..."
    timeout: 15
  test:
    endpoint: https://gw.test.example.com
    access_key: "codoAKtest..."
    timeout: 10
```

```bash
export CODO_SECRET_KEY='...'
codo-cli --profile test admin biz-list --pretty
# 或
export CODO_PROFILE=test
codo-cli admin biz-list --pretty
```

---

## 命令参考

全局：

```bash
codo-cli --version
codo-cli --help
```

多数子命令支持（鉴权/输出）：

| 参数 | 说明 |
|---|---|
| `--profile` | 配置 profile |
| `--endpoint` | 覆盖网关地址 |
| `--access-key` | 覆盖 AK |
| `--secret-key` | 覆盖 SK（更推荐环境变量） |
| `--timeout` | 超时秒 |
| `--pretty` | JSON 缩进打印 |
| `--headers` | 打印 HTTP 响应头 |

### `config` — 配置

```bash
codo-cli config init [--force]   # 生成 ~/.codo/config.yaml；已存在则跳过，--force 覆盖
codo-cli config show             # 当前生效配置（SK 打码）
codo-cli config path             # 打印配置文件绝对路径
```

### `api request` — 通用签名请求

任意网关 path（一期文档以 admin `/api/p/...` 为主）：

```bash
codo-cli api request METHOD PATH [选项]
```

| 参数 | 说明 |
|---|---|
| `METHOD` | `GET` / `POST` / `PUT` / `PATCH` / `DELETE` |
| `PATH` | 如 `/api/p/v4/biz/list/`（建议以 `/` 开头） |
| `-p, --param key=value` | Query，可多次 |
| `-d, --data` | JSON 字符串，或 `@/path/to.json` |
| `-y, --yes` | **写操作必填** |

示例：

```bash
codo-cli api request GET /api/p/v4/user/list/ -p page_size=20 -p searchVal=admin --pretty

codo-cli api request POST /api/p/v4/favorites/ \
  -d '{"key":"x","app_code":"overall","value":{}}' --yes --pretty

codo-cli api request PUT /api/p/v4/xxx/ -d @./body.json --yes
```

### `admin` — codo-admin 封装

#### `admin list`

列出 `AdminV4APIS` 中已声明接口：

```bash
codo-cli admin list
codo-cli admin list --pretty
codo-cli admin list --quiet                    # 只打印 API 名
codo-cli admin list --filter openapi --pretty  # 名称/描述/url 过滤
```

#### `admin call <name>`

按 `AdminV4APIS` **属性名**调用（与 Python SDK 一致）：

```bash
codo-cli admin call get_biz_list --pretty
codo-cli admin call get_user_list -p page_size=50 -p searchVal=foo --pretty
codo-cli admin call opt_users --method POST -d @user.json --yes
codo-cli admin call get_openapi_accounts --pretty
```

| 参数 | 说明 |
|---|---|
| `name` | 如 `get_biz_list`、`get_all_base_role_list` |
| `--method` | 覆盖声明中的 method（少用） |
| `-p key=value` | 覆盖/追加 query |
| `-d` | body JSON 或 `@file` |
| `-y, --yes` | 写操作必填 |

常用 API 名示例（完整以 `admin list` 为准）：

| 名称 | 说明 |
|---|---|
| `get_user_list` / `get_users` | 用户列表 |
| `get_biz_list` / `get_biz` | 业务 |
| `get_all_base_role_list` | 全部基础角色 |
| `get_normal_role_list` | 常规角色列表 |
| `get_func_list` / `get_funcs` | 接口权限 |
| `get_menus` / `get_menu_list` | 菜单 |
| `get_apps` | 应用 |
| `get_tokens` | 长期令牌 |
| `get_openapi_accounts` | 开放 API 账号 |
| `get_openapi_credentials` | 开放 API 密钥 |
| `get_opt_log` | 审计日志 |
| `get_favorites_v4` | 收藏 |

#### 糖衣命令（只读快捷方式）

```bash
codo-cli admin user-list [--search KEYWORD] [--pretty]
codo-cli admin biz-list [--pretty]
codo-cli admin role-base-list [--pretty]
```

分别对应：`get_user_list`、`get_biz_list`、`get_all_base_role_list`。

---

## 写操作安全策略

以下 method 视为写操作，**必须**加 `--yes`，否则退出码 `2` 且不发请求：

- `POST` / `PUT` / `PATCH` / `DELETE`

```bash
# 会被拒绝
codo-cli api request POST /api/p/v4/user/ -d '{}'

# 正确
codo-cli api request POST /api/p/v4/user/ -d '{}' --yes
```

---

## 退出码

| 码 | 含义 |
|---|---|
| `0` | 成功（HTTP 2xx） |
| `1` | 请求已发出但 HTTP 非 2xx，或运行期错误 |
| `2` | 参数/配置错误、缺少 `--yes`、未知 API 名等 |
| `130` | Ctrl-C |

---

## 与网关 / 权限的关系

1. 请求打到 **网关** `endpoint`，path 使用对外路径（如 `/api/p/v4/...`）。  
2. 网关对 AK/SK 验签后，按开放 API 账号的**影子用户 + 基础角色**做 RBAC。  
3. 若返回 **401**：检查 AK/SK、时间同步、签名 path、账号/密钥是否禁用。  
4. 若返回 **403**：角色未绑、权限未同步、或该基础角色没有对应 URI 权限。  
5. 管理类接口（用户 CRUD、开放 API 账号管理等）通常需要**高权限基础角色**；列表类接口按角色授权即可。

浏览器登录用的 JWT 与 CLI 的 AK/SK 是两套凭证；CLI **默认不支持**账号密码登录。

---

## 常见问题

**Q: `缺少 secret_key`**  
A: `export CODO_SECRET_KEY=...`，不要指望写在 yaml 里。

**Q: `缺少 endpoint` / `access_key`**  
A: `config init` 后编辑 yaml，或设 `CODO_ENDPOINT` / `CODO_ACCESS_KEY`。

**Q: `未知 API`**  
A: `codo-cli admin list` 查看合法名称；或用 `api request` 直接打 path。

**Q: 写操作无反应 / 退出 2**  
A: 补上 `--yes`。

**Q: 配置文件解析异常**  
A: 优先 `export CODO_ENDPOINT` / `CODO_ACCESS_KEY` / `CODO_SECRET_KEY`；或 `pip install PyYAML` 后使用标准 yaml。一般 `codo-cli config init` 生成的文件无需额外依赖。

**Q: 能否调用 CMDB 等其它服务？**  
A: 一期官方封装只覆盖 admin。通用方式：`api request` 对任意已支持 AK 的网关 path 调用（需账号角色有对应权限）。

---

## 开发与测试

```bash
cd /path/to/ops_sdk
PYTHONPATH=. python -m pytest tests/test_codo_cli_and_mgv4.py -q
PYTHONPATH=. python -m codo_cli.main admin list --quiet
```

相关代码：

| 文件 | 职责 |
|---|---|
| `codo_cli/main.py` | CLI 参数与子命令 |
| `codo_cli/config.py` | 配置与 SK 策略 |
| `codo_cli/client.py` | 请求封装 |
| `websdk2/openapi_client.py` | 签名 HTTP 客户端 |
| `websdk2/apis/mgv4_apis.py` | Admin API 声明 |

---

## 版本

- CLI 包版本：见 `codo_cli/__init__.py`（`codo-cli --version`）  
- 随 codosdk 发布；入口在 `setup.py` 的 `console_scripts`  

---

## 一期范围与后续

**已做：** admin `/api/p`、配置 profile、通用 `api request`、`admin list/call`、少量 list 糖衣、写操作确认、SK 不落盘。  

**未做：** 其它微服务一等公民子命令、表格输出、交互登录、SK 写入配置文件。