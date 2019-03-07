#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018-10-10 8:25
# @Author  : Manu
# @Site    : 
# @File    : narcissistic_num.py
# @Software: PyCharm


print('水仙花数列表:')
for i in range(100, 1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100

    if i == (ge ** 3 + shi ** 3 + bai ** 3):
        print(i)