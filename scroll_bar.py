"""
Author - Anant Luthra
Date - 10/1/22
Purpose - To learn about scrollBar in tkinter, how to make it in our GUI
"""

from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title("Made first ScrollBar in our GUI")
root.geometry("550x510")
root.config(bg="#f2e9ce")


def do_element(command):
    """This function adds element in our List box through the value entered by the user in entry widget's variable value"""

    if command == "add":

        if list_element.get() == "":
            msg.showinfo("Error !!", "Enter item name in box below to insert it in list. Don't let it empty.")
            return

        list1.insert(ACTIVE, f"{list_element.get()}")
        list_element.set("")

    elif command == "delete":
        list1.delete(ACTIVE)

        
# Main heading Label.

Label(root, text="To do list, add your\ndaily tasks.", font=("constantia", 30), bg="#f6ffcf").pack(fill=X, side=TOP, pady=7)


# list1 = Listbox(root, font=("Verdana", 14, "underline"), bg="grey")

list1 = Listbox(root, background="#cef2ed", font=("georgia", 12, "italic"))
list1.pack(pady=20)

# Setting values of Listbox which will be their as default values.

list1.insert(1, "GUI 1 video")
list1.insert(1, "Maths exercise 1 of 7th chapter")
for i in range(201):
    list1.insert(END, f"This is {i}th element")

list_element = StringVar()

# Making entery widget for getting value of another elements for adding in Listbox.

Entry(root, textvariable=list_element, font=("book antiqua", 12)).pack(ipady=7, pady=15)

frame1 = Frame(root, borderwidth=5, height=200, bg="#f2e9ce")
frame1.pack(side=BOTTOM, pady=15)

our_scroll_bar = Scrollbar(root)
our_scroll_bar.pack()

# Our button which will add element in list box by add_element() function.

Button(frame1, text="Add element", font="comicsans 15", command=lambda: do_element("add")).pack(pady=4, padx=7, side=LEFT)
Button(frame1, text="Remove element", font="comicsans 15", command=lambda: do_element("delete")).pack(pady=4, side=LEFT)


root.mainloop()

