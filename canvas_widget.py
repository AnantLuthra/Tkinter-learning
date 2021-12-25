"""
Author - Anant Luthra
Date - 25/12/21
Purpose - To learn canvas widget in tkinter
"""

from tkinter import *

root = Tk()
root.config(bg="light yellow")

canvas_height = 600
canvas_width = 600
root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=200)
canvas_widget.pack()

x1 = 0
y1 = 0
x2 = 300
y2 = 300
canvas_widget.create_line(x1, y1, x2, y2)


root.mainloop()
