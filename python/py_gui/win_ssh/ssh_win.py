#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' ssh win_scp '

__author__ = 'ljk'

import paramiko
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from tkinter import filedialog
from stat import S_ISDIR
import os



# ssh远程登录
def ssh_login():
    global sftp  # 声明变量为全局变量，以便在函数外用到它
    hostname = entry_ip.get()
    username = entry_username.get()
    password = entry_password.get()
    if not hostname or not username:
        messagebox.showwarning("输入错误", "IP地址和用户名不能为空。")
        return
    try:
        # 创建Paramiko SSH客户端
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password)
        sftp = ssh_client.open_sftp()
        #messagebox.showinfo("登录成功", "您已成功登录！")
        update_directory_tree('/')
    except paramiko.AuthenticationException:
        messagebox.showerror("登录失败", "认证失败，用户名或密码错误。")
    except paramiko.SSHException as e:
        messagebox.showerror("登录失败", f"SSH连接失败: {e}")
    except Exception as e:
        messagebox.showerror("错误", f"出错了: {e}")

# 目录展示
def update_directory_tree(path):
    global current_path
    current_path = path
    tree.delete(*tree.get_children())  # 清除tree中的所有项
    # 用于文件夹和文件图标显示
    tree.tag_configure('folder', image=folder_icon)
    tree.tag_configure('file',   image=file_icon)
    try:
        # sftp.chdir(path)               # 不需要切换目录，直接列出目录内容
        files = sftp.listdir_attr(path)  # 获取目录列表和各文件属性
        for fattr in files:
            # 使用stat.S_ISDIR检查文件模式是否表示一个目录
            is_dir = S_ISDIR(fattr.st_mode)
            icon_tag = 'folder' if is_dir else 'file'
            # 插入到treeview
            tree.insert('', 'end', fattr.filename, text=fattr.filename, values=(is_dir,), tags=(icon_tag,))
    except Exception as e:
        messagebox.showerror("错误", f"无法打开目录：{path}\n错误描述：{e}")

# 选择打开目录
def on_tree_select(event):
    selection = tree.selection()
    if not selection:  # 如果没有选中项，则不进行操作
        return
    item = selection[0]
    is_dir = tree.item(item, "values")[0]
    # 修复路径拼接，确保路径中包含斜杠 '/'
    if is_dir == 'True':
        path = tree.item(item, "text")
        # 如果当前路径是根目录，则不需要再次添加 '/'
        new_path = current_path if current_path.endswith('/') else (current_path + '/')
        full_path = new_path + path
        update_directory_tree(full_path)

# 返回上一级目录
def on_back_click():
    if current_path != '':
        new_path = '/'.join(current_path.split('/')[:-1])
    if new_path == '':
        new_path = '/'
    update_directory_tree(new_path)

# 文件夹递归下载的功能
def download_folder(localpath, remotepath):
    os.makedirs(localpath, exist_ok=True)
    for entry in sftp.listdir_attr(remotepath):
        remote_entry_path = os.path.join(remotepath, entry.filename)
        local_entry_path = os.path.join(localpath, entry.filename)
        if S_ISDIR(entry.st_mode):
            download_folder(local_entry_path, remote_entry_path)
        else:
            download_file(local_entry_path, remote_entry_path)

# 文件夹下载
def download_file(localpath, remotepath):
    sftp.get(remotepath, localpath)

def download():
    selection = tree.selection()
    # 检查是否有选择项
    if not selection:
        messagebox.showwarning("警告", "请选择一个文件或文件夹下载")
        return
    for item in selection:
        is_dir = tree.item(item, "values")[0]
        filename = tree.item(item, "text")
        local_path = filename
        remote_path = os.path.join(current_path, filename).replace('\\', '/')
        if is_dir == 'True':
            # 下载整个文件夹
            download_folder(local_path, remote_path)
            messagebox.showinfo("成功", f"目录 '{filename}' 已下载到 '{local_path}'")
        else:
            # 下载单个文件
            download_file(local_path, remote_path)
            messagebox.showinfo("成功", f"文件 '{filename}' 已下载到 '{local_path}'")

# 文件夹递归上传的功能
def upload_folder(local_path, remote_path):
    os.makedirs(remote_path, exist_ok=True)
    for entry in os.listdir(local_path):
        local_entry = os.path.join(local_path, entry)
        remote_entry = f"{remote_path}/{entry}"
        if os.path.isdir(local_entry):
            upload_folder(local_entry, remote_entry)
        else:
            upload_file(local_entry, remote_entry)

# 文件夹上传
def upload_file(local_path, remote_path):
    sftp.put(local_path, remote_path)

def upload():
    # 初始选择上传文件，你可以使用filedialog.askdirectory()来选择目录
    file_path = filedialog.askopenfilename()
    if not file_path:
        return  # 没有选择文件
    filename = os.path.basename(file_path)
    # 上传到当前路径下的filename
    remotepath = os.path.join(current_path, filename)
    if os.path.isdir(file_path):
        # 如果选择的是一个文件夹，使用递归上传
        upload_folder(file_path, remotepath)
        messagebox.showinfo("上传成功", f"文件夹 '{filename}' 已上传到 '{remotepath}'")
    else:
        # 否则，上传单个文件
        upload_file(file_path, remotepath)
        messagebox.showinfo("上传成功", f"文件 '{filename}' 已上传到 '{remotepath}'")

# ui显示
def ui_run():
    global tree
    global entry_ip, entry_username, entry_password
    global folder_icon, file_icon
    # 创建Tkinter窗口
    root = tk.Tk()
    root.title("SSH 文件浏览")
    # UI布局
    frame_login = tk.LabelFrame(root, text="登录信息", padx=10, pady=10)
    frame_login.pack(padx=10, pady=5, fill='x')

    label_ip = tk.Label(frame_login, text="IP地址:")
    label_ip.pack(side=tk.LEFT, fill='x', expand=True)
    entry_ip = tk.Entry(frame_login)
    entry_ip.pack(side=tk.LEFT, fill='x', expand=True)
    entry_ip.insert(0, "172.31.3.80")

    label_username = tk.Label(frame_login, text="用户名:")
    label_username.pack(side=tk.LEFT, fill='x', expand=True)
    entry_username = tk.Entry(frame_login)
    entry_username.pack(side=tk.LEFT, fill='x', expand=True)
    entry_username.insert(0, "liauto")

    label_password = tk.Label(frame_login, text="密码:")
    label_password.pack(side=tk.LEFT, fill='x', expand=True)
    entry_password = tk.Entry(frame_login, show="*")
    entry_password.pack(side=tk.LEFT, fill='x', expand=True)

    button_login = tk.Button(frame_login, text="连接", command=ssh_login)
    button_login.pack(side=tk.LEFT, padx=5)

    frame_files = tk.LabelFrame(root, text="远程文件", padx=10, pady=10)
    frame_files.pack(padx=10, pady=5, fill='both', expand=True)

    tree = ttk.Treeview(frame_files)
    tree.pack(side=tk.TOP, fill='both', expand=True)
    folder_icon = PhotoImage(file='img/imagefolder_16.gif')  # 文件夹图标
    file_icon   = PhotoImage(file='img/imagefile_16.gif')      # 文件图标

    button_back = tk.Button(frame_files, text="返回上级", command=on_back_click)
    #button_back.pack(side=tk.TOP)
    button_back.pack(side=tk.LEFT, padx=5, pady=5)

    button_download = tk.Button(frame_files, text="下载到本地", command=download)
    button_download.pack(side=tk.LEFT, padx=5, pady=5)

    button_upload = tk.Button(frame_files, text="上传到远程", command=upload)
    button_upload.pack(side=tk.LEFT, padx=5, pady=5)

    # 当用户选择一个项目时触发
    tree.bind('<<TreeviewSelect>>', on_tree_select)

    root.mainloop()
    return root

if __name__ == '__main__':
    ui_run()