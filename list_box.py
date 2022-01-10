"""
Author - Anant Luthra
Date - 9/1/22
Purpose - To learn about listbox widget in Tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg

"""
List box is a widget in tkinter which basically works like a list, where we want to show items
in a similar way then we can use List Box widget.
"""

root = Tk()
root.geometry("550x460")
root.title("Listbox inside our GUI")
root.config(bg="#67ebd9")


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

Label(root, text="List of tkinter widgets", font=("constantia", 30), bg="#f6ffcf").pack(fill=X, side=TOP, pady=7)

list1 = Listbox(root, background="#cef2ed", font=("georgia", 12, "italic"))

list1.pack(pady=20)

# Setting values of Listbox which will be their as default values.

list1.insert(1, "Label")
list1.insert(1, "Listbox")
list1.insert(1, "Button")
list1.insert(1, "Radiobutton")

list_element = StringVar()

# Making entery widget for getting value of another elements for adding in Listbox.

Entry(root, textvariable=list_element, font=("book antiqua", 12)).pack(ipady=7, pady=15)

frame1 = Frame(root, borderwidth=5, height=200, bg="#67ebd9")
frame1.pack(side=BOTTOM, pady=15)

# Our button which will add element in list box by add_element() function.

Button(frame1, text="Add element", font="comicsans 15", command=lambda: do_element("add")).pack(pady=4, padx=7, side=LEFT)
Button(frame1, text="Remove element", font="comicsans 15", command=lambda: do_element("delete")).pack(pady=4, side=LEFT)

root.mainloop()
