"""
Author - Anant Luthra
Date - 25/12/21
Purpose - To learn canvas widget in tkinter
"""

from tkinter import *

root = Tk()
root.title("3D illision")
root.config(bg="light blue")

canvas_height = 600
canvas_width = 600
root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height, bg="light yellow")
canvas_widget.pack()

# can pass values from variable's like this.

# x1 = 0
# y1 = 0
# x2 = 600
# y2 = 600

# For creating a line in our canvas we have to give x1 and y1 and x2 and y2 of two points in which between
# the line will be created.
# example--
# -------------------------------------------------------------
#    0    1    2    3    4    5    6    7    8    9           |
# 0                                                           |
# 1       \------ Here x1 and y1 will be (1, 1)               |
# 2        \                                                  |
# 3         \                                                 |
# 4          \                                                |
# 5           \                                               |
# 6            \                                              |
# 7             \------Here x2 and y2 will be (2, 7)          |
# 8                                                           |
# 9                                                           |
# -------------------------------------------------------------
canvas_widget.create_line(0, 0, 600, 600, fill="Blue")
canvas_widget.create_line(600, 0, 0, 600, fill="Blue")
canvas_widget.create_line(0, 300, 600, 300, fill="Blue")
canvas_widget.create_line(300, 0, 300, 600, fill="Blue")

# For making a rectange in our canvas we use canvas_widget.create_rectangle(x1, y1, x2, y2)
# For making a rectange we have to give the coordinates of top left corner and bottom left corner's coordinates
# example--    Here x1 and y1 will be (1, 1) 
# -----------/-----------------------------------------------
#    0    1 /  2    3    4    5    6    7    8    9           |
# 0        /________________________                          |
# 1       |                         |                         |
# 2       |                         |                         |
# 3       |                         |                         |
# 4       |                         |                         |
# 5       |                         |                         |
# 6       |                         |                         |___________
# 7       |_________________________|/------Here x2 and y2 will be (6, 7) |      
# 8                                                           |-----------/
# 9                                                           |
# -------------------------------------------------------------

canvas_widget.create_rectangle(150, 150, 450, 450)
canvas_widget.create_rectangle(160, 160, 440, 440)


canvas_widget.create_rectangle(200, 200, 400, 400)
canvas_widget.create_rectangle(210, 210, 390, 390)


canvas_widget.create_rectangle(100, 100, 500, 500)
canvas_widget.create_rectangle(110, 110, 490, 490)

canvas_widget.create_rectangle(50, 50, 550, 550)
canvas_widget.create_rectangle(60, 60, 540, 540)

canvas_widget.create_rectangle(250, 250, 350, 350)
canvas_widget.create_rectangle(260, 260, 340, 340)


canvas_widget.create_rectangle(275, 275, 325, 325)
canvas_widget.create_rectangle(285, 285, 315, 315, fill="light blue")

# Creating text in our canvas .. for that we have to give the center coordinates of text.

canvas_widget.create_text(300, 25, text="3D ILLISION", font=("footlight mt light", 30 ,"bold"))

# Now creating an oval through .create_oval(x1, y1, x2, y2)

canvas_widget.create_oval(60, 60, 540, 540)
canvas_widget.create_oval(160, 160, 440, 440)
canvas_widget.create_oval(210, 210, 390, 390)
canvas_widget.create_oval(110, 110, 490, 490)
canvas_widget.create_oval(260, 260, 340, 340)


# Exploring another create functions of canvcas widget.

# canvas_widget.create_polygon(60, 60, fill="green")

root.mainloop()
