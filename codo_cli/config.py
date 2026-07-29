# -*- coding: utf-8 -*-
"""配置：~/.codo/config.yaml + 环境变量。SecretKey 禁止写入配置文件。"""

from __future__ import print_function

import os
import re
from copy import deepcopy

CONFIG_DIR = os.path.expanduser('~/.codo')
CONFIG_PATH = os.path.join(CONFIG_DIR, 'config.yaml')

ENV_ENDPOINT = 'CODO_ENDPOINT'
ENV_ACCESS_KEY = 'CODO_ACCESS_KEY'
ENV_SECRET_KEY = 'CODO_SECRET_KEY'
ENV_TIMEOUT = 'CODO_TIMEOUT'
ENV_PROFILE = 'CODO_PROFILE'

_DEFAULT_YAML = """# codo-cli config — secret_key 禁止写入本文件，请使用环境变量 CODO_SECRET_KEY
current: default
profiles:
  default:
    endpoint: https://gw.example.com
    access_key: ""
    timeout: 10
"""


def _default_doc():
    return {
        'current': 'default',
        'profiles': {
            'default': {
                'endpoint': 'https://gw.example.com',
                'access_key': '',
                'timeout': 10,
            }
        },
    }


def ensure_config_dir():
    if not os.path.isdir(CONFIG_DIR):
        os.makedirs(CONFIG_DIR, mode=0o700)


def _load_with_yaml(text):
    import yaml  # optional

    data = yaml.safe_load(text) or {}
    if not isinstance(data, dict):
        return _default_doc()
    return data


def _load_minimal(text):
    """无 PyYAML 时的极简解析（仅支持本工具生成的扁平结构）。"""
    doc = _default_doc()
    current = re.search(r'^current:\s*(\S+)\s*$', text, re.M)
    if current:
        doc['current'] = current.group(1).strip().strip('"\'')
    # profiles.default.endpoint
    ep = re.search(r'endpoint:\s*(\S+)', text)
    ak = re.search(r'access_key:\s*["\']?([^"\'\n]*)["\']?', text)
    to = re.search(r'timeout:\s*(\d+)', text)
    prof = doc['profiles']['default']
    if ep:
        prof['endpoint'] = ep.group(1).strip().strip('"\'')
    if ak:
        prof['access_key'] = ak.group(1).strip()
    if to:
        prof['timeout'] = int(to.group(1))
    return doc


def load_raw_config():
    if not os.path.isfile(CONFIG_PATH):
        return _default_doc()
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        text = f.read()
    if not text.strip():
        return _default_doc()
    try:
        import yaml  # noqa: F401

        data = _load_with_yaml(text)
    except ImportError:
        data = _load_minimal(text)
    if 'profiles' not in data or not isinstance(data.get('profiles'), dict):
        return _default_doc()
    # 防御：丢弃误写入的 secret
    for _n, prof in list(data.get('profiles', {}).items()):
        if isinstance(prof, dict):
            prof.pop('secret_key', None)
    return data


def save_raw_config(doc):
    ensure_config_dir()
    clean = deepcopy(doc) if doc else _default_doc()
    profiles = clean.get('profiles') or {}
    for _name, prof in list(profiles.items()):
        if isinstance(prof, dict):
            prof.pop('secret_key', None)
    try:
        import yaml

        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            f.write('# codo-cli config — do not store secret_key; use CODO_SECRET_KEY\n')
            yaml.safe_dump(clean, f, allow_unicode=True, default_flow_style=False)
    except ImportError:
        # 回退写默认模板 + 简单字段
        cur = clean.get('current') or 'default'
        prof = (clean.get('profiles') or {}).get(cur) or {}
        text = (
            '# codo-cli config — secret_key 禁止写入，请 export CODO_SECRET_KEY\n'
            'current: %s\n'
            'profiles:\n'
            '  %s:\n'
            '    endpoint: %s\n'
            '    access_key: "%s"\n'
            '    timeout: %s\n'
        ) % (
            cur,
            cur,
            prof.get('endpoint') or 'https://gw.example.com',
            prof.get('access_key') or '',
            int(prof.get('timeout') or 10),
        )
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            f.write(text)
    try:
        os.chmod(CONFIG_PATH, 0o600)
    except OSError:
        pass


def init_config(force=False):
    ensure_config_dir()
    if os.path.isfile(CONFIG_PATH) and not force:
        return CONFIG_PATH, False
    # 无 yaml 时直接写模板
    try:
        save_raw_config(_default_doc())
    except Exception:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            f.write(_DEFAULT_YAML)
        try:
            os.chmod(CONFIG_PATH, 0o600)
        except OSError:
            pass
    return CONFIG_PATH, True


def resolve_settings(profile=None, endpoint=None, access_key=None, secret_key=None, timeout=None):
    """
    优先级：显式参数 > 环境变量 > 配置文件 profile。
    secret_key 只来自参数或环境变量，不读配置文件。
    """
    doc = load_raw_config()
    name = profile or os.environ.get(ENV_PROFILE) or doc.get('current') or 'default'
    prof = (doc.get('profiles') or {}).get(name) or {}
    if not isinstance(prof, dict):
        prof = {}

    ep = endpoint or os.environ.get(ENV_ENDPOINT) or prof.get('endpoint') or ''
    ak = access_key or os.environ.get(ENV_ACCESS_KEY) or prof.get('access_key') or ''
    sk = secret_key or os.environ.get(ENV_SECRET_KEY) or ''
    to = timeout
    if to is None:
        env_to = os.environ.get(ENV_TIMEOUT)
        if env_to:
            to = int(env_to)
        else:
            to = int(prof.get('timeout') or 10)

    return {
        'profile': name,
        'endpoint': (ep or '').rstrip('/'),
        'access_key': ak,
        'secret_key': sk,
        'timeout': to,
        'config_path': CONFIG_PATH,
    }


def public_settings_view(settings):
    out = dict(settings)
    sk = out.get('secret_key') or ''
    if sk:
        out['secret_key'] = sk[:2] + '****' + (sk[-2:] if len(sk) > 4 else '')
        out['secret_key_set'] = True
    else:
        out['secret_key'] = ''
        out['secret_key_set'] = False
    return out
