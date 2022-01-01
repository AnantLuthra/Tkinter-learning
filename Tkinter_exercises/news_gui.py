"""
Author - Anant Luthra
Date - 1/1/22
Purpose - To make a newspaper GUI
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("900x600")
Label(text="This is total gaming news", font=("bell mt", 40)).pack(side=TOP)

frame1 = Frame(root, bg="light yellow")
file = Image.open("news.png")
image1 = ImageTk.PhotoImage(file)

Label(frame1, image=image1).pack(pady=40)
Label(frame1, text="This is noticed in ajjubhai's vidoes that he loves sooneta").pack(side=LEFT)



frame1.pack()
root.mainloop()