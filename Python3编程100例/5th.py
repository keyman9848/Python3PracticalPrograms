#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 15:10
# @Author  : Manu
# @Site    : 
# @File    : sortNum.py
# @Software: PyCharm

while True:
    print('Input x, y, z:')
    arr = []
    for i in range(3):
        tmp = int(input())
        arr.append(tmp)
    arr.sort()
    print('三个数从小到大排序: ',  arr)