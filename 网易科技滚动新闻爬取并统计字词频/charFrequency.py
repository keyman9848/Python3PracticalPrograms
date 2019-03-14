#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 18:30
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : charFrequency.py
# @Software: PyCharm

import jieba
import collections

txt = open('news.txt', 'r', encoding='utf-8').read()

txt1 = txt
txt1 = txt1.replace('\n', '')  # 删掉换行符
txt1 = txt1.replace(' ', '')

print(txt1)
mylist = list(txt1)
charCount = collections.Counter(mylist)

with open('新闻字频统计.txt', 'w', encoding='utf-8') as f:
	for key, val in charCount.most_common():
		print(key, val)
		f.write(key + '    ' + str(val))
		f.write('\n')

	print('统计完成！')