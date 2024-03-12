from tkinter import *
from tkinter import ttk
import pyodbc
from tkinter import messagebox
from PIL import Image, ImageTk
m= Tk()
m.title("Hotel Room Booking")
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
m.geometry(f"{screen_width}x{screen_height}")
var1= StringVar()
var2= StringVar()
var3= StringVar()
var4= StringVar()
def Insert():
    conection = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                r'DBQ=C:\Users\Nabeed\Documents\Hotel.accdb;'))
    cursor = conection.cursor()
    cursor.execute(f"INSERT INTO Room(roomnumber,custumer,dateofcheckin,durationofstay) values('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}')")
    cursor.commit()
    messagebox.showinfo("One record has been added")
    Display()
def Display():
    con1= pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=C:\Users\Nabeed\Documents\Hotel.accdb;'))
    cursor1= con1.cursor()
    cursor1.execute("select * from Room order by roomnumber")
    data= cursor1.fetchall()
    style=ttk.Style()
    style.configure('Treeview.Heading',font=("Arial black",11,"bold"))
    tree_view=ttk.Treeview(m) 
    tree_view.tag_configure('font',font=('Arial',10))
    tree_view.tag_configure('bg', background="light pink") 
    tree_view['columns']=('1','2','3','4')
    tree_view.column("1", width=167)  
    tree_view.column("2", width=167)  
    tree_view.column("3", width=167)
    tree_view.heading('1',text="Room Number",anchor=W)
    tree_view.heading('2',text="Custumer",anchor=W)
    tree_view.heading('3',text="Date of Check In",anchor=W)
    tree_view.heading('4',text="Duration of Stay",anchor=W)
    for i in data:
        tree_view.insert('',index='end',values=(i[0],i[1],i[2],i[3]),tags=('font','bg'))  
    tree_view.place(x=400,y=75)
    con1.close()
def Delete():
    con1 = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                           r'DBQ=C:\Users\Nabeed\Documents\Hotel.accdb;'))
    cursor1 = con1.cursor()
    cursor1.execute(f"DELETE FROM Room where roomnumber= {var1.get()}")
    con1.commit()
    messagebox.showinfo("One record has been deleted")
    Display()
    
l1=Label(m,text="PC Hotel Room Booking",bg="black",fg="white",font=("Ariel",40))
l1.pack(side=TOP,fill=X)
f1=Frame(m,bd=5,bg="#3f92ff")
f1.place(x=10,y=75,width=500,height=700,)
img = Image.open('main.jpg')
rez = img.resize((250,180))
new = ImageTk.PhotoImage(rez)
image = Label(f1, image=new)
image.place(x=50,y=430)

l8=Label(f1,text="Let's start your booking!",bg="grey",fg="black",font=("Arial",10,'bold')).grid(row=0,column=1,pady=10,padx=10)
l2=Label(f1,text="Room number",bg="grey",fg="black",font=("Arial",12,'bold'),width=12).grid(row=2,column=0,pady=0,padx=0)
l3=Label(f1,text="Custumer",bg="grey",fg="black",font=("Arial",12,'bold'),width=12).grid(row=3,column=0,pady=0,padx=0)
l4=Label(f1,text="Date of check in",bg="grey",fg="black",font=("Arial",12,'bold'),width=12).grid(row=4,column=0,pady=0,padx=0)
l5=Label(f1,text="Duration of stay",bg="grey",fg="black",font=("Arial",12,'bold'),width=12).grid(row=5,column=0,pady=0,padx=0)
e1=Entry(f1,textvariable=var1,bg="white",fg="black",width=15)
e1.grid(row=2,column=1,pady=10,padx=0)
e2=Entry(f1,textvariable=var2,bg="white",fg="black",width=15)
e2.grid(row=3,column=1,pady=10,padx=0)
e3=Entry(f1,textvariable=var3,bg="white",fg="black",width=15)
e3.grid(row=4,column=1,pady=10,padx=0)
e4=Entry(f1,textvariable=var4,bg="white",fg="black",width=15)
e4.grid(row=5,column=1,pady=10,padx=0)
l9=Label(f1,text="For further details,Contact\n02134564460\n02134673250"
                 "\nKarachi",justify="left",bg="grey",fg="black",font=("Arial",11,'bold')).grid(row=9,column=0,pady=10,padx=10)

b1=Button(f1,text="Display",fg="white",bg="black",width=10,height=3,command=Display).grid(row=7,column=0,pady=5,padx=20)
b2=Button(f1,text="Insert",fg="white",bg="black",width=10,height=3,command=Insert).grid(row=7,column=1,pady=5,padx=20,)
b3=Button(f1,text="Delete",fg="white",bg="black",width=10,height=3,command=Delete).grid(row=8,column=0,pady=5,padx=20)
f2=Frame(m,bd=5,bg="white")
f2.place(x=400,y=75,width=900,height=700)

f3 = Frame(f2,width=900,height=40,bg='black')
f3.place(y=577)
m.mainloop()