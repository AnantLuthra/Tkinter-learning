"""
Author - Anant Luthra
Date - 24/1/22
Purpose - To make GUI like notepad in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg
root = Tk()

def show_info(title, message):
    msg.showinfo(title, message)

def send_feedback():
    """This function takes feedback from user of experience after using notepad."""

    def feedback_saver():
        """This function saves the stars given by the user to the notepad."""
        stars = percentage.get()
        name = name_variable.get()
        with open("feedback.txt", "a") as f:
            f.write(f"{name}/{stars}\n")

    feedback_window = Toplevel(root, bg="#79fcd9")
    # feedback_window.geometry("300x200")
    feedback_window.title("Feedback")
    Label(feedback_window, text="Give your rating from 5 star.", font="arial 25", pady=2).pack(side=TOP, pady=10)
    name_variable = StringVar()
    name_variable.set("Your name")
    Entry(feedback_window, textvariable=name_variable, font=("lucida", 18)).pack(ipady=7 ,pady= 5)
    percentage = Scale(feedback_window, from_=0, to=5, orient=HORIZONTAL)
    percentage.set(5)
    percentage.pack(side=TOP)

    Button(feedback_window, text="Submit", command = feedback_saver, font="arial 15").pack(pady=10)

root.geometry("500x400")
root.title("Untitled - Anant Luthra")
root.wm_iconbitmap("notepad_icon.ico")

Label(root, text="Ready", font=("cambria", 11), relief = SUNKEN, padx = 5, anchor = "w").pack(side = BOTTOM, fill = X)

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

first_text = Text(root, yscrollcommand= scrollbar.set, font=("book antiqua", 18))
first_text.pack(fill=BOTH)

scrollbar.config(command=first_text.yview)

main_menu = Menu(root)

option1 = Menu(main_menu, tearoff=0)
option1.add_command(label="New", command=lambda : print("new command runed sucessfuly"))
option1.add_command(label="New window", command=lambda : print("New widow command runed sucessfuly"))
option1.add_command(label="Open", command=lambda : print("Open command runed sucessfuly"))
option1.add_command(label="Save", command=lambda : print("Save command runed sucessfuly"))
option1.add_command(label="Save As", command=lambda : print("Save as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Page setup", command=lambda : print("Page setup as command runed sucessfuly"))
option1.add_command(label="Print", command=lambda : print("Print as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Exit", command=exit)

option2 = Menu(main_menu, tearoff=0)
option2.add_command(label="Undo", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Cut", command=lambda: print("Command runned successfly"))
option2.add_command(label="Copy", command=lambda: print("Command runned successfly"))
option2.add_command(label="Paste", command=lambda: print("Command runned successfly"))
option2.add_command(label="Delete", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Search with Bing", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find next", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find previous", command=lambda: print("Command runned successfly"))
option2.add_command(label="Replace", command=lambda: print("Command runned successfly"))
option2.add_command(label="Go to", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Select All", command=lambda: print("Command runned successfly"))
option2.add_command(label="Time/Date", command=lambda: print("Command runned successfly"))

option3 = Menu(main_menu, tearoff=0)
option3.add_command(label="Word Wrap", command=lambda: print("Command runned successfly"))
option3.add_command(label="Font...", command=lambda: print("Command runned successfly"))

option4 = Menu(main_menu, tearoff=0)
option4.add_command(label="Zoom", command=lambda: print("Command runned successfly"))
option4.add_command(label="Status Bar", command=lambda: print("Command runned successfly"))

option5 = Menu(main_menu, tearoff=0)
option5.add_command(label="View Help", command=lambda: print("Command runned successfly"))
option5.add_command(label="Send Feedback", command=send_feedback)
option5.add_separator()
option5.add_command(label="About Notepad", command=lambda: show_info("About", "This notepad is developed by Anant luthra."))

root.config(menu=main_menu)
main_menu.add_cascade(label="File", menu=option1)
main_menu.add_cascade(label="Edit", menu=option2)
main_menu.add_cascade(label="Format", menu=option3)
main_menu.add_cascade(label="View", menu=option4)
main_menu.add_cascade(label="Help", menu=option5)

root.mainloop()
