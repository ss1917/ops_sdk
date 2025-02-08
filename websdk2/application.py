#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : ming
date   : 2018年1月12日13:43:27
role   : 定制 Application
"""

import logging
from abc import ABC
from shortuuid import uuid
from tornado import httpserver, ioloop
from tornado import options as tnd_options
from tornado.options import options, define
from tornado.web import Application as tornadoApp
from tornado.web import RequestHandler
from .configs import configs
from .logger import init_logging

# options.log_file_prefix = "/tmp/codo.log"
define("addr", default='0.0.0.0', help="run on the given ip address", type=str)
define("port", default=8000, help="run on the given port", type=int)
define("progid", default=str(uuid()), help="tornado progress id", type=str)
init_logging()
urls_meta_list = []


class Application(tornadoApp):
    """ 定制 Tornado Application 集成日志、sqlalchemy 等功能 """

    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        tnd_options.parse_command_line()
        handlers = handlers or []
        if configs.can_import:
            configs.import_dict(**settings)

        handlers.extend([(r"/v1/probe/meta/urls/", MetaProbe), ])

        self._generate_url_metadata(handlers)

        max_buffer_size = configs.get('max_buffer_size')
        max_body_size = configs.get('max_body_size')
        super(Application, self).__init__(handlers, default_host, transforms, **configs)
        http_server = httpserver.HTTPServer(self, max_buffer_size=max_buffer_size, max_body_size=max_body_size)
        http_server.listen(options.port, address=options.addr)
        self.io_loop = ioloop.IOLoop.instance()

    def start_server(self):
        """
        启动 tornado 服务
        :return:
        """
        try:
            logging.info('server address: %(addr)s:%(port)d' % dict(addr=options.addr, port=options.port))
            logging.info('web server start sucessfuled.')
            self.io_loop.start()
        except KeyboardInterrupt:
            self.io_loop.stop()
            logging.info("Server shut down gracefully.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}", exc_info=True)

    @staticmethod
    def _generate_url_metadata(urls):
        """Generate metadata for registered URLs."""
        for url in urls:
            meta = {
                "url": url[0],
                "name": url[2].get("handle_name", "暂无")[:30] if len(url) > 2 else "暂无",
                "method": url[2].get("method", []) if len(url) > 2 else [],
                "status": url[2].get("handle_status", "y")[:2] if len(url) > 2 else "y",
            }
            urls_meta_list.append(meta)


class MetaProbe(ABC, RequestHandler):
    def head(self, *args, **kwargs):
        self._write_response()

    def get(self, *args, **kwargs):
        self._write_response()

    def _write_response(self):
        self.write({
            "code": 0,
            "msg": "Get success",
            "count": len(urls_meta_list),
            "data": urls_meta_list,
        })


if __name__ == '__main__':
    pass
