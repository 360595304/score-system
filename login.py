from tkinter import *
from tkinter import messagebox

from admin import TeacherSide
from dao import *


class Login:
    def __init__(self, master, **kw):
        super().__init__(**kw)
        master.destroy()
        self.win = Tk()
        self.win.title('登陆')
        self.win.geometry('200x120+650+200')
        self.win.resizable(0, 0)
        self.createWidgets()

    def createWidgets(self):
        self.nameLabel = Label(self.win, text='用户ID：')
        self.pwdLabel = Label(self.win, text='密码：')
        self.name = StringVar()
        self.password = StringVar()
        self.nameEntry = Entry(self.win, textvariable=self.name)
        self.pwdEntry = Entry(self.win, textvariable=self.password, show='*')
        self.nameLabel.grid(row=1, column=1, rowspan=1, columnspan=1)
        self.nameEntry.grid(row=1, column=2, rowspan=1, columnspan=2)
        self.pwdLabel.grid(row=2, column=1, rowspan=1, columnspan=1)
        self.pwdEntry.grid(row=2, column=2, rowspan=1, columnspan=2)
        self.loginButton = Button(self.win, text='登陆')
        self.cancelButton = Button(self.win, text='取消')
        self.cancelButton.bind('<Button-1>', self.cancel)
        self.loginButton.bind('<Button-1>', self.login)
        self.cancelButton.grid(row=4, column=2, rowspan=1, columnspan=1)
        self.loginButton.grid(row=4, column=3, rowspan=1, columnspan=1)

    def cancel(self, event):
        self.win.destroy()

    def login(self, event):
        res = login(self.name.get(), self.password.get())
        print(res)
        if len(res) == 0:
            messagebox.showwarning('登陆失败', '用户ID或密码错误')
            return
        self.win.destroy()
        app = TeacherSide(res[0])
        app.mainloop()


root = Tk()
a = Login(root)
root.mainloop()
