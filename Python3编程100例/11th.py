#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018-10-10 8:49
# @Author  : Manu
# @Site    : 
# @File    : rabbit_num.py
# @Software: PyCharm


def rabbit_num(month):
    if month == 1 or month == 2:
        return 1
    else:
        return rabbit_num(month-2) + rabbit_num(month-1)

while True:
    month = input('输入第几个月')
    if month.isdigit():
        month = int(month)
        print('第 %d 个月的兔子数为 %d 对' %(month, rabbit_num(month)))
    elif month == 'q':
        break
    else:
        print('输入错误，请重新输入')
