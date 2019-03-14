#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 18:30
# @Author  : cunyu
# @Site    : cunyu1943.github.io
# @File    : wordsFrequency.py
# @Software: PyCharm

import os,codecs
import jieba
from collections import Counter

# 获取jieba分词后的列表
def getWords(txt):
	seg_list = jieba.cut(txt)
	c = Counter()
	for x in seg_list:
		if len(x) > 0 and x != '\r\n' and x != ' ':
			c[x] += 1
	wordFreqList = []
	for item in c.most_common():
		wordFreqList.append(item)
	return wordFreqList

if __name__ == '__main__':
	with codecs.open('newsTitle.txt', 'r', 'utf-8') as title_f, codecs.open('newsContent.txt', 'r', 'utf-8') as content_f,codecs.open('news.txt', 'r', 'utf-8') as news_file, \
			codecs.open('标题词频统计.txt', 'w', 'utf-8') as titleFile,codecs.open('正文词频统计.txt', 'w', 'utf-8') as contentFile, codecs.open('新闻词频统计', 'w', 'utf-8') as newsFile:

		title_txt = title_f.read()
		content_txt = content_f.read()
		news_txt = news_file.read()

		title_items = getWords(title_txt)
		content_items = getWords(content_txt)
		news_items = getWords(news_txt)

		print('标题词频统计结果')
		for item in title_items:
			titleFile.write(item[0] + '    ' + str(item[-1]))
			titleFile.write('\n')
		print(title_items)

		print('内容词频统计结果')
		for item in content_items:
			contentFile.write(item[0] + '    ' + str(item[-1]))
			contentFile.write('\n')
		print(content_items)

		print('新闻词频统计结果')
		for item in news_items:
			newsFile.write(item[0] + '    ' + str(item[-1]))
			newsFile.write('\n')
		print(news_items)

		print('统计完成！')