# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/3/27
"""

import logging
from utils import *
from common.retry import Retry
from common.singleton import Singleton
from utils.sqlite_handler import SqliteHandler

log = logging.getLogger("admin-model-ctr")

@Singleton
class AdminModel(object):

    sqlite = SqliteHandler()

    @Retry(return_on_failure=False)
    def init_db(self):
        cursor = self.sqlite.writer.cursor()
        cursor.execute("DROP TABLE IF EXISTS flow_control;")
        cursor.execute("DROP TABLE IF EXISTS flow_dict;")
        cursor.execute('CREATE TABLE flow_control ('
                       'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                       'host VARCHAR(255),'
                       'ratio INTEGER(3), '
                       'status INTEGER(1), '
                       'is_default INTEGER(1), '
                       'desc VARCHAR(255), '
                       'policy VARCHAR (255),'
                       'create_time TEXT, '
                       'update_time TEXT'
                       '); ')

        cursor.execute('CREATE TABLE flow_dict ('
                       'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                       'fid INTEGER(20),'
                       'sign VARCHAR(4) UNIQUE,'
                       'status INTEGER(1), '
                       'create_time TEXT, '
                       'update_time TEXT'
                       '); ')
        return True

    def init_table_data(self):
        cursor = self.sqlite.writer.cursor()
        for i in range(0, 100):
            k = i
            if i < 10:
                k = '0%d' % i
            bt = get_time_str()
            sql = 'insert into flow_dict (sign, fid, status, create_time, update_time) values("%s", "%s", "%s", "%s", "%s");'
            cursor.execute(sql % (k, 0, 0, bt, bt))

    @Retry(return_on_failure=[])
    def get_all_flows(self):
        sql = "SELECT * " \
              "FROM flow_control;"
        self.sqlite.writer.row_factory = dict_factory
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @Retry(return_on_failure=None)
    def get_flow_base(self, fid):
        sql = "SELECT * " \
              "FROM flow_control " \
              "WHERE id=?;"
        self.sqlite.writer.row_factory = dict_factory
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, [fid])
        return cursor.fetchone()

    @Retry(return_on_failure=False)
    def insert_flow_base_to_db(self, req):
        sql = 'INSERT INTO flow_control ' \
              '(ratio, desc, host, status, policy, create_time, update_time) ' \
              'VALUES (?, ?, ?, ?, ?, ?, ?);'

        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, req)
        return cursor.lastrowid

    def reset_flow_to_default(self, fid):
        sql = "UPDATE flow_dict " \
              "SET fid=0 " \
              "WHERE fid=?; "
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, [fid])
        return True

    @Retry(return_on_failure=False)
    def update_flow_base(self, req):
        sql = "UPDATE flow_control SET ratio=?, host=?, is_default=?, desc=?, status=?, update_time=?" \
              "WHERE id=?;"
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, req)
        return True

    @Retry(return_on_failure=False)
    def update_flow_status(self, req):
        sql = "UPDATE flow_control " \
              "SET status=? " \
              "WHERE id=?;"
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, req)
        return True

    @Retry(return_on_failure=False)
    def delete_flow_by_id(self, fid):
        sql = "DELETE " \
              "FROM flow_control  " \
              "WHERE id=?"
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql, [fid])
        return True

    @Retry(return_on_failure=[])
    def get_no_bind_fid_sign_by_flow_dict(self):
        sql = "SELECT sign " \
              "FROM flow_dict " \
              "WHERE fid=0;"
        self.sqlite.writer.row_factory = None
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @Retry(return_on_failure=False)
    def bind_fid_to_sign(self, fid, signs):
        sql = "UPDATE flow_dict set fid=? WHERE sign in (%s);"
        self.sqlite.writer.row_factory = None
        cursor = self.sqlite.writer.cursor()
        cursor.execute(sql % signs, [fid])
        return True

