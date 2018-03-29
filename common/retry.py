# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2017/6/7
"""


import sys
import time
import logging
import traceback

logging.basicConfig(format="%(asctime)s : %(name)s: %(levelname)s : %(message)s", level=logging.INFO)
log = logging.getLogger("Retry")


class Retry(object):
    def __init__(self, max_retries=3, return_on_failure=None, hooks=None, sleeps=0.001):
        """
        """
        self._max_retries = max_retries
        self._return_on_failure = return_on_failure
        self._hooks = hooks
        self.sleeps = sleeps

    def __call__(self, function):

        def wrapper(*args, **kwargs):
            times = 0
            while times < self._max_retries:
                try:
                    log.info("This is %s time run function %s" % (times+1, function.__name__))
                    return function(*args, **kwargs)
                except:
                    t, v, tb = sys.exc_info()
                    log.error("%s, %s, %s, %s" % (function.__name__, t, v, traceback.format_tb(tb)))
                    time.sleep(self.sleeps)
                    times += 1
                    if times >= self._max_retries:
                        return self._return_on_failure

        return wrapper