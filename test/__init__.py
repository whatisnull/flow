# -*- coding: utf-8 -*-
"""
 Created by Dr.W on 2018/3/27
"""

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
f_path = os.path.dirname(__file__)
if len(f_path) < 1: f_path = "."
sys.path.append(f_path)
sys.path.append(f_path + "/..")
sys.path.append(f_path + "/../..")

import logging
import traceback

logging.basicConfig(format="%(asctime)s : %(name)s: %(levelname)s : %(message)s", level=logging.INFO)
log = logging.getLogger("crawler")

if __name__ == '__main__':
    pass