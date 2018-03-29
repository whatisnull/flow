# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-4.
"""

import sys
import logging
import MySQLdb
import traceback
from flow import config
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor
from common.singleton import Singleton


log = logging.getLogger('flow-ctr-admin-model')

@Singleton
class AdminModel(object):

    reader = None
    writer = None

    def __init__(self):
        pass

    def connect_reader(self):
        if not self.reader:
            pool = PooledDB(MySQLdb, 10, host=config.db_host, port=config.db_port, user=config.db_user,
                            passwd=config.db_passwd, db=config.db_name, autocommit=True, charset="utf8", cursorclass=DictCursor)
            self.reader = pool.connection()

    def connect_writer(self):
        if not self.writer:
            pool = PooledDB(MySQLdb, 10, host=config.db_host, port=config.db_port, user=config.db_user,
                            passwd=config.db_passwd, db=config.db_name, autocommit=True, charset="utf8")
            self.writer = pool.connection()

    def get_all_fids(self, times=0):
        if times>3:
            return []
        try:
            self.connect_reader()
            sql = 'select * from flow_control;'
            cursor = self.reader.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            t, v, tb = sys.exc_info()
            log.error("get_all_fids has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.get_all_fids(times + 1)

    def get_flow_base(self, fid, times=0):
        if times > 3 :
            return None
        try:
            self.connect_reader()
            sql = 'select * from flow_control where fid=%s;'
            cursor = self.reader.cursor()
            cursor.execute(sql, [fid])
            return cursor.fetchone()
        except:
            t, v, tb = sys.exc_info()
            log.error("get_flow_base has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.get_flow_base(fid, times + 1)

    def add_flow_base_to_db(self, req, times=0):
        if times > 3:
            return False
        try:
            self.connect_writer()
            sql = 'insert ignore into flow_control(fid, ratio, host, is_default, fid_desc, status, create_time) values (%s, %s, %s, %s, %s, %s, now()) ;'
            cursor = self.writer.cursor()
            cursor.execute(sql, req)
        except:
            t, v, tb = sys.exc_info()
            log.error("add_flow_base_to_db has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.add_flow_base_to_db(req, times + 1)

    def update_flow_base(self, req, times=0):
        if times > 3:
            return False
        try:
            self.connect_writer()
            sql = 'update flow_control set ratio=%s, host=%s, is_default=%s, fid_desc=%s, status=%s where fid=%s;'
            cursor = self.writer.cursor()
            cursor.execute(sql, req)
        except:
            t, v, tb = sys.exc_info()
            log.error("update_flow_base has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.update_flow_base(req, times + 1)

    def update_flow_status(self, req, times=0):
        if times > 3:
            return False
        try:
            self.connect_writer()
            sql = 'update flow_control set status=%s where fid=%s;'
            cursor = self.writer.cursor()
            cursor.execute(sql, req)
        except:
            t, v, tb = sys.exc_info()
            log.error("update_flow_status has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.update_flow_status(req, times + 1)

    def delete_flow(self, fid, times=0):
        if times > 3:
            return False
        try:
            self.connect_writer()
            sql = 'delete from flow_control where fid=%s;'
            cursor = self.writer.cursor()
            cursor.execute(sql, [fid])
        except:
            t, v, tb = sys.exc_info()
            log.error("delete_flow has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
            return self.delete_flow(times + 1)







