# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-6.
"""


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)