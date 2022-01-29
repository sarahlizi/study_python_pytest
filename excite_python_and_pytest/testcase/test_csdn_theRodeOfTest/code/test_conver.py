"""
# @Time : 2022-01-27 13:20 

# @Author : sarah

# @File : test_conver.py 

# @Software: PyCharm
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testcase.test_csdn_theRodeOfTest.code.cau import *

class Test_cover:
    def test_add(self):
        a=cau(1,2,3)
        assert a==3

    # def test_java(self):
    #     a=Fribonacci(1)
    #     assert a==1