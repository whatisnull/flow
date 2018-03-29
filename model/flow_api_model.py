# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-6-3.
"""

import sys
import logging
import traceback
from flow import config
from common.redis_service import RedisReaderService

log = logging.getLogger("flow-ctr-model")


def get_flow_url(uid, times=0):
    if times > 3:
        return None
    try:
        redis_reader = RedisReaderService()

        # check marked user use marked fid
        sign = None
        fid = redis_reader.reader.get(config.MARKED_UID_FID_PREFIX.format(uid=uid))
        log.info('check current uid: %s is marked user, and get marked fid: %s' % (uid, fid))
        if not fid:
            # other users get fid used by hash rule and sublist
            sign = str(hash(uid))[-2:]
            fid = redis_reader.reader.get(config.UID_FID_PREFIX.format(uid=sign))

        key = config.FID_KEY_PREFIX.format(fid=fid)
        host = redis_reader.reader.hget(key, 'host')
        log.info('from uid: %s, get sign: %s, get fid: %s, get host: %s' % (uid, sign, fid, host))

        return host
    except:
        t, v, tb = sys.exc_info()
        log.error("get_flow_url has error: %s,%s,%s" % (t, v, traceback.format_tb(tb)))
        return get_flow_url(uid, times + 1)
