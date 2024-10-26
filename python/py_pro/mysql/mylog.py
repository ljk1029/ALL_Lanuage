#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Project:   MyLogger
@File:      mylog.py
@Author:    jk.l
@Date:      2024/03/19
"""


import datetime
import inspect 

# 日志系统
class MyLogger:
    def __init__(self, level='INFO', write_to_file=False, file_path='mylog.log'):
        self.level = level
        self.write = write_to_file
        self.path   = file_path
        self.levels = {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}

    # 单日志
    def log(self, level, *args, **kwargs):
        if self.levels[level] >= self.levels[self.level]:
            log_message = f"{datetime.datetime.now()}-{level}: " + ' '.join(map(str, args))
            # 如果kwargs不为空，添加到日志信息中
            if kwargs:
                log_message += " " + ' '.join(f"{k}={v}" for k, v in kwargs.items())
            print(log_message)
            if self.write:
                with open(self.path, 'a') as file:
                    file.write(log_message + '\n')

    # 添加调试行号
    def log_line(self, level, *args, **kwargs):
        if self.levels[level] >= self.levels[self.level]:
            # 获取调用者的堆栈帧
            frame = inspect.currentframe()
            stack = inspect.stack()
            # stack[1]是当前方法（log），所以信息来源是stack[2]
            # index 1是文件路径，index 2是行号
            caller_info = f"{stack[2].filename}:{stack[2].lineno}"
            log_message = f"{datetime.datetime.now()}-{level}-{caller_info}: " + ' '.join(map(str, args))
            # 如果kwargs不为空，添加到日志信息中
            if kwargs:
                log_message += " " + ' '.join(f"{k}={v}" for k, v in kwargs.items())
            print(log_message)
            if self.write:
                with open(self.path, 'a') as file:
                    file.write(log_message + '\n')
            # 清理堆栈帧防止泄露
            del frame, stack

    def debug(self, *args, **kwargs):
        self.log_line('DEBUG', *args, **kwargs)

    def info(self, *args, **kwargs):
        self.log_line('INFO', *args, **kwargs)

    def warning(self, *args, **kwargs):
        self.log_line('WARNING', *args, **kwargs)
        
    def error(self, *args, **kwargs):
        self.log_line('ERROR', *args, **kwargs)
        
    def critical(self, *args, **kwargs):
        self.log_line('CRITICAL', *args, **kwargs)