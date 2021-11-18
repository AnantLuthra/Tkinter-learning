"""
Author = Anant Luthra
Date = 18/11/21
Purpose = Learning how to represent images in our GUI
"""

from tkinter import *

root = Tk()
root.geometry("3840x2160")
root.minsize("3840", "2160")
root.maxsize("3840", "2160")
image2 = PhotoImage(file="back_image.png")
stuff = Label(text="Welcome to guess the number\nMade by Anant luthra", image=image2)

stuff.pack()

root.mainloop()
