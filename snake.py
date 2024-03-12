# from tkinter import *
# from PIL import Image, ImageTk
# m = Tk()
# m.title("Snake Game")
# screen_width = m.winfo_screenwidth()
# screen_height = m.winfo_screenheight()
# m.geometry(f"{screen_width}x{screen_height}")

# snake1 = Image.open('snake1.png') 
# new = snake1.resize((320,320))
# s1 = ImageTk.PhotoImage(new)
# img = Label(m, image=s1)
# img.place(x=0,y=370)

# snake2 = Image.open('snake2.jpeg') 
# new = snake2.resize((320,320))
# s2 = ImageTk.PhotoImage(new)
# img = Label(m, image=s2)
# img.place(x=1030,y=370)


# # Cobra Chase


# import tkinter as tk

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Transparent Label")

# # Create a transparent label
# transparent_label = tk.Label(root, text="Transparent Label", bg="cyan", fg="black")
# transparent_label.pack()

# # Set transparency (alpha) level
# transparent_label.config(bg=root.cget('bg'))

# root.mainloop()


# from tkinter import*
# m = Tk()
# screen_width = m.winfo_screenwidth()
# screen_height = m.winfo_screenheight()
# m.geometry(f"{screen_width}x{screen_height}")
# m.title("Snake Game")
# m.configure(bg='light brown')
# m.mainloop()

import tkinter as tk

# Constants
WIDTH = 400  # Width of the game area
HEIGHT = 400  # Height of the game area
GRID_SIZE = 20  # Size of each grid cell

# Create a Tkinter window
root = tk.Tk()
root.title("Snake Game")

# Create a Canvas widget for the game area
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Draw border
border_color = "white"
canvas.create_rectangle(0, 0, WIDTH,  fill=border_color)  # Top border
canvas.create_rectangle(0, 0, HEIGHT, fill=border_color)  # Left border
canvas.create_rectangle(0, WIDTH, HEIGHT, fill=border_color)  # Bottom border
canvas.create_rectangle(WIDTH - GRID_SIZE, 0, WIDTH, HEIGHT, fill=border_color)  # Right border

# Other game elements (snake, food, etc.) would be added here

root.mainloop()
