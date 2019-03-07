#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-3 12:10
# @Author  : Manu
# @Site    : 
# @File    : bonus.py
# @Software: PyCharm

while True:
    profit = int(input("Input the profit"))
    print("利润是 %d 万元" % profit)
    if profit <= 10:
        bonus = profit * 0.1
    elif profit > 10 and profit < 20:
        bonus = 10 * 0.1 + (profit - 10) * 0.075;
    elif profit >= 20 and profit < 40:
        bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (profit - 20)
    elif profit >= 40 and profit < 60:
        bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (profit - 40)
    elif profit >= 60 and profit < 100:
        10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (60 - 40) + (profit - 60) * 0.015
    else:
        bonus = 10 * 0.1 + (20 - 10) * 0.075 + 0.05 * (40 - 20) + 0.03 * (60 - 40) + (100 - 60) * 0.015 + (profit - 100) * 0.01

    print("奖金是 %f 万元" %bonus)