import pymysql


def getConnect():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='su360595304',
        db='student',
        charset='utf8'
    )
    cursor = conn.cursor()
    return conn, cursor


def login(username, password):
    conn, cursor = getConnect()
    sql = 'select * from admin where id=%s and password=%s'
    cursor.execute(sql, (username, password))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def getStuList():
    conn, cursor = getConnect()
    sql = 'select id,name,sex,college,class from student'
    cursor.execute(sql)
    res = []
    for line in cursor.fetchall():
        res.append(line)
    cursor.close()
    conn.close()
    return res


def add_stu(stu):
    conn, cursor = getConnect()

    sql = 'insert into student (id,name,sex,college,class)values(%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, stu)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def update_stu(stu):
    conn, cursor = getConnect()
    sql = 'update student set name=%s,sex=%s,college=%s,class=%s where id=%s'
    stu = (stu[1], stu[2], stu[3], stu[4], stu[0])
    try:
        cursor.execute(sql, stu)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def remove_stu(sid):
    conn, cursor = getConnect()
    sql = 'delete from student where id=%s'
    try:
        cursor.execute(sql, sid)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def getCourses():
    conn, cursor = getConnect()
    sql = 'select * from course'
    res = []
    try:
        cursor.execute(sql)
        conn.commit()
        for i in cursor.fetchall():
            res.append(i)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res


def getCourse(course_id):
    conn, cursor = getConnect()
    sql = 'select * from course where id = %s'
    res = []
    try:
        cursor.execute(sql, course_id)
        conn.commit()
        res = cursor.fetchall()[0]
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res


def add_course(course):
    conn, cursor = getConnect()

    sql = 'insert into course (id,name,description)values(%s,%s,%s)'
    try:
        cursor.execute(sql, course)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def update_course(course):
    conn, cursor = getConnect()
    sql = 'update course set name=%s,description=%s where id=%s'
    stu = (course[1], course[2], course[0])
    try:
        cursor.execute(sql, stu)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def getScore(course_id):
    conn, cursor = getConnect()
    sql = 'select s_id, s.name, college, class,score from results join student s on s.id = results.s_id where results.course_id ' \
          '= %s'
    res = []
    try:
        cursor.execute(sql, course_id)
        conn.commit()
        for i in cursor.fetchall():
            res.append(i)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res


def getTotalScore():
    conn, cursor = getConnect()
    sql = 'select s_id, s.name, college, class, sum(score) from results join student s on s.id = results.s_id  GROUP BY s_id,s.name '
    res = []
    try:
        cursor.execute(sql)
        conn.commit()
        for i in cursor.fetchall():
            res.append(i)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res


def add_score(sid, course_id, score):
    conn, cursor = getConnect()
    sql = 'insert into results (s_id, course_id, score) VALUES (%s,%s,%s)'
    try:
        cursor.execute(sql, (sid, course_id, score))
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def update_score(sid, course_id, score):
    conn, cursor = getConnect()
    sql = 'update results set score=%s where s_id=%s and course_id=%s'
    try:
        cursor.execute(sql, (score, sid, course_id))
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


def getSid():
    conn, cursor = getConnect()
    sql = 'select id from student'
    res = []
    try:
        cursor.execute(sql)
        conn.commit()
        for i in cursor.fetchall():
            res.append(i[0])
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res


def get_stu(sid, course_id):
    conn, cursor = getConnect()
    sql = 'select * from results where s_id=%s and course_id=%s'
    res = []
    try:
        cursor.execute(sql, (sid, course_id))
        conn.commit()
        for i in cursor.fetchall():
            res.append(i)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return res
