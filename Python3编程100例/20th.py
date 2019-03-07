#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 22:10
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : 20th.py
# @Software: PyCharm

# 初始距离
distance = 100

total = 0

total += distance

# 第10次落地时，经历了9次弹起到落地
for i in range(9):
	distance /= 2
	total += 2 * distance

print('总共经过距离: ', total)
print('第10次反弹距离: ', distance / 2)