#!/usr/bin/env python3
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
  文件操作demo
"""

import os, sys



# 文件打开
def file_open(path):
    f = open(path, 'a+')
    f.write('Hello, world!')
    f.seek(0)
    print(f.read())
    f.close()

# 路径添加
def path_add():
    sys.path.append('..')
    print("append ..:", sys.path)

# 路径设置
def path_demo():
    print('name:',  os.name)
    print('uname:', os.uname)
    print('environ:',  os.environ)
    print('environ:',  os.environ.get('PATH'))
    path = os.path.abspath('.')
    print("abspath:", path)
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    dir_path = os.path.join(path, 'testdir')
    print("dir_path:", dir_path)
    # 然后创建一个目录:
    os.mkdir(dir_path)
    # 删掉一个目录:
    os.rmdir(dir_path)


# main
if __name__ == '__main__':
    file_open('test.txt')
    path_add()
    path_demo()
    