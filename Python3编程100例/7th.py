#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-10-4 10:20
# @Author  : Manu
# @Site    : 
# @File    : copy.py
# @Software: PyCharm

import copy

# 直接赋值，相当于对象引用，即就是另起一个名字
print('assignment:')
list1 = [1, 3, 5, 7, 9, 'Manu Ginobili', 20]
list2 = list1
print(list2)

# 浅拷贝(copy)，拷贝父对象，不拷贝子对象
print('copy:')
list1 = [1, 3, 5, 7, 9, 'Manu Ginobili', 20]
list2 = list1.copy()

list1.append(21)
print(list1)
print(list2)

list2.append(14)
print(list1)
print(list2)

# 深拷贝(deepcopy)，完全拷贝父对象及子对象
print('Deepcopy:')
list1 = [1, 3, 5, 7, 9, 'Manu Ginobili', 20]
list2 = copy.deepcopy(list1)

list1.append('Duncan')
print(list1)
print(list2)

list2.append('Paker')
print(list1)
print(list2)