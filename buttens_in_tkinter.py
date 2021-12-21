"""
Author - Anant Luthra
Date - 21/12/21
Purpose - Exploring buttons in Tkinter, and making a GUI to tell 
"""
from tkinter import *
from tkinter import font
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


root = Tk()
root.title("Exploring buttons in Tkinter")
root.geometry("700x600")
root.minsize("300", "300")
frame1 = Frame(root, borderwidth=6, bg= "Light green", relief=SUNKEN)
frame2 = Frame(root, borderwidth=40, bg= "sky blue")
lable1 = Label(frame1, text="Press the button of required person's wikipedia",
 bg="Light green", fg="Black", font="comicsans 22 italic")
b3 = Button(frame2, text="Sharukh Khan", fg="brown", font="Arial 10 italic",
 command=lambda : search_wiki("sharukh khan"))
b4 = Button(frame2, text="Narendra Modi", fg="brown", font="Arial 10 italic",
 command=lambda : search_wiki("Narendra Modi"))
b2 = Button(frame1, text="Print \"Hello world\"", fg="brown",
 font="Arial 10 italic", command=print_command)
close_button = Button(frame1, text="Close", bg="Black", fg="White", font="comicsans 15 bold",
 command=exit, pady=1)

frame1.pack(side=TOP, fill=X)
frame2.pack(side=TOP, fill=X, pady=20)
close_button.pack(anchor="ne", padx=10)
lable1.pack(fill=X)
close_button.pack(side=TOP)
b4.pack(side=TOP)
b3.pack()


root.mainloop()
