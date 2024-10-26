#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： log和调试使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

import logging
# 日志设置
def configure_logging(log_file_path):
    # 创建一个日志记录器
    logger = logging.getLogger()
    # 设置日志级别（DEBUG最详细，CRITICAL最严重）
    logger.setLevel(logging.DEBUG)
    # 创建一个文件处理程序，用于写入日志到文件
    file_handler = logging.FileHandler(log_file_path)
    # 创建一个控制台处理程序，用于将日志打印到控制台
    console_handler = logging.StreamHandler()
    # 创建一个格式化器，定义日志记录的格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # 将格式化器添加到处理程序
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 将处理程序添加到记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
def log_demo():
    # 配置日志，将日志写入到文件 'my_log.log'
    configure_logging('my_log.log')
    # 记录不同级别的日志消息
    logging.debug('这是一个调试消息')
    logging.info('这是一个信息消息')
    logging.warning('这是一个警告消息')
    logging.error('这是一个错误消息')
    logging.critical('这是一个严重错误消息')
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)


   
# main
if __name__ == '__main__':
    log_demo()