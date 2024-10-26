#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect
import datetime
import os


class CustomLogger:
    log_version = 'mylog version 1.0.1'
    log_default = 'mylog'
   
    # 初始化日志配置
    def __init__(self, log_to_disk=True, log_dir=None, log_name=None, max_size=5*1024*1024):
        self.log_to_disk = log_to_disk
        self.log_dir = log_dir or os.getcwd()
        os.makedirs(self.log_dir, exist_ok=True) # 创建log_dir（如果不存在）
        self.max_size = max_size
        self.log_name = log_name or CustomLogger.log_default
        self.log_file = f"{self.log_name}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]}.log"
        self.log_path = os.path.join(self.log_dir, self.log_file)
        
    # 打印和记录日志
    def log(self, *args, **kwargs) -> str:
        frame = inspect.currentframe().f_back
        filename = os.path.basename(frame.f_code.co_filename)
        lineno = frame.f_lineno
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = f"[{now} - {filename}:{lineno}]"
        message = ' '.join(str(arg) for arg in args)
        full_message = f"{prefix} {message}"

        if self.log_to_disk:
            self._write_to_disk(full_message)
        
        print(full_message, **kwargs)
        return full_message
    
    # 写入日志文件
    def _write_to_disk(self, message) -> bool:
        if os.path.exists(self.log_path) and os.path.getsize(self.log_path) >= self.max_size:
            self._roll_log_files()
        
        with open(self.log_path, 'a') as log_file:
            log_file.write(message + "\n")
    
    # 日志滚动, mode 滚动实现/删除实现
    def _roll_log_files(self, mode=True) -> bool:
        if mode:
            self.log_file = f"{self.log_name}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]}.log"
            self.log_path = os.path.join(self.log_dir, self.log_file)
        elif os.path.exists(self.log_path):
            os.remove(self.log_path)
        return mode

    # 临时实例化日志方法
    @classmethod
    def static_log(cls, *args, **kwargs) -> str:
        temp_logger = cls(log_to_disk=False)
        return temp_logger.log(*args, **kwargs)

    # 静态方法，无需实例化
    @staticmethod
    def static_version() -> str:
        print(CustomLogger.log_version)
        return CustomLogger.log_version


# 测试用例
if __name__ == '__main__':
    # 默认记录到磁盘
    logger = CustomLogger(log_dir = '../1/')  
    for i in range(10):
        logger.log(i, 'This is an info message.')
        CustomLogger.static_version()  
        CustomLogger.static_log('This is printed directly without disk logging.')  # 不记录到磁盘
        CustomLogger.static_log('This is printed directly without disk logging.')  
        logger.log('This is an error message.')