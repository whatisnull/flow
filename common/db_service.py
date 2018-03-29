# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-5-24.
"""

# -*- coding: utf-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB


class DatabaseService(object):

    pools = {}

    def __init__(self, database_configs, max_connection=8):
        """
        :param database_configs: configuration of database. it's dict of dict with following format:
        {
            'zhisland_base': {
                'host': "192.168.2.46",
                'user': "base",
                'port': 3306,
                'passwd': "zhd_base#x1x3x",
                'db': "zhisland_base"
            },
            'address_book': {
                'host': "192.168.2.46",
                'user': "base",
                'port': 3306,
                'passwd': "zhd_base#x1x3x",
                'db': "zhd_user_addressbook"
            }
        }
        :param max_connection: maximum number of connections generally allowed per database
        """
        self.database_configs = database_configs
        self.max_connection = max_connection

    def get_connection(self, name):
        if name not in self.pools:
            self.pools[name] = PooledDB(
                MySQLdb, maxconnections=self.max_connection, charset='utf8', **self.database_configs[name])
        return self.pools[name].connection()

    def select(self, database_name, sql, args=None):
        conn = self.get_connection(database_name)
        try:
            cursor = conn.cursor()
            count = cursor.execute(sql, args if args else {})
            rows = cursor.fetchall()
            return count, rows
        finally:
            conn.close()

    def execute_one(self, database_name, sql, args=None):
        conn = self.get_connection(database_name)
        try:
            cursor = conn.cursor()
            cursor.execute(sql, args if args else {})
            conn.commit()
        finally:
            conn.close()

