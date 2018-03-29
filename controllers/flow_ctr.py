# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-3.
"""
import sys
import json
import logging
import traceback
import tornado.web
import tornado.httpclient
from flow.model import flow_api_model as model

log = logging.getLogger("flow-ctr-index")

class FlowApiHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        uid = self.get_argument('uid', None)
        if not uid:
            self.write(json.dumps(dict(msg="invalid uid", code=404, data=[])))
            self.finish()
            return
        log.info("uri: %s" % self.request.uri)
        try:
            host = model.get_flow_url(uid)
            if not host:
                self.write(json.dumps(dict(msg="service error", code=500, data=[])))
                self.finish()
                return
            client = tornado.httpclient.AsyncHTTPClient()
            client.fetch('%s%s' % (host, self.request.uri), method='GET', body=None,
                         validate_cert=False, callback=self.on_resonse, connect_time=2, request_timeout=2)
        except:
            t, v, tb = sys.exc_info()
            log.error("service has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            self.write(json.dumps(dict(msg="service error", code=500, data=[])))
            self.finish()
            return

    def on_resonse(self, response):
        data = response.body
        if data:
            self.write(data)
        else:
            self.write(json.dumps(dict(msg='no data', code=200, data=[])))
        self.finish()
        return