#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a ui module '

__author__ = 'ljk'

import tkinter as tk
from tkinter import messagebox


def ui_Tk():
    # 创建主窗口
    root = tk.Tk()
    root.title("Tkinter 控件例程")

    # 标签
    label = tk.Label(root, text="这是一个标签")
    label.pack()

    # 按钮
    def button_click():
        messagebox.showinfo("按钮点击", "按钮被点击了！")

    button = tk.Button(root, text="点击我", command=button_click)
    button.pack()

    # 文本框
    entry = tk.Entry(root)
    entry.pack()

    # 列表框
    listbox = tk.Listbox(root)
    listbox.insert(1, "Python")
    listbox.insert(2, "Java")
    listbox.insert(3, "C++")
    listbox.pack()

    # 复选框
    check_var = tk.IntVar()
    checkbutton = tk.Checkbutton(root, text="选择我", variable=check_var)
    checkbutton.pack()

    # 单选框
    radio_var = tk.StringVar()
    radio_var.set("Option 1")
    radio1 = tk.Radiobutton(root, text="选项1", variable=radio_var, value="Option 1")
    radio2 = tk.Radiobutton(root, text="选项2", variable=radio_var, value="Option 2")
    radio1.pack()
    radio2.pack()

    # 滑块
    scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()
    return root

def ui_Tk2(switch):
    # 创建顶级窗口，独立出来
    #root = tk.Toplevel()
    # 创建主窗口
    root = tk.Tk()
    root.title("Tkinter 标签例程")
    label1 = tk.Label(root, text="标签1")
    label2 = tk.Label(root, text="标签2")
    if switch:
        # 使用 grid() 放置组件
        label1.grid(row=0, column=0)
        label2.grid(row=1, column=1)
    else:
        # 使用 place() 放置组件
        label1.place(x=10, y=20)
        label2.place(relx=0.5, rely=0.5, anchor="center")
    return root

class UI_Tkinter(tk.Tk):
    def __init__(self):
         # 调用父类 tk.Tk 的构造函数
        super().__init__()
        self.set_size()
        self.draw_ui()

    def set_size(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # 设置窗口的初始大小为屏幕长宽的一半
        window_width = screen_width // 2
        window_height = screen_height // 2
        self.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//4}")

    def draw_ui(self):
        self.title("Tkinter 控件例程")

        # 标签
        self.label = tk.Label(self, text="这是一个标签")
        self.label.pack()

        # 按钮
        self.button = tk.Button(self, text="点击我", command=self.button_click)
        self.button.pack()

        # 文本框
        self.entry = tk.Entry(self)
        self.entry.pack()

        # 列表框
        self.listbox = tk.Listbox(self)
        self.listbox.insert(1, "Python")
        self.listbox.insert(2, "Java")
        self.listbox.insert(3, "C++")
        self.listbox.pack()

        # 复选框
        self.check_var = tk.IntVar()
        self.checkbutton = tk.Checkbutton(self, text="选择我", variable=self.check_var)
        self.checkbutton.pack()

        # 单选框
        self.radio_var = tk.StringVar()
        self.radio_var.set("Option 1")
        self.radio1 = tk.Radiobutton(self, text="选项1", variable=self.radio_var, value="Option 1")
        self.radio2 = tk.Radiobutton(self, text="选项2", variable=self.radio_var, value="Option 2")
        self.radio1.pack()
        self.radio2.pack()

        # 滑块
        self.scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.pack()

    def button_click(self):
        messagebox.showinfo("按钮点击", "按钮被点击了！")

if  __name__ == "__main__" :
    # 创建应用程序对象并运行主循环
    app = UI_Tkinter()
    app.mainloop()

    # 创建应用程序对象并运行主循环
    root = ui_Tk()
    # 运行主循环
    root.mainloop()

    root1 = ui_Tk2(True)
    root1.mainloop()

    root2 = ui_Tk2(False)
    root2.mainloop()

