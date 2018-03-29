# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-3.
"""

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

src_path = os.path.dirname(__file__)
if len(src_path) < 1: src_path = "."
sys.path.append(src_path)
sys.path.append(src_path + "/")
sys.path.append(src_path + "/../")

import tornado
import logging
import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from controllers.flow_ctr import FlowApiHandler
from controllers.admin import FlowAdminHandler, FlowAddHandler, FlowEditHandler, FlowEffectHandler, FlowDelHandler, FlowInitHandler

logging.basicConfig(level='INFO', format="[%(asctime)s](%(levelname)s)%(name)s : %(message)s")


def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/admin", FlowAdminHandler),
            (r"/add", FlowAddHandler),
            (r"/edit", FlowEditHandler),
            (r"/delete", FlowDelHandler),
            (r"/effect", FlowEffectHandler),
            (r"/init", FlowInitHandler),
            (r"/.*", FlowApiHandler), ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "public"),
        # autoreload = True,
        # debug = True,
    )


if __name__ == '__main__':
    server = HTTPServer(make_app())
    server.listen(8088)
    IOLoop.current().start()
    server.start(1)
