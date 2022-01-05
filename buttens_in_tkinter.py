"""
Author - Anant Luthra
Date - 21/12/21
Purpose - Exploring buttons in Tkinter, and making a GUI to tell 
"""

from tkinter import *
import wikipedia

def search_wiki(command):
    try:
        print("Searching Wikipedia....")
        command = command.replace("wikepedia", "")
        results = wikipedia.summary(command, sentences=3)
        print(results)

    except wikipedia.exceptions.PageError:
        print("Could not find about the given data..")

def print_command():
    print("Hello world")

# Arguments of buttons
# - (frame_name, fg=text_color, font=same as label, command=name of function)

# How to pass arguments required by the provided fuction for the button.
# We do it though lambda function

# button1 = Button(frame1, text="Submit", command= lambda: name_of_function("Anant"))

root = Tk()
root.title("Exploring buttons in Tkinter")
root.geometry("700x600")
root.minsize("300", "300")

# Frames


frame1 = Frame(root, borderwidth=6, bg= "Light green", relief=SUNKEN)
frame2 = Frame(root, borderwidth=40, bg= "sky blue")

# Labels

lable1 = Label(frame1, text="Press the button of required person's wikipedia",
 bg="Light green", fg="Black", font="comicsans 22 italic")

# Buttons

b3 = Button(frame2, text="Sharukh Khan", fg="brown", font="Arial 10 italic",
 command=lambda : search_wiki("sharukh khan"))
b4 = Button(frame2, text="Narendra Modi", fg="brown", font="Arial 10 italic",
 command=lambda : search_wiki("Narendra Modi"))
b2 = Button(frame1, text="Print \"Hello world\"", fg="brown",
 font="Arial 10 italic", command=print_command)
close_button = Button(frame1, text="Close", bg="Pink", fg="Black", font="comicsans 15 bold",
 command=exit, pady=-20, padx=35)
frame1.pack(side=TOP, fill=X)
frame2.pack(side=TOP, fill=X, pady=20)
close_button.pack(anchor="ne", padx=10)
lable1.pack(fill=X)
close_button.pack(side=TOP, fill=X)
b4.pack(side=TOP)
b3.pack()
b2.pack()

root.mainloop()
