"""
# @Time : 2022-01-27 13:20 

# @Author : sarah

# @File : cau.py.py 

# @Software: PyCharm
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  flask
def cau (type,n1, n2):

    if type==1:
        a=n1 + n2
    elif type==2:
        a = n1 - n2
    else:
        a=n1 * n2
    return a
