# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-5-24.
"""


def Singleton(cls, *args, **kwargs):

    instances = {}

    def _singleton(*args, **kwargs):

        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return _singleton
