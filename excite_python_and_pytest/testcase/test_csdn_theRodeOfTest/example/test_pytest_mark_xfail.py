"""
# @Time : 2022-01-27 11:18 

# @Author : sarah

# @File : test_pytest_mark_xfail.py 

# @Software: PyCharm
"""

import pytest

class Test_Pytest_mark_Xfail():

        @pytest.mark.xfail
        def test_one(self):
                print("test_one方法执行" )
                assert 1==2

        def test_two(self):
                print("test_two方法执行" )
                assert "o" in "love"

        def test_three(self):
                print("test_three方法执行" )
                assert 3-2==1

if __name__=="__main__":
    pytest.main(['-s','test_pytest_mark_xfail.py'])
