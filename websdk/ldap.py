#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2019/4/17
Desc    : 对接LDAP登录认证
"""

from ldap3 import Server, Connection, ALL, SUBTREE, ServerPool


class LdapApi:
    def __init__(self, ldap_server_host, ldap_admin_dn, ldap_admin_password, ldap_server_port=389, ldap_use_ssl=False):
        self._ldap_admin_dn = ldap_admin_dn
        self._ldap_admin_password = ldap_admin_password
        # ldap_server_pool = ServerPool(["172.16.0.102",'172.16.0.103'])
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

    def ldap_auth(self, username, password, search_base, search_filter='cn'):
        if not self.ldap_server_test():
            return False, None, None

        conn = Connection(self.ldap_server, user=self._ldap_admin_dn, password=self._ldap_admin_password,
                          check_names=True, lazy=False, raise_exceptions=False)
        conn.open()
        conn.bind()

        res = conn.search(search_base=search_base,
                          search_filter='({}={})'.format(search_filter, username),
                          search_scope=SUBTREE,
                          # attributes=['cn', 'givenName', 'email', 'mail', 'sAMAccountName'],
                          attributes=['cn', 'email', 'mail'], paged_size=5)

        if res:
            entry = conn.response[0]
            dn = entry['dn']
            attr_dict = entry['attributes']

            # check password by dn
            try:
                conn2 = Connection(self.ldap_server, user=dn, password=password, check_names=True, lazy=False,
                                   raise_exceptions=False)
                conn2.bind()
                if conn2.result["description"] == "success":
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

                    return True, attr_dict["cn"][0], email
                else:
                    print("auth fail")
                    return False, None, None
            except Exception as e:
                print("auth fail {}".format(e))
                return False, None, None
        else:
            return False, None, None

    def ldap_auth_v2(self, username, password, search_base, search_filter='cn'):
        if not self.ldap_server_test(): return False, None, None

        conn = Connection(self.ldap_server, user=self._ldap_admin_dn, password=self._ldap_admin_password,
                          check_names=True, lazy=False, raise_exceptions=False)
        conn.open()
        conn.bind()

        res = conn.search(search_base=search_base, search_filter=f'({search_filter}={username})',
                          search_scope=SUBTREE, attributes=[search_filter, 'email', 'mail'], paged_size=5)

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

                return True, attr_dict[search_filter][0], email
            else:
                print("auth fail")
                return False, None, None
        except Exception as e:
            print("auth fail {}".format(e))
            return False, None, None


if __name__ == "__main__":
    obj = LdapApi('172.16.0.102', 'cn=Manager,DC=sz,DC=com', '070068')
    print(obj.ldap_server_test())
    print('____________')
    print(obj.ldap_auth("yanghongfei", "123456", 'ou=opendevops,dc=sz,dc=com', 'cn'))
