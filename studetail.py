from tkinter import *
from tkinter import messagebox

from dao import *


class StuDetail(Tk):
    def __init__(self, state, lst, treeview):
        super().__init__()
        self.treeview = treeview
        self.geometry('230x200+620+200')
        self.resizable(0, 0)
        self.state = state
        self.lst = lst
        self.createWidgets(state, lst)
        self.mainloop()

    def createWidgets(self, state, lst):
        Label(self, text='学号：').place(x=10, y=10)
        Label(self, text='姓名：').place(x=10, y=40)
        Label(self, text='性别：').place(x=10, y=70)
        Label(self, text='院系：').place(x=10, y=100)
        Label(self, text='班级：').place(x=10, y=130)
        # sid = StringVar()
        # name = StringVar()
        # sex = StringVar()
        # college = StringVar()
        # pwd = StringVar()
        self.id_entry = Entry(self)
        self.id_entry.place(x=75, y=10)
        self.name_entry = Entry(self)
        self.name_entry.place(x=75, y=40)
        self.sex_entry = Entry(self)
        self.sex_entry.place(x=75, y=70)
        self.college_entry = Entry(self)
        self.college_entry.place(x=75, y=100)
        self.class_entry = Entry(self)
        self.class_entry.place(x=75, y=130)
        self.cancel_button = Button(self, text='取消', command=self.cancel)
        self.cancel_button.place(x=75, y=160)
        if state == 2:
            self.title('修改学生')
            self.id_entry.insert(0, lst[0])
            self.id_entry['state'] = 'readonly'
            self.name_entry.insert(0, lst[1])
            self.sex_entry.insert(0, lst[2])
            self.college_entry.insert(0, lst[3])
            self.class_entry.insert(0, lst[4])
            self.modify_button = Button(self, text='修改', command=self.modify)
            self.modify_button.place(x=115, y=160)
        else:
            self.title('添加学生')
            self.add_button = Button(self, text='录入', command=self.add)
            self.add_button.place(x=115, y=160)

    def cancel(self):
        self.destroy()

    def add(self):
        stu = (
            self.id_entry.get(), self.name_entry.get(), self.sex_entry.get(), self.college_entry.get(),
            self.class_entry.get(),)
        if self.check():
            add_stu(stu)
            self.modify_tree()
            messagebox.showinfo('成功', '成功添加学生！')
            self.destroy()
        else:
            messagebox.showerror('失败', '学号已存在！')

    def modify(self):
        stu = (
            self.id_entry.get(), self.name_entry.get(), self.sex_entry.get(), self.college_entry.get(),
            self.class_entry.get(),)

        update_stu(stu)
        self.modify_tree()
        messagebox.showinfo('成功', '成功修改学生！')
        self.destroy()


    def modify_tree(self):
        res = getStuList()
        x = self.treeview.get_children()
        for item in x:
            self.treeview.delete(item)
        i = 1
        for line in res:
            lst = list(line)
            self.treeview.insert("", i, values=lst)
            i += 1

    def check(self):
        x = self.treeview.get_children()
        for item in x:
            sid = self.treeview.item(item)['values'][0]
            sid = str(sid)
            # print(sid, self.id_entry.get())
            # print(type(sid), type(self.id_entry.get()))
            if sid == self.id_entry.get():
                return False
        return True

