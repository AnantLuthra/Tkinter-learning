"""
Author = Anant Luthra
Date = 18/11/21
Purpose = Learning how to represent images in our GUI
"""

from tkinter import *
from PIL import ImageTk, Image
import os
images_files = []
files = os.listdir()
for i in files:
    if i.endswith(".png") or i.endswith(".jpg"):
        images_files.append(i)
print(images_files)
root = Tk()
root.geometry("500x500")
for i,Index in enumerate(images_files):
    print(Index)
    Photo = ImageTk.PhotoImage(file=i)
    data = Label(image=Photo)
    data.pack()


root.mainloop()
