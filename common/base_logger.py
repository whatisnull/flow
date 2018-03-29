# -*- coding: utf-8 -*-

"""
 Created by wangwf on 17-5-24.
"""

"""
from common.base_logger import logging
log = logging.getLogger("test")
"""


import os
import logging.config

logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "./logging.conf"))
