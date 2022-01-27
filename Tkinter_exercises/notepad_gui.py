"""
Author - Anant Luthra
Date - 24/1/22
Purpose - To make GUI like notepad in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg

root = Tk()

def open_file():
    pass

def save_file():
    pass

def new_file():
    pass

def quit_app():
    pass

def cut():
    pass

def paste():
    pass

def copy():
    pass

def delete():
    pass

def find():
    pass

def show_info(title, message):
    msg.showinfo(title, message)

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
option1.add_command(label="New", command=new_file)
option1.add_command(label="New window", command=lambda : print("New widow command runed sucessfuly"))
option1.add_command(label="Open", command=open_file)
option1.add_command(label="Save", command=save_file)
option1.add_command(label="Save As", command=lambda : print("Save as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Page setup", command=lambda : print("Page setup as command runed sucessfuly"))
option1.add_command(label="Print", command=lambda : print("Print as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Exit", command=quit_app)

option2 = Menu(main_menu, tearoff=0)
option2.add_command(label="Undo", command=lambda: print("Command runned successfly"))
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
