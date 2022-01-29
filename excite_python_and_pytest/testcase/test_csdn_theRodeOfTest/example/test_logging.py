"""
# @Time : 2022-01-27 12:57 

# @Author : sarah

# @File : test_logging.py 

# @Software: PyCharm
"""

import time
import logging

logging.basicConfig(level=logging.DEBUG)

def test_1():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'


def test_2():
    log = logging.getLogger('test_2')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 0, 'failing for demo purposes'
