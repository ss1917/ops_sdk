#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2023/3/17
Desc    : 对接LDAP登录认证
"""

import logging
import json
from typing import Dict, Optional, Tuple, Union
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES


class LdapApi:
    def __init__(self, ldap_server_host, ldap_admin_dn, ldap_admin_password, ldap_server_port=389, ldap_use_ssl=False):
        self._ldap_admin_dn = ldap_admin_dn
        self._ldap_admin_password = ldap_admin_password
        # ldap_server_pool = ServerPool(["172.16.0.102",'172.16.0.103'])
        use_ssl = True if ldap_use_ssl in ['y', 'yes', True] else False
        self.ldap_server = Server(ldap_server_host, port=ldap_server_port, use_ssl=ldap_use_ssl)

    def ldap_server_test(self):
        try:
            conn = Connection(self.ldap_server, user=self._ldap_admin_dn, password=self._ldap_admin_password,
                              check_names=True, lazy=False, raise_exceptions=False)
            conn.open()
            conn.bind()
            return True
        except Exception as e:
            print("auth fail {}".format(e))
            return False

    def ldap_auth_v2(self, username, password, search_base, search_filter='cn'):
        if not self.ldap_server_test(): return False, None, None

        conn = Connection(self.ldap_server, user=self._ldap_admin_dn, password=self._ldap_admin_password,
                          check_names=True, lazy=False, raise_exceptions=False)
        conn.open()
        conn.bind()
        res = conn.search(search_base=search_base, search_filter=f'({search_filter}={username})',
                          search_scope=SUBTREE, attributes=[search_filter, 'cn', 'sAMAccountName'], paged_size=5)
        if not res: return False, None, None
        entry = conn.response[0]
        dn = entry['dn']
        attr_dict = entry['attributes']

        # check password by dn
        try:
            conn2 = Connection(self.ldap_server, user=dn, password=password, check_names=True, lazy=False,
                               raise_exceptions=False)
            conn2.bind()
            if conn2.result["description"] == "success":
                try:
                    if 'email' in attr_dict and isinstance(attr_dict["email"], list) and attr_dict["email"]:
                        email = attr_dict["email"][0]
                    elif 'email' in attr_dict and not isinstance(attr_dict["email"], list) and attr_dict["email"]:
                        email = attr_dict["email"]
                    elif 'mail' in attr_dict and isinstance(attr_dict["mail"], list) and attr_dict["mail"]:
                        email = attr_dict["mail"][0]
                    elif 'mail' in attr_dict and not isinstance(attr_dict["mail"], list) and attr_dict["mail"]:
                        email = attr_dict["mail"]
                    else:
                        email = None
                except Exception as err:
                    print(f"email fail, {err}")
                    email = None

                return True, attr_dict[search_filter], email
            else:
                print("auth fail")
                return False, None, None
        except Exception as e:
            print("auth fail {}".format(e))
            return False, None, None

    def ldap_auth_v3(self, username, password, search_base, conf_attr_dict, search_filter='cn'):
        # 用户  密码  用户ou 映射数据  查询过滤 应和登录的账户关联
        if not self.ldap_server_test():
            return False, None

        conn = Connection(self.ldap_server, user=self._ldap_admin_dn, password=self._ldap_admin_password,
                          check_names=True, lazy=False, raise_exceptions=False)
        conn.open()
        conn.bind()
        try:
            if isinstance(conf_attr_dict, str): conf_attr_dict = json.loads(conf_attr_dict)
            attr_list = list(conf_attr_dict.values())
        except Exception as err:
            attr_list = ['cn', 'sAMAccountName']
        res = conn.search(search_base=search_base, search_filter=f'({search_filter}={username})',
                          search_scope=SUBTREE, attributes=attr_list, paged_size=1000)

        if not res:
            return False, None
        entry = conn.response[0]
        dn = entry['dn']
        attr_dict = entry['attributes']

        # check password by dn
        try:
            conn2 = Connection(self.ldap_server, user=dn, password=password, check_names=True, lazy=False,
                               raise_exceptions=False)
            conn2.bind()
            if conn2.result["description"] == "success":
                return True, {k: attr_dict.get(v) for k, v in conf_attr_dict.items()}
            else:
                print("auth fail 2")
                return False, None
        except Exception as e:
            print(f"auth fail 3 {e}")
            return False, None


class LdapApiV4:
    def __init__(self, ldap_server_host: str, ldap_admin_dn: str, ldap_admin_password: str,
                 ldap_server_port: int = 389, ldap_use_ssl: Union[bool, str] = False):
        self._ldap_admin_dn = ldap_admin_dn
        self._ldap_admin_password = ldap_admin_password
        self.ldap_server = Server(ldap_server_host, port=ldap_server_port,
                                  use_ssl=str(ldap_use_ssl).lower() in {'y', 'yes', 'true'})

    def test_server_connection(self) -> bool:
        try:
            with Connection(self.ldap_server, self._ldap_admin_dn, self._ldap_admin_password, auto_bind=True) as conn:
                return conn.bound
        except Exception as e:
            logging.error(f"Server connection failed: {e}")
            return False

    def ldap_auth(self, username: str, password: str, search_base: str,
                  attribute_map: Union[Dict[str, str], str, None] = None,
                  search_filter: str = 'cn') -> Tuple[bool, Optional[Dict]]:
        if not self.test_server_connection():
            return False, None
        try:
            with Connection(self.ldap_server, self._ldap_admin_dn, self._ldap_admin_password) as conn:
                if not conn.search(search_base, f'({search_filter}={username})', SUBTREE, attributes=ALL_ATTRIBUTES):
                    return False, None
                user_attrs, user_dn = conn.entries[0].entry_attributes_as_dict, conn.entries[0].entry_dn

                try:
                    with Connection(self.ldap_server, user=user_dn, password=password, auto_bind=True) as uc:
                        if not uc.bound:
                            return False, None
                except Exception as e:
                    logging.error(f"User auth failed: {e}")
                    return False, None

                final_attrs = user_attrs
                if attribute_map:
                    if isinstance(attribute_map, str):
                        try:
                            attribute_map = json.loads(attribute_map)
                        except json.JSONDecodeError:
                            attribute_map = None
                    if isinstance(attribute_map, dict):
                        final_attrs = {k: (v[0] if isinstance(v := user_attrs.get(mv), list) else v)
                                       for k, mv in attribute_map.items()}
                return True, final_attrs
        except Exception as e:
            logging.error(f"Auth error: {e}")
            return False, None


if __name__ == "__main__":
    obj = LdapApiV4('172.16.0.102', 'cn=Manager,DC=sz,DC=com', '070068')
    print(obj.test_server_connection())
    print('____________')
    print(obj.ldap_auth("yanghongfei", "123456", 'ou=opendevops,dc=sz,dc=com', 'cn'))
