#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-7 18:54
# @Author  : Manu
# @Site    : 
# @File    : wait1s_format.py
# @Software: PyCharm

import time

print('当前时间:')
print(time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))
time.sleep(1)
print('等待一秒后时间:')
print(time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))