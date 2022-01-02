"""
Author = Anant Luthra
Date = 21/12/21
Purpose = Learning frames in tkinter and trying to make similar GUI like vs code :))
"""

from tkinter import * 

root = Tk()
root.title("VS Code")
root.geometry("500x500")
f1 = Frame(root, bg="green", borderwidth=5)
f2 = Frame(root, bg="green", borderwidth=5)
f3 = Frame(root, bg="green", borderwidth=5)
lable1 = Label(f1, text="Visual Studio Code",
 font="Comicsans 20 bold", foreground="White", bg="green")
lable2 = Label(f2, text="EXPLORER\n\n> TKINTER LEARNING\n> OUTLINE\n> TIMELINE",
 font="Arial 15", foreground="White", bg="green", borderwidth=5)
lable3 = Label(f3, text="PROBLEMS   OUTPUT   DEBUG_CONSOLE    TERMINAL",
 font="Arial 15", foreground="White", bg="green", borderwidth=5, padx=10)



f1.pack(side=TOP, fill=X)
f2.pack(side=LEFT, fill=Y)
f3.pack(side=BOTTOM, fill=X)
lable1.pack()
lable2.pack()
lable3.pack(anchor="sw")


root.mainloop()
