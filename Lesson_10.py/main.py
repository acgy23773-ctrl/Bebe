from tkinter import *

mainWindow = Tk()
width = 700
height = 400
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
x_offset = (screen_width - width) // 2
y_offset = (screen_height - height) // 2
mainWindow.geometry(f"{width}x{height}+{x_offset}+{y_offset}")






mainWindow.mainloop()
