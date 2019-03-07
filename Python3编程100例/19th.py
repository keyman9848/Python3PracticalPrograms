#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 21:57
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : nineteen.py
# @Software: PyCharm


for num in range(2, 1001):
	arr = []
	for i in range(1, num):
		if num % i == 0:
			arr.append(i)
	if sum(arr) == num:
		print(num, arr)


