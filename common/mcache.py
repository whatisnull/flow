# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2017/6/7
"""

import time
import logging

logging.basicConfig(format="%(asctime)s : %(name)s: %(levelname)s : %(message)s", level=logging.INFO)
log = logging.getLogger("cache")


def cache(expired=36 * 10, *args, **kwargs):

    # 检查缓存是否无效（缓存数据为空或过期时间已到）
    invalid = lambda data, expired_time, flush: data is None or time.time() > expired_time or flush

    def cache_decorator(func, *args, **kwargs):

        tmp_cache = {}

        def cache_wrapper(*args, **kwargs):

            key = kwargs.get('key')
            flush = kwargs.get('flush', False)
            # 尝试取缓存结果和过期时间信息
            data = tmp_cache.get(key, {}).get('data', None)
            expired_time = tmp_cache.get(key, {}).get('exp', 0)

            # 缓存无效则重新生成缓存
            if invalid(data, expired_time, flush):
                log.warn('rebuild cache for key: %s', key)
                tmp_cache[key] = {}

                tmp_cache[key]['data'] = func(*args, **kwargs)  # 缓存结果
                tmp_cache[key]['exp'] = time.time() + expired  # 计算过期时间

            return tmp_cache[key]['data']

        return cache_wrapper

    return cache_decorator



# @cache()
# def test(a=2, b=3, **kwargs):
#     print a, b
#     return a + b
#
# print test(a=1, b=3, key="a")
# print test(a=1, b=3, key="a")
# print test(a=1, b=3, key="b")
