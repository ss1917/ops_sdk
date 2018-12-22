#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author : shenshuo
date   : 2018年2月6日11:18:40
role   : 解析配置文件
'''

import json
import os
import configparser

def json_to_dict(conf_path):
    if not os.path.isfile(conf_path):
        raise FileNotFoundError('{0} file does not exist'.format(conf_path))

    with open(conf_path, encoding='utf-8') as f:
        try:
            conf_data = json.load(f)
        except ValueError as e:
            raise ValueError('仅解析json格式')
        return conf_data



class IniToDict:
    def __init__(self, conf_path, section):
        self.path = conf_path
        self.sect = section

    def get_option(self, *keys):
        ###判断配置文件path是否存在
        if not os.path.isfile(self.path):
            raise FileNotFoundError('{0} file does not exist'.format(self.path))

        ###解析文件
        fh_conf = configparser.ConfigParser()
        fh_conf.read(self.path)

        ###确认配置文件有无配置层
        list_section = fh_conf.sections()

        res_back = {}
        if self.sect in list_section:
            ###取出section下的所有配置项
            res_list = fh_conf.items(self.sect)

            ###转换成字典
            res_dict = dict(res_list)

            if keys:
                ###取出指定的键
                for k, v in res_dict.items():
                    if k in keys:
                        res_back[k] = v
            else:
                res_back = res_dict
        else:
            raise ValueError('{0} not have {1}'.format(self.path, self.sect))

        ###如果只取一个键，则返回值，其他返回字典
        if keys and len(keys) == 1:
            return res_back.get(keys[0], "")

        return res_back