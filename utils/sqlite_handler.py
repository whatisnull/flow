# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/3/27
"""

import config
import sqlite3
import logging
from common.retry import Retry
from common.singleton import Singleton

logging.basicConfig(format="%(asctime)s : %(name)s: %(levelname)s : %(message)s", level=logging.INFO)
log = logging.getLogger("crawler")


@Singleton
class SqliteHandler(object):
    writer = None

    def __init__(self):
        self.get_client()

    @Retry(max_retries=10, return_on_failure=False)
    def connect(self):
        return sqlite3.connect(config.FLOW_DB, isolation_level=None)

    def get_client(self):
        if not self.writer:
            self.writer = self.connect()
