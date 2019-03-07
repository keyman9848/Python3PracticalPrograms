#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018-10-8 18:41
# @Author  : Manu
# @Site    : 
# @File    : Prime.py
# @Software: PyCharm

def prime(n):
    print(str(n) + ' = ')
    if not isinstance(n, int) or n <= 0 :
        print('Please input a valid number !')
        exit(0)
    elif n in [1] :
        print(n)
    while n not in [1]:
        for index in range(2, int(n + 1)):
            if n % index == 0:
                n /= index
                if n == 1:
                    print(index)
                else :
                    print(str(index) + " *", end=' ')
                break

num = input('Input the num, enter "q" to quit：')
while num != 'q':
    prime(int(num))
    num = input('Input the num：')