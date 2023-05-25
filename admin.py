from tkinter import *
from tkinter import messagebox, font
from tkinter.ttk import Treeview
import xlsxwriter

from PythonStudy.design.coursedetail import CourseDetail
from dao import *
from scoredetail import ScoreDetail
from studetail import StuDetail


class TeacherSide(Tk):
    def __init__(self, user):
        super().__init__()
        self.scoreList = []
        print(user)
        self.user = user
        self["bg"] = "skyblue"
        self.title("学生成绩管理系统")
        self.geometry("900x640+290+80")
        self.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        self.setup_UI()
        self.reverse = True

    def setup_UI(self):
        self.name = Label(self, text='学生成绩管理系统', font=font.Font(size=50, slant='italic'), bg='skyblue')
        self.name.place(x=150, y=10)
        # 加载当前用户
        self.Label_login_user = Label(self, text="当前用户:" + self.user[1], bg='skyblue')
        self.Label_login_user.place(x=750, y=60)

        # 左边：按钮区域,创建一个容器
        self.Pane_left = PanedWindow(width=160, height=540)
        self.Pane_left.place(x=4, y=94)

        # 添加左边按钮
        self.Button_stu = Button(self.Pane_left, text="学生信息", command=self.show_stu)
        self.Button_stu.place(x=20, y=20)
        self.Button_course = Button(self.Pane_left, text="课程信息", command=self.show_course)
        self.Button_course.place(x=20, y=60)
        self.Button_score = Button(self.Pane_left, text="考试成绩", command=self.show_score)
        self.Button_score.place(x=20, y=100)
        self.Button_stu = Button(self.Pane_left, text="导出学生", command=self.stu_xls)
        self.Button_stu.place(x=20, y=140)
        self.Button_score = Button(self.Pane_left, text="导出成绩", command=self.score_xls)
        self.Button_score.place(x=20, y=180)

        # 右边：查询、TreeView
        self.Pane_right = PanedWindow(width=725, height=540)
        self.Pane_right.place(x=170, y=94)
        # 学生信息查询
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息查询", width=700, height=70)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_sno = Label(self.LabelFrame_query, text="学号：")
        self.Label_sno.place(x=5, y=13)
        self.var_sno = StringVar()
        self.Entry_sno = Entry(self.LabelFrame_query, width=8, textvariable=self.var_sno)
        self.Entry_sno.place(x=40, y=10)

        self.Label_name = Label(self.LabelFrame_query, text="姓名：")
        self.Label_name.place(x=125, y=13)
        self.var_name = StringVar()
        self.Entry_name = Entry(self.LabelFrame_query, width=8, textvariable=self.var_name)
        self.Entry_name.place(x=160, y=10)

        self.Button_query = Button(self.LabelFrame_query, text="查询", width=4, command=self.stu_query)
        self.Button_query.place(x=240, y=5)
        self.Button_all = Button(self.LabelFrame_query, text="刷新", width=7, command=self.fetchData)
        self.Button_all.place(x=300, y=5)

        self.Button_add = Button(self.LabelFrame_query, text="添加学生", width=7, command=self.stu_add)
        self.Button_add.place(x=600, y=5)

        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right, columns=("sno", "name",
                                                       "gender", "college", "class"),
                             show="headings", height=20)
        self.Tree.bind('<Double-1>', self.stu_modify)
        self.Tree.bind('<3>', self.show_menu)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("name", width=120, anchor="center")
        self.Tree.column("gender", width=120, anchor="center")
        self.Tree.column("college", width=160, anchor="center")
        self.Tree.column("class", width=196, anchor="center")

        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("name", text="姓名")
        self.Tree.heading("gender", text="性别")
        self.Tree.heading("college", text="院系")
        self.Tree.heading("class", text="班级")
        self.Tree.place(x=10, y=80)

        # 考试信息
        self.LabelFrame_score = LabelFrame(self.Pane_right, text="考试成绩查询", width=700, height=70)
        # 添加控件
        self.course_label = Label(self.LabelFrame_score, text="科目：")
        self.course_label.place(x=5, y=13)
        self.var_course = StringVar()
        self.courses = getCourses()
        # print(getCourses())
        self.var_course.set(self.courses[0][1])
        self.course_menu = OptionMenu(self.LabelFrame_score, self.var_course, *[x[1] for x in self.courses], '总分')
        self.course_menu.place(x=40, y=10)
        self.change_button = Button(self.LabelFrame_score, text='切换', command=self.fetchData)
        self.change_button.place(x=150, y=10)

        self.Label_avg = Label(self.LabelFrame_score, text="平均分：")
        self.Label_avg.place(x=255, y=13)
        self.var_avg = StringVar()
        self.Entry_avg = Entry(self.LabelFrame_score, width=8, textvariable=self.var_avg, state='readonly')
        self.Entry_avg.place(x=300, y=13)

        self.Button_flush = Button(self.LabelFrame_score, text="刷新", width=7, command=self.fetchData)
        self.Button_flush.place(x=400, y=5)

        self.Button_add_score = Button(self.LabelFrame_score, text="排序", width=7, command=self.sort_tree)
        self.Button_add_score.place(x=500, y=5)

        self.Button_add_score = Button(self.LabelFrame_score, text="添加成绩", width=7, command=self.score_add)
        self.Button_add_score.place(x=600, y=5)

        # 成绩
        self.Tree_score = Treeview(self.Pane_right, columns=("no", "sno", "name",
                                                             "college", "class", "score"),
                                   show="headings", height=20)
        self.Tree_score.bind('<Double-1>', self.score_modify)
        # 设置每一个列的宽度和对齐的方式
        self.Tree_score.column("no", width=50, anchor="center")
        self.Tree_score.column("sno", width=100, anchor="center")
        self.Tree_score.column("name", width=100, anchor="center")
        self.Tree_score.column("class", width=120, anchor="center")
        self.Tree_score.column("college", width=170, anchor="center")
        self.Tree_score.column("score", width=160, anchor="center")

        # 设置每个列的标题
        self.Tree_score.heading("no", text="序号")
        self.Tree_score.heading("sno", text="学号")
        self.Tree_score.heading("name", text="姓名")
        self.Tree_score.heading("class", text="班级")
        self.Tree_score.heading("college", text="院系")
        self.Tree_score.heading("score", text="分数")
        self.popup = Menu(self.Tree, tearoff=0)
        self.popup.add_command(label="修改", command=self.stu_modify)  # , command=next) etc...
        self.popup.add_command(label="删除", command=self.stu_remove)

        # 课程信息
        self.LabelFrame_course = LabelFrame(self.Pane_right, text="课程查询", width=700, height=70)
        # 添加控件
        self.LabelFrame_course.place(x=10, y=10)
        # 添加控件
        self.Course_add = Button(self.LabelFrame_course, text="添加课程", width=7, command=self.course_add)
        self.Course_add.place(x=10, y=5)

        # 课程信息
        self.Tree_course = Treeview(self.Pane_right, columns=("no", "course_id", "course_name",
                                                              "description"),
                                    show="headings", height=20)
        self.Tree_course.bind('<Double-1>', self.course_modify)
        # 设置每一个列的宽度和对齐的方式
        self.Tree_course.column("no", width=50, anchor="center")
        self.Tree_course.column("course_id", width=100, anchor="center")
        self.Tree_course.column("course_name", width=100, anchor="center")
        self.Tree_course.column("description", width=200, anchor="center")

        # 设置每个列的标题
        self.Tree_course.heading("no", text="序号")
        self.Tree_course.heading("course_id", text="课程ID")
        self.Tree_course.heading("course_name", text="课程名")
        self.Tree_course.heading("description", text="课程简介")

        self.popup = Menu(self.Tree, tearoff=0)
        # self.popup.add_command(label="修改", command=self.stu_modify)  # , command=next) etc...
        # self.popup.add_command(label="删除", command=self.stu_remove)

        self.fetchData()
        self.show_stu()

    def stu_add(self):
        add_frame = StuDetail(1, None, self.Tree)

    def course_add(self):
        add_frame = CourseDetail(1, None, self.Tree_course)

    def course_modify(self, *kw):
        for item in self.Tree_course.selection():
            add_frame = CourseDetail(2, self.Tree_course.item(item)['values'], self.Tree_course)

    def score_add(self):
        add_frame = ScoreDetail(1, None, self.Tree, self.course_id)

    def stu_modify(self, *kw):
        for item in self.Tree.selection():
            add_frame = StuDetail(2, self.Tree.item(item)['values'], self.Tree)

    def score_modify(self, *kw):
        for item in self.Tree_score.selection():
            ScoreDetail(2, self.Tree_score.item(item)['values'], self.Tree_score, self.course_id)

    def stu_remove(self, *kw):
        for item in self.Tree.selection():
            sid = self.Tree.item(item)['values'][0]
            remove_stu(sid)
        messagebox.showinfo('成功', '成功删除学生！')
        self.fetchData()

    def show_stu(self):
        self.LabelFrame_score.place_forget()
        self.LabelFrame_course.place_forget()
        self.Tree_score.place_forget()
        self.Tree_course.place_forget()
        self.LabelFrame_query.place(x=10, y=10)
        self.Tree.place(x=10, y=80)
        self.fetchData()

    def show_course(self):
        self.LabelFrame_score.place_forget()
        self.LabelFrame_query.place_forget()
        self.Tree_score.place_forget()
        self.Tree.place_forget()
        self.LabelFrame_course.place(x=10, y=10)
        self.Tree_course.place(x=10, y=80)
        self.fetchData()

    def show_score(self):
        self.LabelFrame_query.place_forget()
        self.LabelFrame_course.place_forget()
        self.Tree.place_forget()
        self.Tree_course.place_forget()
        self.LabelFrame_score.place(x=10, y=10)
        self.Tree_score.place(x=10, y=80)
        self.fetchData()

    def fetchData(self, *kw):
        self.stuList = getStuList()
        self.courses = getCourses()
        course_name = self.var_course.get()
        self.course_id = ''
        for course in self.courses:
            if course_name == course[1]:
                self.course_id = course[0]
                break
        # print('aaa', self.var_course.get(), self.course_id)
        if self.course_id == '':
            self.scoreList = getTotalScore()
        else:
            self.scoreList = getScore(self.course_id)
        self.update_tree()

    def update_tree(self):
        x = self.Tree.get_children()
        y = self.Tree_score.get_children()
        z = self.Tree_course.get_children()
        for item in x:
            self.Tree.delete(item)
        for item in y:
            self.Tree_score.delete(item)
        for item in z:
            self.Tree_course.delete(item)
        i = 1
        total = 0
        for stu in self.stuList:
            lst = list(stu)
            self.Tree.insert("", i, values=lst)
            i += 1
        i = 1
        for course in self.courses:
            lst = list(course)
            lst = [i] + lst
            self.Tree_course.insert("", i, values=lst)
            i += 1
        i = 1
        for stu in self.scoreList:
            lst = list(stu)
            total += lst[4]
            lst = [i] + lst
            self.Tree_score.insert("", i, values=lst)
            i += 1
        # print(self.scoreList)
        if len(self.scoreList) > 0:
            total /= len(self.scoreList)
            total = int(total * 100) / 100
        else:
            total = 0
        self.var_avg.set(total)

    def sort_tree(self):
        self.scoreList.sort(key=lambda x: x[4], reverse=self.reverse)
        self.reverse = not self.reverse
        self.update_tree()

    def show_menu(self, event):
        try:
            self.popup.tk_popup(event.x_root + 23, event.y_root + 10, 0)
        finally:
            self.popup.grab_release()

    def stu_query(self):
        x = self.Tree.get_children()
        for item in x:
            self.Tree.delete(item)
        i = 1
        for stu in self.stuList:
            lst = list(stu)
            if lst[0].__contains__(self.var_sno.get()) and lst[1].__contains__(self.var_name.get()):
                self.Tree.insert("", i, values=lst)
                i += 1

    def stu_xls(self):
        workbook = xlsxwriter.Workbook('学生信息.xlsx')  # 新建文件
        ws = workbook.add_worksheet()  # 新建sheet
        # bold = workbook.add_format({'bold': True})
        ws.write('A1', u'学号')  # 测试插入数据
        ws.write('B1', u"姓名")
        ws.write('C1', u'性别')
        ws.write('D1', u'院系')
        ws.write('E1', u'班级')
        row = 2
        for item in self.stuList:
            ws.write_row('A' + str(row), item)
            row += 1
        workbook.close()  # 保存并关闭
        messagebox.showinfo('成功', '已导出学生信息到当前目录！')

    def score_xls(self):
        workbook = xlsxwriter.Workbook(self.course_id + '.xlsx')  # 新建文件
        ws = workbook.add_worksheet()  # 新建sheet
        # bold = workbook.add_format({'bold': True})
        ws.write('A1', u'序号')  # 测试插入数据
        ws.write('B1', u'学号')  # 测试插入数据
        ws.write('C1', u"姓名")
        ws.write('D1', u'院系')
        ws.write('E1', u'班级')
        ws.write('F1', u'分数')
        row = 2
        for item in self.scoreList:
            lst = [row - 1] + list(item)
            ws.write_row('A' + str(row), lst)
            row += 1
        workbook.close()  # 保存并关闭
        messagebox.showinfo('成功', '已导出成绩信息到当前目录！')
