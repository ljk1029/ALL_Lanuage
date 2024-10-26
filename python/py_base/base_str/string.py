#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
说明文档： 字符串操作使用说明
        正则匹配使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

#split(":")[-1]  以:分割倒数第一元素
#strip() 去掉二端空格
#strip(“#”) 去掉二端的#号
import re

# 连接
def string_link(pub="1234", sub:str='abcd', index:int=0):
    # 连接
    print(  "连接:" + pub + "---" + sub  + str(index))
    # 转字符
    print( f"转换:{pub}---{sub}---")
    print( ("转换:{}---{}---").format(pub, sub))

# 分割
def string_split():
    my_string = "Hello, World, Python"
    # 使用split方法拆分字符串
    split_result = my_string.split(', ')
    # 打印拆分后的结果
    print("拆分前的字符:", my_string)
    print("拆分后的结果:", split_result)
    print("拆分后的结果[0]:",  split_result[0])
    print("拆分后的结果[1]:",  split_result[1])
    print("拆分后的结果[-1]:", split_result[-1])
    print("拆分后的结果[:-1]:", split_result[:-1])

# 过滤
def string_strip():
    my_string = " Hello, World, Python# "
    # 使用空格过滤
    strip_result = my_string.strip()
    print("过滤前的字符:", my_string)
    print("过滤后的字符:", strip_result)
    # 使用#号过滤
    strip_result = strip_result.strip('#')
    print("\'#\'过滤后的结果:", strip_result)

# 正则
def string_regular():
    log_data = """
    01-25 14:03:28.156 793252 793253 I EXE-TASK for Performance: Process: user_cpu:957, sys_cpu:93, total_cpu:109506067, memory:275697664
    01-25 14:03:28.156 793252 793253 I EXE-TASK for Performance: Process: user_cpu:956, sys_cpu:94, total_cpu:109506066, memory:275697667
    ... (其他日志行) ...
    """
    # 编写正则表达式以匹配日志中的相应部分
    pattern = re.compile(
        r'Process:\s*user_cpu:(\d+),\s*sys_cpu:(\d+),\s*total_cpu:(\d+),\s*memory:(\d+)'
    )
    # 定义列表来存储匹配的值
    user_cpu_list  = []
    sys_cpu_list   = []
    total_cpu_list = []
    memory_list    = []
    # 分行匹配日志数据
    for line in log_data.split('\n'):
        match = pattern.search(line)
        if match:
            # 将匹配的值添加到相应的列表中
            user_cpu_list.append(int(match.group(1)))
            sys_cpu_list.append(int(match.group(2)))
            total_cpu_list.append(int(match.group(3)))
            memory_list.append(int(match.group(4)))
    # 打印结果以检查
    print("正则匹配：\n", user_cpu_list,  '\n', 
                        sys_cpu_list,   '\n', 
                        total_cpu_list, '\n', 
                        memory_list)


# main
if __name__ == '__main__':
    string_link()
    string_split()
    string_strip()
    string_regular()