"""
Author - Anant Luthra
Date - 24/1/22
Purpose - To make GUI like notepad in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os, pyautogui
from datetime import datetime


def open_file():
    """This function opens the file which is to be opened in the """
    global file

    file = askopenfilename(defaultextension=".txt,",
                            filetypes=[("text files", "*.txt"),
                            ("Text files", "*.txt")])

    if file == "":
        file = None

    else:

        # Clearing the present data and changing the title.
        root.title(os.path.basename(file) + " - Notepad")
        first_text.delete(1.0, END)

        # Getting the present text which in the file.
        with open(file, "r") as f:
            first_text.insert(1.0, f.read())


def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                    defaultextension=".txt,",
                            filetypes=[("text files", "*.txt"),
                            ("Text files", "*.txt")])

        if file == None:
            file = None

        else:
            # Saving as a new file.
            with open(file, "w") as f:
                f.write(first_text.get(1.0, END))

            root.title(os.path.basename(file) + " - Notepad")
    
    else:
        # Saving old file with new text data
        with open(file, "w") as f:
            f.write(first_text.get(1.0, END))

        root.title(os.path.basename(file) + " - Notepad")

def add_date_time():
    d = datetime.now()
    only_date = str(d.date())
    only_time = str(d.time())
    
    data = first_text.get(1.0, END)
    first_text.delete(1.0, END)

    if data == "\n":
        first_text.insert(1.0, f"{only_time}  {only_date}")
    else:
        first_text.insert(1.0, data + f"{only_time}  {only_date}")


    # datetime_list = only_date.split("-")
    # month = datetime_list[1]
    # date1 = datetime_list[2]


def new_window():
    os.startfile(r"E:\Python\Python projects\Tkinter learning\Tkinter_exercises\notepad_gui.py")

def new_file():
    global file
    root.title("Untitled - Anant Luthra")
    file = None
    first_text.delete(1.0, END)

def quit_app():
    root.destroy()

def cut():
    first_text.event_generate("<<Cut>>")

def paste():
    first_text.event_generate("<<Paste>>")

def copy():
    first_text.event_generate("<<Copy>>")

def delete():
    first_text.event_generate("<<Delete>>")

def find():
    pass

def show_info(title, message):
    msg.showinfo(title, message)

def print_data():
    data = first_text.get("1.0", END)
    print(data)
    first_text.delete("1.0", END)
    first_text.insert("1.0", "This is inserted through a command which is working properly.")

def send_feedback():
    """This function takes feedback from user of experience after using notepad."""

    def feedback_saver():
        """This function saves the stars given by the user to the notepad."""

        stars = percentage.get()
        name = name_variable.get()
        
        if name == "Your name":
            msg.showerror("Error", "Your name is required !")
            return

        with open("feedback.txt", "a") as f:
            f.write(f"{name}/{stars}\n")

    # Making a toplevel window to take feedback from the user.
    feedback_window = Toplevel(root)

    
    feedback_window.title("Feedback")
    feedback_window.maxsize("400", "400")
    Label(feedback_window, text="Give your rating from 5 star.", font="arial 15", pady=2).pack(side=TOP, pady=10)

    name_variable = StringVar()
    name_variable.set("Your name")

    # Entry widget for taking feedback sender's name. #
    Entry(feedback_window, textvariable=name_variable, font=("lucida", 12)).pack(anchor = "w", ipady=7 ,pady= 5, padx=10)

    # Scale widget for taking rating from the user.
    percentage = Scale(feedback_window, from_=1, to=5, orient=HORIZONTAL)
    percentage.set(5)
    percentage.pack(anchor="w", padx=15)
    

    Button(feedback_window, text="Submit", command = feedback_saver, font="arial 15").pack(pady=10)


root = Tk()
# Basic details of GUI's main window.
root.geometry("500x400")
root.title("Untitled - Anant Luthra")
root.wm_iconbitmap("notepad_icon.ico")

# Label for status bar.
status_bar = Label(root, text="Ready", font=("cambria", 11), relief = SUNKEN, padx = 5, anchor = "w")
status_bar.pack(side = BOTTOM, fill = X)

# Scrollbar for this GUI.
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(fill=Y, side=RIGHT)

# Making main text widget in which all data will be shown and edited.
first_text = Text(root, yscrollcommand= scrollbar.set, font=("book antiqua", 18))
file = None
first_text.pack(expand=True, fill=BOTH)

scrollbar.config(command=first_text.yview)

# Making main menu for all options and drop down list.
main_menu = Menu(root)

option1 = Menu(main_menu, tearoff=0)
option1.add_command(label="New", command=new_file)
option1.add_command(label="New window", command=new_window)
option1.add_command(label="Open", command=open_file)
option1.add_command(label="Save", command=save_file)
option1.add_command(label="Save As", command=lambda : print("Save as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Page setup", command=lambda : print("Page setup as command runed sucessfuly"))
option1.add_command(label="Print", command=print_data)
option1.add_separator()
option1.add_command(label="Exit", command=quit_app)

option2 = Menu(main_menu, tearoff=0)
option2.add_command(label="Undo", command=lambda: first_text.event_generate("<<Undo>>"))
option2.add_separator()
option2.add_command(label="Cut", command=cut)
option2.add_command(label="Copy", command=copy)
option2.add_command(label="Paste", command=paste)
option2.add_command(label="Delete", command=delete)
option2.add_separator()
option2.add_command(label="Search with Bing", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find", command=find)
option2.add_command(label="Find next", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find previous", command=lambda: print("Command runned successfly"))
option2.add_command(label="Replace", command=lambda: print("Command runned successfly"))
option2.add_command(label="Go to", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Select All", command=lambda: pyautogui.hotkey("Ctrl", "a"))
option2.add_command(label="Time/Date", command=add_date_time)

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

# Adding all menu's to main_menu
main_menu.add_cascade(label="File", menu=option1)
main_menu.add_cascade(label="Edit", menu=option2)
main_menu.add_cascade(label="Format", menu=option3)
main_menu.add_cascade(label="View", menu=option4)
main_menu.add_cascade(label="Help", menu=option5)

root.mainloop()
