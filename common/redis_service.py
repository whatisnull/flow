# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-5-24.
"""
import redis
from singleton import Singleton

class RedisBseService(object):

    _pool = redis.ConnectionPool(max_connections=5, host="192.168.1.110", port=6379, db=10, password='algorithm')

@Singleton
class RedisReaderService(RedisBseService):

    reader = None

    def __init__(self):
        if not self.reader:
            self.get_client()

    def get_client(self):
        if not self.reader:
            self.reader = redis.Redis(connection_pool=self._pool)

@Singleton
class RedisWriterService(RedisBseService):

    writer = None

    def __init__(self):
        if not self.writer:
            self.get_client()

    def get_client(self):
        if not self.writer:
            self.writer = redis.Redis(connection_pool=self._pool)
