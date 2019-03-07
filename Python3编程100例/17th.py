#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 21:37
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : seventeen.py
# @Software: PyCharm

import string

s = input('请输入字符串:\n')
num_letter = 0
num_space = 0
num_digit = 0
num_other = 0

for i in range(len(s)):
	if s[i].isspace():
		num_space += 1
	elif s[i].isdigit():
		num_digit += 1
	elif s[i].isalpha():
		num_letter += 1
	else:
		num_other += 1

print('character: ', num_letter)
print('space: ', num_space)
print('digit: ', num_digit)
print('other: ', num_other)