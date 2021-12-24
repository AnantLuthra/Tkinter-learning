"""
Author - Anant luthra
Date - 23/12/21
Purpose - Making a GUI of submission of user name and password.
"""

from tkinter import *
import datetime
date1 = (datetime.datetime.now().date())

def submit_details():
    """
    This function stores user details in .txt file after checking the required condition. like all details are filled or not
    or captcha is checked or not.. after these all data will be recorded in a .txt file..
    """
    username = user_name_str.get()
    password = pass_str.get()
    not_robot = not_robot_check.get()
    if username == "" or password == "":
        print("All details are required !!")
        return
    elif not_robot != 1:
        print("First check \"I am not a robot\"")
        return
    else:
        with open("user_pass_dep.txt", "a") as f:
            f.write(f"Date - {date1}\nUser name - {username}\nPassword - {password}\n#-----------------------------------------------#\n")
        print("Successfully Submitted !!")

root = Tk()
root.geometry("380x380")
root.title("Login page")
root.config(bg="light yellow")

# Labels for GUI ---------------------------------------------------------------------------------------------------------------------------#

Label(text="Submit you username and\npassword", font="comicsans 20 bold", pady=9).grid(columnspan=2, pady=23, padx=10)
Label(text="User name - ", font="arial 15 italic", bg="light yellow").grid(row=3, pady=15)
Label(text="Password - ", font="arial 15 italic", bg="light yellow").grid(row=4, pady=15)

# Making variables for entery & checkbuttons -----------------------------------------------------------------------------------------------#

user_name_str = StringVar()
pass_str = StringVar()
not_robot_check = IntVar()

# Creating and packing entery & checkbutton through .grid() function. -------------------------------------------------------------------------#

Entry(textvariable=user_name_str).grid(row=3, column=1, ipady=10, ipadx=20)
Entry(textvariable=pass_str).grid(row=4, column=1, ipady=10, ipadx=20)
Checkbutton(variable=not_robot_check, text="I am not a robot", font="arial 13 italic", fg="Blue", bg="light yellow").grid(columnspan=2,
 ipadx=10, ipady=10, row=6)

# Creating submit button ---------------------------------------------------------------------------------------------------------------------#

Button(text="Submit", font="Arial 15 italic", bg="White", fg="Black", command=submit_details).grid(row=7, columnspan=2, pady=15)

root.mainloop()
