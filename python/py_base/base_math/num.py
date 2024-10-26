#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： 图像处理使用说明

作者： ljk
日期： 2023/01/01

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

from PIL import Image
 
# 图像处理
def pillow_test():
    im = Image.open('test.png')
    print(im.format, im.size, im.mode)  
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')


# main
if __name__ == '__main__':
    pillow_test()