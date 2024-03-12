# from tkinter import *
# from tkinter import messagebox
#
# lst = ['green', 'yellow', 'blue', 'pink', 'teal', 'brown', 'orange', 'purple', 'yellow', 'green']
#
#
# def Message():
#     messagebox.showinfo(title='Message', message="Welcome to Pl Lab")
#
#
# def Table():
#     table_no = int(e1.get())
#     table_ran = int(e2.get())
#     for i in range(1, table_ran + 1):
#         # if i == 4:
#         #     continue
#         # else:
#         z = table_no, 'x', i, '=', table_no * i
#         Label(m, text=z, bg=lst[i - 1], fg='black', width=12, font=('Time New Roman', 12)).grid(row=i, column=4,
#                                                                                                 padx=10, pady=10)
#
#
# def Add():
#     x = int(e1.get())
#     y = int(e2.get())
#     z = x + y
#     l4.config(text=z)
#
#
# def Subtract():
#     x = int(e1.get())
#     y = int(e2.get())
#     z = x - y
#     l4.config(text=z)
#
#
# def Product():
#     x = int(e1.get())
#     y = int(e2.get())
#     z = x * y
#     Label(m, text=z, bg='red', fg='white', width=20, font=('Time New Roman', 20)).grid(row=4, column=2, padx=10,
#                                                                                        pady=10)
#
#
# def Divide():
#     x = int(e1.get())
#     y = int(e2.get())
#     z = x / y
#     l4.config(text=z)
#
#
# m = Tk()
# m.config(bg='purple')
# l1 = Label(m, text="Enter no 1", bg='pink', fg='black', font=('Time New Roman', 11), width=12).grid(row=0, column=0,
#                                                                                                     pady=10, padx=15)
# l2 = Label(m, text="Enter no 2", bg='pink', fg='black', font=('Time New Roman', 11), width=12).grid(row=1, column=0,
#                                                                                                     pady=10, padx=15)
# l3 = Label(m, text="Result", bg='pink', fg='black', font=('Time New Roman', 11), width=12).grid(row=2, column=0,
#                                                                                                 pady=10, padx=15)
# l4 = Label(m, bg='grey', fg='black', font=('Time New Roman', 11), width=13)
# l4.grid(row=2, column=1, pady=10, padx=15)
# e1 = Entry(m, bg='grey', fg='black')
# e1.grid(row=0, column=1, pady=10)
# e2 = Entry(m, bg='grey', fg='black')
# e2.grid(row=1, column=1, pady=10)
# b1 = Button(m, text='Add', bg='blue', fg='white', font=('Time New Roman', 14), width=10, command=Add).grid(row=3,
#                                                                                                            column=0,
#                                                                                                            padx=20,
#                                                                                                            pady=10)
# b2 = Button(m, text='Subtract', bg='blue', fg='white', font=('Time New Roman', 14), width=10, command=Subtract).grid(
#     row=4, column=0, padx=20, pady=10)
# b3 = Button(m, text='Multiply', bg='blue', fg='white', font=('Time New Roman', 14), width=10, command=Product).grid(
#     row=5, column=0, padx=20, pady=10)
# b4 = Button(m, text='Divide', bg='blue', fg='white', font=('Time New Roman', 14), width=10, command=Divide).grid(row=6,
#                                                                                                                  column=0,
#                                                                                                                  padx=20,
#                                                                                                                  pady=10)
# b5 = Button(m, text='Table-Generator', bg='blue', fg='white', font=('Time New Roman', 14), width=15,
#             command=Table).grid(row=7, column=0, padx=20, pady=10)
# b6 = Button(m, text='Message', bg='blue', fg='white', font=('Time New Roman', 14), width=15, command=Message).grid(
#     row=8, column=0, padx=20, pady=10)
# m.mainloop()

from tkinter import *
from tkinter import messagebox

def Message():
    messagebox.showerror(title='Message', message='There is some error')
def Add():
    x = int(e1.get())
    y = int(e2.get())
    z = x + y
    l4.config(text=z)
def Subtract():
    x = int(e1.get())
    y = int(e2.get())
    z = x - y
    l4.config(text=z)
def Multiply():
    x = int(e1.get())
    y = int(e2.get())
    z = x * y
    Label(text=z,bg='red',fg='black',width=20,font=('Arial',15)).grid(row=3,column=2,padx=10,pady=10)
def Divide():
    x = int(e1.get())
    y = int(e2.get())
    z = x / y
    l4.config(text=z)
lst = ['green', 'yellow', 'blue', 'pink', 'teal', 'brown', 'orange', 'blue', 'yellow', 'green']
def Table():
    table_no = int(e1.get())
    table_range = int(e2.get())
    for i in range(1, table_range+1):
        z = table_no,'x', i, '=', table_no*i
        Label(m, text=z, bg=lst[i-1], fg='black', width=12,font=('Arial',10)).grid(row=i,column=3,padx=10,pady=10)
m = Tk()
m.config(bg='purple')

l1 = Label(m, text='Enter no 1',bg='pink',fg='black',width=12,font=('Arial',10)).grid(row=0,column=0,padx=10,pady=10)
l2 = Label(m, text='Enter no 2',bg='pink',fg='black',width=12,font=('Arial',10)).grid(row=1,column=0,padx=10,pady=10)
l3 = Label(m, text='Result',bg='pink',fg='black',width=12,font=('Arial',10)).grid(row=2,column=0,padx=10,pady=10)
l4 = Label(m, bg='grey',fg='black',width=12,font=('Arial',10))
l4.grid(row=2,column=1,padx=10,pady=10)
e1 = Entry(m, bg='grey',fg='black',width=12,font=('Arial',10))
e1.grid(row=0,column=1,padx=10,pady=10)
e2 = Entry(m, bg='grey',fg='black',width=12,font=('Arial',10))
e2.grid(row=1,column=1,padx=10,pady=10)
b1 = Button(m, text='Add',bg='blue',fg='black',width=15,font=('Arial',10),command=Add).grid(row=3,column=0,padx=10,pady=10)
b2 = Button(m, text='Subtract',bg='blue',fg='black',width=15,font=('Arial',10),command=Subtract).grid(row=4,column=0,padx=10,pady=10)
b3 = Button(m, text='Multiply',bg='blue',fg='black',width=15,font=('Arial',10),command=Multiply).grid(row=5,column=0,padx=10,pady=10)
b4 = Button(m, text='Divide',bg='blue',fg='black',width=15,font=('Arial',10),command=Divide).grid(row=6,column=0,padx=10,pady=10)
b5 = Button(m, text='Table-Generator',bg='blue',fg='black',width=15,font=('Arial',10),command=Table).grid(row=7,column=0,padx=10,pady=10)
b6 = Button(m, text='Message',bg='blue',fg='black',width=15,font=('Arial',10),command=Message).grid(row=8,column=0,padx=10,pady=10)
m.mainloop()

from tkinter import *
m = Tk()
m.config(bg='purple')
l1= Label(m, text='Place').place(x=0,y=0)
l2= Label(m, text='Place').place(x=200,y=200)
l3 = Label(m, text='Place').place(x=400,y=400)
m.mainloop()