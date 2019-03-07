#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 11:10
# @Author  : Manu
# @Site    : 
# @File    : group.py
# @Software: PyCharm

count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and k != j:
                print(i, j, k)
                count += 1

print("组成的数共有：%d 个" % count)