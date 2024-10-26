#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档：解析输入参数

作者： ljk
日期:  2024/01/23

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2

功能：
  命令行demo
"""

import sys


# 命令行参数
def command_demo():
    args = sys.argv
    if len(args)==1:
        print('%s Hello, world!' % args[0])
    elif len(args)==2:
        print('%s Hello, %s!' % (args[0], args[1]))
    else:
        print('Too many arguments!')

# main
if __name__ == '__main__':
    command_demo()
    