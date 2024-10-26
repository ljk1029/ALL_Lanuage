#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： 时间使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

from datetime import datetime


# time
def time_demo():
    now = datetime.now() # 获取当前 datetime
    print(now)

# main
if __name__ == '__main__':
    time_demo()
    