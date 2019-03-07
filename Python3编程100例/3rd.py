#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 12:10
# @Author  : Manu
# @Site    : 
# @File    : compSquNum.py
# @Software: PyCharm

res = 168 // 2
for i in range(1, res + 1):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = m * m - 268
			print('这个数可能是: ', x)