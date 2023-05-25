from tkinter import *
from tkinter import messagebox

from PythonStudy.design import dao
from dao import *


class ScoreDetail(Tk):
    def __init__(self, state, lst, treeview, course_id):
        super().__init__()
        self.treeview = treeview
        self.course = dao.getCourse(course_id)
        self.course_id = self.course[0]
        self.geometry('230x200+620+200')
        self.resizable(0, 0)
        self.state = state
        self.lst = lst
        self.createWidgets(state, lst)
        self.mainloop()

    def createWidgets(self, state, lst):
        Label(self, text='学号：').place(x=10, y=10)
        Label(self, text='姓名：').place(x=10, y=40)
        Label(self, text='课程：').place(x=10, y=70)
        Label(self, text='分数：').place(x=10, y=100)
        # sid = StringVar()
        # name = StringVar()
        # sex = StringVar()
        # college = StringVar()
        # pwd = StringVar()
        self.id_entry = Entry(self)
        self.id_entry.place(x=75, y=10)
        self.name_entry = Entry(self)
        self.name_entry.place(x=75, y=40)
        self.course_entry = Entry(self)
        self.course_entry.place(x=75, y=70)
        self.score_entry = Entry(self)
        self.score_entry.place(x=75, y=100)
        self.cancel_button = Button(self, text='取消', command=self.cancel)
        self.cancel_button.place(x=75, y=130)
        self.course_entry.insert(0, self.course[1])
        self.course_entry['state'] = 'readonly'
        # 修改
        if state == 2:
            self.title('修改成绩')
            self.id_entry.insert(0, lst[1])
            self.name_entry.insert(0, lst[2])
            self.score_entry.insert(0, lst[5])
            self.name_entry['state'] = 'readonly'
            self.id_entry['state'] = 'readonly'

            self.modify_button = Button(self, text='修改', command=self.modify)
            self.modify_button.place(x=115, y=130)
        # 新增
        else:
            self.name_entry['state'] = 'readonly'
            self.title('录入成绩')
            self.add_button = Button(self, text='录入', command=self.add)
            self.add_button.place(x=115, y=130)

    def cancel(self):
        self.destroy()

    # 添加成绩
    def add(self):
        score = self.score_entry.get()
        if not str(score).isdigit():
            messagebox.showwarning('提示', '分数不合法！')
            return
        if self.check():
            add_score(self.id_entry.get(), self.course, self.score_entry.get())
            self.modify_tree()
            messagebox.showinfo('成功', '成功添加成绩！')
            self.destroy()

    # 修改分数
    def modify(self):
        score = self.score_entry.get()
        if not str(score).isdigit():
            messagebox.showwarning('提示', '分数不合法！')
            return
        update_score(self.id_entry.get(), self.course_id, self.score_entry.get())
        self.modify_tree()
        messagebox.showinfo('成功', '成功修改分数！')
        self.destroy()

    # 更新treeview
    def modify_tree(self):
        res = getScore(self.course_id)
        x = self.treeview.get_children()
        for item in x:
            self.treeview.delete(item)
        i = 1
        for stu in res:
            lst = list(stu)
            lst = [i] + lst
            self.treeview.insert("", i, values=lst)
            i += 1

    # 检查学号和成绩是否存在
    def check(self):
        ids = getSid()
        if self.id_entry.get() not in ids:
            messagebox.showerror('错误', '学号有误！')
            return False
        res = get_stu(self.id_entry.get(), self.course)
        if len(res) > 0:
            messagebox.showerror('错误', '成绩已存在！')
            return False
        return True
