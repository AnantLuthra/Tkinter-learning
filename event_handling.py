"""
Author - Anant Luthra
Date - 30/12/21
Purpose - To learn event handling in tkinter.
"""

from tkinter import *

def do_your_task(event):
    print("You have done your task now you can just logout after sending the log files.")
    
root = Tk()

# Basic details of GUI window.

root.title("Events in tkinter")
root.geometry("500x500")
button1 = Button(root, text="Warning !!") # Made a button
button1.pack(anchor="n", pady=100)        # And simply packed it through .pack() function
button1.bind('<DoubleClick>', do_your_task)    # Now made a bind event handler 


root.mainloop()
