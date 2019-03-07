#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-7 18:38
# @Author  : Manu
# @Site    : 
# @File    : multiple.py
# @Software: PyCharm

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d\t' %(i, j, i * j), end=' ')
    print()