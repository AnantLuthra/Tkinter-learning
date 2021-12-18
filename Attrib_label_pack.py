# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# root.geometry("500x500")
# root.maxsize()
# root.title("Tere bhai ki GUI")

# # important label options
# # text - adds the text
# # bd - background
# # fg - foreground
# # font - sets the font
# # padx - x padding
# # pady - y padding 
# # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# root.mainloop()

from tkinter import *
from PIL import ImageTk, Image

nach_root = Tk()
nach_root.geometry("500x500")
nach_root.minsize("500", "500")
nach_root.maxsize("500", "500")
nach_root.title("Free anything.")
photo1 = Image.open("bird.png")
photo2 = ImageTk.PhotoImage(photo1)
# Image2 = ImageTk.PhotoImage("1.png")
nacho = Label(text="Mare bina kisi dar ke..", image=photo2)
nacho.pack()

nach_root.mainloop()
