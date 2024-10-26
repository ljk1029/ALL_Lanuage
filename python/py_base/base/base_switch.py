#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： 选择分支使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

# if选择
def if_demo(number = 1)->str:
    age = number
    if age >= 18:
        print(age, 'adult')
    elif age >= 6:
        print(age, 'teenager')
    else:
        print(age, 'kid')
    return str(age)

# for循环
def for_demo()->int:
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum + x
    print(sum)
    return sum

# while循环
def while_demo()->int:
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)
    return sum


# main
if __name__ == '__main__':
    if_demo()
    for_demo()
    while_demo()
 