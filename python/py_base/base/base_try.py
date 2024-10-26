#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： try调试使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""


# try
def trys_demo():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
        print('END')


# main
if __name__ == '__main__':
    trys_demo()