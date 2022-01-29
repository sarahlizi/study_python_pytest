#coding=utf-8

"""
# @Time : 2022-01-27 11:12 

# @Author : sarah

# @File : test_pytest_xfail.py 

# @Software: PyCharm
"""

import pytest

class Test_Pytest_Xfail():

        def test_one(self,):
                print("----start------")
                pytest.xfail(reason='该功能尚未完成')
                print("test_one方法执行" )
                assert 1==1

        def test_two(self):
                print("test_two方法执行" )
                assert "o" in "love"

        def test_three(self):
                print("test_three方法执行" )
                assert 3-2==1

if __name__=="__main__":
    pytest.main(['-s','-r','test_pytest_xfail.py','test_pytest_xfail.py'])

