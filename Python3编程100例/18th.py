#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 21:46
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : eighteen.py
# @Software: PyCharm

num = input('输入重复的数字:\n')
times = int(input('你要重复的次数:\n'))

answer = 0
for i in range(times):
	answer += int(num)
	num += num[0]

print('结果为: ', answer)
