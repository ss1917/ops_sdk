#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : ming
date   : 2017/4/11 下午3:21
desc   :
'''
import fire


class MainProgram(object):
    def __init__(self, progressid=''):
        print(progressid)

    @staticmethod
    def run(cls_inst):
        if issubclass(cls_inst, MainProgram):
            fire.Fire(cls_inst)
        else:
            raise Exception('')