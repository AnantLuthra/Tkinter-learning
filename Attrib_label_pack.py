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
from tkinter import font
from PIL import ImageTk, Image

nach_root = Tk() # Making a instance of class Tk()
nach_root.geometry("1080x600") # Default size of our window.
nach_root.minsize("500", "500") # Minimumsize of our window
nach_root.maxsize("1090", "650") # Maxsize of our window
nach_root.title("Siya")  # Our browser's title.
imagefile = Image.open("bird.png") # Opening our image for loading it on a lable.
photo1 = ImageTk.PhotoImage(image=imagefile)
image1 = Label(image=photo1) # Making a label of image to show on our window.
main_heading = Label(text="Welcome to Siya browser",bg="sky blue",underline=0-22, fg="white",padx=5, pady=5, borderwidth=5,
 font="opensans 20 bold", relief=RAISED)  # main label with specifications.
browser_search1 = Label(text="SIYA", font="arialrounded 80 bold", fg="Black") # Another label of text as main Heading of our browser.
search_button = Label(text="Search:-", cursor="dot", font="bookman 26 italic", fg="black") # Search button of our broswer..
bottom_strip = Label(text="Ready !!", bg="Blue", fg="white", font="Arial 30 bold")

# Important pack options.. Attributes of "Pack()"
# - ANCHOR = S=south, E=East, W=West, N=North.
# - Side = top, bottom, left, RIGHT
# Fill = X, Ytime

main_heading.pack(side=TOP, anchor="s", fill=X)  # 
search_button.pack(side=TOP, anchor="nw")
browser_search1.pack(side=TOP, anchor="s")   # packing all labels to show on window.
bottom_strip.pack(side=BOTTOM, anchor="s", fill=X)

image1.pack()
nach_root.mainloop() # Setting up main loop.
