#!/usr/bin/env python
# -*-coding:utf-8-*-


import logging
import sys
import tornado.log


class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s%(asctime)s | %(levelname)s%(end_color)s     | %(filename)s:%(funcName)s:%(lineno)s - %(message)s',
            datefmt="%Y-%m-%d %H:%M:%S"
        )


def init_logging():
    # write file
    [
        i.setFormatter(LogFormatter())
        for i in logging.getLogger().handlers
    ]
    logging.getLogger().setLevel(logging.INFO)
    # write stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(LogFormatter())
    logging.getLogger().addHandler(stdout_handler)
