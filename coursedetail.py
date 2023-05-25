from tkinter import *
from tkinter import messagebox

from dao import *


class CourseDetail(Tk):
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
        Label(self, text='课程ID：').place(x=10, y=10)
        Label(self, text='课程名：').place(x=10, y=40)
        Label(self, text='描述：').place(x=10, y=70)
        # sid = StringVar()
        # name = StringVar()
        # sex = StringVar()
        # college = StringVar()
        # pwd = StringVar()
        self.id_entry = Entry(self)
        self.id_entry.place(x=75, y=10)
        self.name_entry = Entry(self)
        self.name_entry.place(x=75, y=40)
        self.detail_entry = Entry(self)
        self.detail_entry.place(x=75, y=70)

        self.cancel_button = Button(self, text='取消', command=self.cancel)
        self.cancel_button.place(x=75, y=160)
        if state == 2:
            self.title('修改课程')
            self.id_entry.insert(0, lst[1])
            self.id_entry['state'] = 'readonly'
            self.name_entry.insert(0, lst[2])
            self.detail_entry.insert(0, lst[3])
            self.modify_button = Button(self, text='修改', command=self.modify)
            self.modify_button.place(x=115, y=160)
        else:
            self.title('添加学生')
            self.add_button = Button(self, text='录入', command=self.add)
            self.add_button.place(x=115, y=160)

    def cancel(self):
        self.destroy()

    def add(self):
        course = (
            self.id_entry.get(), self.name_entry.get(), self.detail_entry.get(),)
        if self.check():
            add_course(course)
            self.modify_tree()
            messagebox.showinfo('成功', '成功添加课程！')
            self.destroy()
        else:
            messagebox.showerror('失败', '课程已存在！')

    def modify(self):
        course = (
            self.id_entry.get(), self.name_entry.get(), self.detail_entry.get(),)

        update_course(course)
        self.modify_tree()
        messagebox.showinfo('成功', '成功修改课程！')
        self.destroy()

    def modify_tree(self):
        res = getCourses()
        x = self.treeview.get_children()
        for item in x:
            self.treeview.delete(item)
        i = 1
        for line in res:
            lst = list(line)
            lst = [i] + lst
            print(lst)
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
