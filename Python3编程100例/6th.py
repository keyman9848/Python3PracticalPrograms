#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 21:10
# @Author  : Manu
# @Site    : 
# @File    : fib.py
# @Software: PyCharm

def fib(num):
    if num <= 2:
        result = 1
    else:
        result = fib(num - 1) + fib(num - 2)
    return result

while True:
    num = int(input('num = '))
    print('斐波那契数列的第 %d 个值是 %d' % (num, fib(num)))
