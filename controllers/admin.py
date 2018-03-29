# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-4.
"""

import random
import logging
from utils import *
import tornado.httpclient
from model.admin import AdminModel as model

log = logging.getLogger('flow-ctr-admin-controller')


# 小流量管理
class FlowAdminHandler(tornado.web.RequestHandler):
    def get(self):
        title = "flow service"
        flows = model().get_all_flows()
        self.render('index.html', flows=flows, title=title)


# 小流量添加
class FlowAddHandler(tornado.web.RequestHandler):
    title = "flow service new"

    def get(self):
        self.render("add.html", title=self.title)

    def post(self):
        req = []
        params = ['ratio', 'desc', 'host', 'status', ]
        for k in params:
            v = self.get_argument(k)
            req.append(v)

        if req:
            # get signs by fid=0
            signs = [sign for sign, in model().get_no_bind_fid_sign_by_flow_dict()]

            # current ratio compare with len(signs)
            ratio = self.get_argument('ratio')
            count = len(signs) if int(ratio) > len(signs) else int(ratio)

            # random sign
            result = random.sample(signs, int(count))
            signs_str = '"' + '","'.join(result) + '"'

            req.extend([signs_str, get_time_str(), get_time_str()])

            # to flow_control
            fid = model().insert_flow_base_to_db(req)

            # bind sign
            model().bind_fid_to_sign(fid, signs_str)

        self.redirect('/admin')


# 小流量编辑
class FlowEditHandler(tornado.web.RequestHandler):
    def get(self):
        fid = self.get_argument('fid')
        if not fid:
            log.warn('invalid fid and goto admin page')
            self.redirect('/admin')
        flow = model().get_flow_base(fid)
        self.render("edit.html", flow=flow)

    def post(self):
        req = []
        params = ['ratio', 'host', 'desc', 'status', ]
        for k in params:
            v = self.get_argument(k)
            req.append(v)
        if req:
            req.extend([get_time_str(), self.get_argument('fid')])
            model().update_flow_base(req)
        self.redirect('/admin')


# 小流量删除
class FlowDelHandler(tornado.web.RequestHandler):
    def get(self):
        fid = self.get_argument('fid')
        if not fid:
            log.warn('invalid fid and goto admin page')
            self.redirect('/admin')

        # del flow id
        model().delete_flow_by_id(fid)

        # reset flow id to 0
        model().reset_flow_to_default(fid)
        self.redirect('/admin')

    post = get


# 小流量生效，失效
class FlowEffectHandler(tornado.web.RequestHandler):
    def get(self):
        fid = self.get_argument('fid')
        if not fid:
            log.warn('invalid fid and goto admin page')
            self.redirect('/admin')

        flag = 0
        status = str(self.get_argument('status', 'no')).lower()
        if status == 'yes':
            flag = 1

        model().update_flow_status([flag, fid])

        self.redirect('/admin')


# data and table init
class FlowInitHandler(tornado.web.RequestHandler):
    def get(self):
        status = self.get_argument('status')
        if not status:
            log.warn('invalid status and goto admin page')
            self.redirect('/admin')

        if status == 'yes':
            model().init_db()
            model().init_table_data()

        self.redirect('/admin')

    post = get
