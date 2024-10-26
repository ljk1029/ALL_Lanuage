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

if  __name__ == "__main__" :
    # 创建应用程序对象并运行主循环
    app = ui_Tk()
    # 运行主循环
    app.mainloop()

    root1 = ui_Tk2(True)
    root1.mainloop()

    root2 = ui_Tk2(False)
    root2.mainloop()

