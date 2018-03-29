# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-3.
"""


import time

def get_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d