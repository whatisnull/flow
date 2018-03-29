# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/3/27
"""

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
f_path = os.path.dirname(__file__)
if len(f_path) < 1: f_path = "."
sys.path.append(f_path)
sys.path.append(f_path + "/..")
sys.path.append(f_path + "/../..")

import logging
import time
import traceback
import sqlite3

logging.basicConfig(format="%(asctime)s : %(name)s: %(levelname)s : %(message)s", level=logging.INFO)
log = logging.getLogger("crawler")

conn = sqlite3.connect("../data/flow.db", isolation_level=None)
cursor = conn.cursor()


def make_table():
    cursor.execute("DROP TABLE IF EXISTS flow_control;")
    cursor.execute("DROP TABLE IF EXISTS flow_dict;")
    cursor.execute('CREATE TABLE flow_control ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                   'host VARCHAR(255),'
                   'ratio INTEGER(3), '
                   'status INTEGER(1), '
                   'is_default INTEGER(1), '
                   'desc VARCHAR(255), '
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


def insert():
    for i in range(0, 100):
        if i < 10:
            k = '0%d' % i
        else:
            k = i
        bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'insert into flow_dict (sign, fid, status, create_time, update_time) values("%s", "%s", "%s", "%s", "%s");'
        cursor.execute(sql % (k, 0, 0, bt, bt))
        print 'lastrowid: ', cursor.lastrowid, k


def select():
    pass
    sql = "select * from flow_dict where fid=6"
    cursor.execute(sql)
    result = cursor.fetchall()
    print len(result)
    for item in result:
        print item

    # sql = "SELECT sign " \
    #       "FROM flow_dict " \
    #       "WHERE fid=0;"
    #
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # for item, in result:
    #     print item

    # sql = "UPDATE flow_dict set fid=7 where sign in (00,02,03,05,06);"
    # cursor.execute(sql)

if __name__ == '__main__':
    pass
    # make_table()
    # insert()
    select()
