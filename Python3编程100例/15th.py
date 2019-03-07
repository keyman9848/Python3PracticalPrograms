#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018-10-10 8:33
# @Author  : Manu
# @Site    : 
# @File    : score_.py
# @Software: PyCharm

print('输入成绩查看登记，输入"q"则退出')
while True:
    score = input('输入你的成绩:')

    if score.isdigit():

        score_rank = int(score) // 10

        if score_rank >= 9:
            print('A')
        elif score_rank >= 6 and score_rank < 9:
            print('B')
        else:
            print('C')
    elif score == 'q':
        break
    else:
        print('输入错误，请重新输入！')