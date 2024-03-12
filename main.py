# import pandas as pd
# SERIES ONE DIMENTIONAL
# data = [1,2,3,4]
# series = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(series)
# print(type(series))

# DATAFRAME TWO DIMENTIONAL
# data1 =[1,2,3,4,5]
# df = pd.DataFrame(data1)
# print(df)

# dic = {'fruits':['apple', 'banana', 'orange', 'grapes'], 'count':[10,20,30,40]}
# df = pd.DataFrame(dic)
# print(df)

# data = pd.Series([1,2,3,4],index=['a','b','c','d'])
# df = pd.DataFrame(data)
# print(df)

# data = pd.Series({'Students':['Nabeed', 'talha', 'Awwab'], 'course':['Pl','FIT','DS']})
# df = pd.DataFrame(data)
# print(df)

# import numpy as np
# numpyarray = np.array([['Nabeed', 'Talha'], [50000,60000]])
# data = pd.DataFrame({'Names': numpyarray[0], "Salary": numpyarray[1]})
# print(data)

# player = ['Nabeed','Abyaz','Awwab']
# point = [10,9,8]
# title = ['Game1','Game2','Game3']
# df1 = pd.DataFrame({'Players':player, 'Points':point, 'Title':title})
# # print(df1)

# player = ['Karim','Ashan','Ayan']
# power = ['punch','kick','elbow']
# title = ['Game1','Game2','Game6']
# df2 = pd.DataFrame({'Players':player,'Power':power,'Title':title})
# # print(df2)

# x = df1.merge(df2, on='Title', how='inner')
# # y = df1.merge(df2, on='Title', how='outer')
# print(x)

# player = ['Nabeed','Abyaz','Awwab']
# point = [10,9,8]
# title = ['Game1','Game2','Game3']
# df1 = pd.DataFrame({'Players':player, 'Points':point, 'Title':title})
# # print(df1)

# player = ['Nabeed','Ashan','Ayan']
# power = ['punch','kick','elbow']
# title = ['Game1','Game2','Game6']
# df2 = pd.DataFrame({'Players':player,'Power':power,'Title':title})
# # print(df2)

# x = df1.merge(df2, on='Players', how='inner')
# x = df1.merge(df2)


# x = df1.merge(df2, on='Players', how='left')
# x = df1.merge(df2, on='Players', how='right')
# x = df1.merge(df2, on='Players', how='outer')
# print(x)
# print(y)

# IN merge both dataset must contain atleast one common attribute name

# import tkinter as tk
# from math import *

# class ScientificCalculator(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Scientific Calculator")
#         self.geometry("400x600")

#         self.result_var = tk.StringVar()

#         # Entry widget to display the result
#         result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=4,
#                                 width=15, justify='right', background="lightgray")
#         result_entry.grid(row=0, column=0, columnspan=4)

#         # Button layout for the calculator
#         buttons = [
#             ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#             ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#             ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#             ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
#             ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
#             ('(', 6, 0), (')', 6, 1), ('log', 6, 2), ('exp', 6, 3),
#             ('Clear', 7, 0), ('^', 7, 1), ('pi', 7, 2), ('^2', 7, 3),
#         ]

#         # Create buttons and add them to the grid
#         for (text, row, col) in buttons:
#             btn = tk.Button(self, text=text, padx=20, pady=20, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
#             btn.grid(row=row, column=col)

#     def on_button_click(self, button_text):
#         current_text = self.result_var.get()

#         if button_text == '=':
#             try:
#                 result = eval(current_text)
#                 self.result_var.set(result)
#             except Exception as e:
#                 self.result_var.set("Error")

#         elif button_text == 'Clear':
#             self.result_var.set("")

#         else:
#             current_text += button_text
#             self.result_var.set(current_text)


# if __name__ == "__main__":
#     calculator = ScientificCalculator()
#     calculator.mainloop()


# list1 = [10,20,30,40,50]
# list2 = [2,4,0,5,10,6]
# for i in range(6):
#     try:
#         result = list1[i] / list2[i]
#         print(result)
#     except ArithmeticError:
#         print("Cannot divided by zero")
#     except IndexError:
#         print("Index out of range")

def stats(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            # Count lines, words, and characters
            line_count = len(content.splitlines())
            word_count = len(content.split())
            char_count = len(content)

            # Print the results
            print(f"line count: {line_count} word count: {word_count} character count: {char_count}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
stats('example.txt')
