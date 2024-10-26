from tkinter import Tk, ttk, PhotoImage

root = Tk()

tree = ttk.Treeview(root)
tree.pack(expand=True, fill='both')

# 假设图像文件在脚本相同的目录下
folder_icon = PhotoImage(file='imagefolder.gif')
file_icon = PhotoImage(file='imagefile.gif')

tree.tag_configure('folder', image=folder_icon)
tree.tag_configure('file', image=file_icon)

# 添加带有图标的测试项
tree.insert('', 'end', text='Folder', tags=('folder',))
tree.insert('', 'end', text='File', tags=('file',))

root.mainloop()