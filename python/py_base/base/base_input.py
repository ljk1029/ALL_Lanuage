#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
说明文档：

作者： ljk
日期:  2024/01/23

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2

功能：
  输入输出demo
"""

import argparse



"""
函数创建了一个 ArgumentParser 对象，并使用 add_argument 方法来添加两个参数：
--logPath 和 --output。
其中，--logPath 参数被设置为必需的
"""
# python3 base_input.py --logPath l --logName s
# 输入参数
def input_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logPath", required=True, help="Specify the log path.")
    parser.add_argument("--logName", help="Specify the log path.")
    args = parser.parse_args()
    print("Log file path:", args.logPath)
    print("Log file name:", args.logName)
    return args

# 控制台输入
def input_demo():
    s = input('请输入生日年份: ')
    birth = int(s)
    if birth < 2000:
        print('00 前')
    else:
        print('00 后')


# main
if __name__ == '__main__':
    # 使用示例
    args = input_parse()
   
    # 输入测试
    input_demo()
