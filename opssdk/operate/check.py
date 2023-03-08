#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
author : shenshuo
date   : 2018年2月5日19:23:09
role   : 检查
"""
import os
import socket
import fcntl
import struct
from opssdk.operate import exec_shell


def check_disk(d='/data1', f=10):
    vfs = os.statvfs(d)
    available = vfs.f_bsize * vfs.f_bavail / 1024 / 1024 / 1024
    if available > f:
        return True
    return False


def check_sys_version():
    recode, res = exec_shell(
        "awk -F'release' '{print $2}' /etc/redhat-release | awk '{print $1}'|awk -F'.' '{print $1}'")
    return res[0]


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])
