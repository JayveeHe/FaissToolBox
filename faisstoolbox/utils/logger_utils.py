# coding=utf-8

"""
Created by jayvee on 2020/8/16.
https://github.com/JayveeHe
"""


import datetime
import logging
# import os
# import sys

# PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PARENT_PATH)
# PROJECT_PATH = PARENT_PATH
# # print('Relate file: %s, \tPROJECT path = %s\nPARENT PATH = %s' % (__file__, PROJECT_PATH, PARENT_PATH))
# sys.path.append(PROJECT_PATH)

date_str = datetime.datetime.now().strftime('%Y-%m-%d')
log_console = logging.StreamHandler()
# LOG_PATH = '%s/logs' % PROJECT_PATH
# if not os.path.exists(LOG_PATH):
#     os.mkdir(LOG_PATH)
# log_file = logging.FileHandler('%s/%s.log' % (LOG_PATH, date_str))
default_logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '[%(asctime)s][pid:%(process)s-tid:%(thread)s] %(module)s.%(funcName)s: %(levelname)s: %(message)s')
log_console.setFormatter(formatter)
# log_file.setFormatter(formatter)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)
# default_logger.addHandler(log_file)
