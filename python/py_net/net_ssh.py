#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ssh 功能

import sys
import subprocess


ip_add    = "127.0.0.1"
user_name = "lixiang"


def usage():
    print("用法：")
    print("  {0} ".format(sys.argv[0]))
    print("  : 登录")
    print(" ")

def ssh_remote(ip, name):
    subprocess.call(["ssh", "-l", name, ip])

def sub_run_demo():
    # 执行命令，并等待它完成，然后获取输出
    completed = subprocess.run(['ls', '-l'], text=True, capture_output=True)
    print('ReturnCode:', completed.returncode)
    print('Have error? ', completed.stderr is not None)
    print('Output:', completed.stdout)
    return completed

def sub_popen_demo():
    # 使用Popen执行命令
    process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 等待进程结束并获取输出
    stdout, stderr = process.communicate()
    print('Output:', stdout)
    print('Error:', stderr)
    print('ReturnCode:', process.returncode)

usage()
#exit(0)

if __name__ == '__main__':
    ssh_remote(ip_add, user_name)
    sub_run_demo()
    sub_popen_demo()
