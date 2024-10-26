#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Project:   MyCommand
@File:      mycmd.py
@Author:    jk.l
@Date:      2024/03/19
"""




import os
import subprocess
import paramiko


# 命令系统
class MyCommand:
    def __init__(self, logger=print, paras:list=['127.0.0.1', 22, 'lixiang', '0']):
        self.log = logger
        self.log(self.__class__.__name__, 'class init')
        self.log(self.__init__.__name__,  'function init')
        self.sshcmd = 'ssh -o "StrictHostKeyChecking no" -o ConnectTimeout=3'
        self.ip     = paras[0]
        self.port   = paras[1]
        self.user   = paras[2]
        self.passwd = paras[3]
        self.log('init:', 'ip', self.ip, 'port', self.port, 'uder', self.user, 'passwd', self.passwd)

    # 恢复默认参数
    def change_init(self, ip:str='127.0.0.1', port:int=22, user:str='lixiang', passwd:str='0'):
        self.ip   = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.log(f'change: {self.user}@{self.ip}:{self.port}  {self.passwd}')

    # paramiko连接检查
    def test_connection(self):
        transport = self.connection.get_transport() if self.connection else None
        return transport and transport.is_active()

    # paramiko连接断开
    def close_connection(self):
        self.connection.sftp.close()
        self.connection.close()

    # paramiko连接建立
    def open_connection(self, ip, port, username, passwd):
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if passwd:
                self.connection.connect(ip, port, username, password=passwd,
                                    look_for_keys=False, allow_agent=False, timeout=5.0)
            else :
                self.connection.connect(ip, port, username, look_for_keys=False, allow_agent=False, timeout=5.0)
        except paramiko.ssh_exception.SSHException:
            self.connection.get_transport().auth_none(username)
        self.connection.sftp = paramiko.SFTPClient.from_transport(self.connection.get_transport())
        return self.connection

    # paramiko 命令行远程使用
    def get_result_connet_cmd(self, cmd, ip=None, port=None, username=None, passwd=None):
        self.log('get_result_connet_cmd:', cmd, ', ip:', ip)
        if ip :
            self.open_connection(ip, port, username, passwd)
        else :
            self.open_connection(self.ip, self.port, self.user, self.passwd)
        if self.test_connection():
            stdin, stdout, stderr = self.connection.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            if output.strip() == '':
                output = stderr.read().decode('utf-8')
        else :
            self.log('paramiko connect 失败')
        self.close_connection()
        self.log('cmd_ret:',output)
        return output

    # 远程命令获取结果
    def get_result_remote_cmd(self, cmd, ip, username):
        remote_cmd = f'{self.sshcmd} {username}@{ip} {cmd}'
        self.log('get_result_remote_cmd:', remote_cmd)
        return self.exe_subprocess_popenE(remote_cmd)

    # 本地命令获取结果
    def get_result_local_cmd(self, cmd):
        self.log('get_result_local_cmd:', cmd)
        return self.exe_subprocess_run(cmd)

    # os执行命令
    def exe_os_system_cmd(self, cmd)->bool:
        res = os.system(cmd)
        self.log('ret_cmd:', res)
        return res
    
    # scp执行命令
    def exe_scp_cmd(self, saddr, daddr, ip, username):
        scp_cmd = f'scp -r {saddr} {username}@{ip}:{daddr}'
        self.exe_subprocess_run(scp_cmd)

    # shell=True设置为shell启动
    def exe_subprocess_run(self, cmd:str)->(str, int):
        try:
            result = subprocess.run(cmd,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    shell=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            # 异常情况下从异常对象获取stdout, stderr和返回码
            output = e.stdout if e.stdout else e.stderr
            returncode = e.returncode
            self.log('ret_err:', output)
            return output, returncode
        else:
            # 成功执行的情况
            returncode = result.returncode
            self.log('ret_cmd:', result.stdout)
            return result.stdout, returncode
        
    # 
    def exe_subprocess_popen(self, cmd):
        subprocess.Popen(cmd, 
                        stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        shell=True, text=True, preexec_fn=os.setsid)
        
    # preexec_fn=os.setsid新开会话
    def exe_subprocess_popenE(self, cmd:str):
        result = subprocess.Popen(cmd,
                                  stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  shell=True, text=True, preexec_fn=os.setsid)
        # 等待程序结束才有输出
        stdout, stderr = result.communicate()
        returncode = result.returncode  # 返回值  
        if stdout: 
            self.log('ret_cmd:', stdout)
            return stdout, returncode
        else :
            self.log('ret_err:', stderr)
            return stderr, returncode

