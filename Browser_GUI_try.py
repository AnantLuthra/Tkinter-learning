"""
Author - Anant Luthra
Date - 18/12/21
Purpose - Practice attributes of label.
"""

from tkinter import *
from PIL import Image, ImageTk

shorya_root = Tk()

# important label options
# text - adds the text
# bd - background
# fg - foreground
# font=("Algerian", 20, "bold")
# font - sets the font
# padx - x padding
# pady - y padding 
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

shorya_root.geometry("700x600")
# shorya_root.minsize("500", "500")
# shorya_root.maxsize("500", "500")
shorya_root.title("Hamara browser")
file = Image.open("bird.png")
image1 = ImageTk.PhotoImage(file)
shorya_lable = Label(text="Welcome to our private browser..",bg ="Blue", fg="White", padx=10,
pady=12, font=("Algerian", 20, "bold"))
shory2_photo_lable = Label(image=image1)

shorya_lable.pack()
shory2_photo_lable.pack()
shorya_root.mainloop()
