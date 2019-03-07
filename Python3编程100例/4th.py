#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 14:10
# @Author  : Manu
# @Site    : 
# @File    : day.py
# @Software: PyCharm

list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    year = int(input('输入年份'))
    month = int(input('输入月份'))
    day = int(input('输入日期'))
    sum = 0

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        for i in range(month - 1):
            sum += list2[i]
        sum += day
    else:
        for i in range(month - 1):
            sum += list1[i]
        sum += day

    print('这是第 %d 天' %sum)