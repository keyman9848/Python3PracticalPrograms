#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-7 19:06
# @Author  : Manu
# @Site    : 
# @File    : prime_number.py
# @Software: PyCharm

import math

flag = False
count = 0
for i in range(101, 201):
    for j in range(2, int(math.sqrt(i + 1)) + 1):
        if i % j == 0:
            flag = True
            break
    if flag == False:
        count += 1
        print(i, end='\t')
        if count % 5 == 0:
            print()
    flag = False