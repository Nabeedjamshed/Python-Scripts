# File: university_app.py
import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch and display data
def display_data():
    connection = sqlite3.connect("university.db")
    cursor = connection.cursor()

    # Execute SQL query to fetch data
    query = """
        SELECT Teacher.name, Teacher.designation, Teacher.salary, Dept.dname, Courses.cname, Courses.credithrs
        FROM Teacher
        JOIN Dept ON Teacher.deptid = Dept.deptid
        LEFT JOIN Courses ON Teacher.Tid = Courses.Tid
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    # Display data in a Tkinter window
    window = tk.Tk()
    window.title("University Database")

    tree = ttk.Treeview(window, columns=("Name", "Designation", "Salary", "Department", "Course", "Credit Hours"), show="headings")

    for col in ("Name", "Designation", "Salary", "Department", "Course", "Credit Hours"):
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack()

    window.mainloop()

if __name__ == "__main__":
    # Call the display_data function
    display_data()
