# import pyodbc

# con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#                      r'DBQ=d:\Project.accdb;'))

# cur = con.cursor()

# cur.execute('SELECT Teachers.TeacherID, Course.CourseName FROM Teachers, Course WHERE Teachers.TeacherID = Course.TeacherID')

# data = cur.fetchall()

# for i in data:
#     print(i)

import pyodbc
con = pyodbc.connect((r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                      r"DBQ=d:\Project.accdb;"))
cur = con.cursor()
cur.execute("SELECT Teachers.Name, Course.CourseName FROM Teachers, Course WHERE Teachers.Name=Course.Name")
data = cur.fetchall()
for i in data:
    print(i)