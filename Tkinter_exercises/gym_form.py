"""
Author - Anant luthra
Date - 23/12/21
Purpose - Making a GUI for form of registration for dance class.
"""

from tkinter import *
from PIL import Image, ImageTk
import datetime
date1 = (datetime.datetime.now().date())

def resposes_details(option):
    """
    This function is to write details in .txt file and also to print details on console.
    """
    name1 = name.get()
    age1 = age.get()
    gender1 = gender.get()
    mono1 = mono.get()
    if option == "submit":
        if name1 == "" or age1 ==  "" or gender1 == "" or mono1 == "":
            print("All details are required !!")
            return

        # if mono1.isnumeric() and age1.isnumeric():
        #     follow = True
        else:
            with open("dance_class.txt", "a") as f:
                f.write(f"Date - {date1}\nName - {name1}\nAge - {age1}\nGender - {gender1}\nMobile no. - {mono1}\n#-----------------------------------------------#\n")
            
                print("Successfully Submitted !!")

    elif option == "get":
        with open("dance_class.txt", "r") as f:
            data = f.read()
            if data == "":
                print("Not any responses yet !!")
            else:
                print(data)


# Basic details of our GUI window. ===============================================================#

root = Tk()
root.configure(bg="light yellow")
root.geometry("570x600")
root.minsize("455", "65")
# root.maxsize("442", "650")
root.title("Dance class registration form")

# Opening image for GUI ---------------------------------------------------------------------------#

image_file = Image.open("dance_class.png")
main_image = ImageTk.PhotoImage(image_file)

# Making labels for GUI window  -------------------------------------------------------------------#

header_image = Label(image=main_image)
main_heading = Label(text="Dance class registration form",
font="Times 30 bold", fg="black", bg="light yellow", padx=5, pady=5)
name_lable = Label(root, text="Name - ", font="Helvetica 20 italic")
age_lable = Label(root, text="Age - ", font="Helvetica 20 italic")
Gender_lable = Label(root, text="Gender - ", font="Helvetica 20 italic")
mono_lable = Label(root, text="Mobile no. - ", font="Helvetica 20 italic")

# Buttons for GUI ---------------------------------------------------------------------------------#

submit_button = Button(root, text="Submit", font="arial 15 bold", fg="Green", bg="yellow",
command=lambda: resposes_details("submit"))
reterive_button = Button(root, text="See all responses", font="arial 10 italic", fg="blue", bg="light yellow",
command=lambda: resposes_details("get"))

# Setting stringsvariables for input from user from entry widget ----------------------------------#

name = StringVar()
age = StringVar()
gender = StringVar()
mono = StringVar()

# Setting Entry Widgets ---------------------------------------------------------------------------#

name_entry = Entry(root, textvariable=name)
age_entry = Entry(root, textvariable=age)
gender_entry = Entry(root, textvariable=gender)
mono_entry = Entry(root, textvariable=mono)

# Packing elements through .grid() function --------------------------------------------------------#

main_heading.grid(padx=30, columnspan=2)
header_image.grid(row=4, pady=10, columnspan=2)
name_lable.grid(row=5, padx=10, pady=5)
age_lable.grid(row=6, padx=10, pady=5)
Gender_lable.grid(row=7, padx=10, pady=5)
mono_lable.grid(row=8, padx=10, pady=5)
submit_button.grid(row=9, padx=10, pady=27, columnspan=2)
reterive_button.grid(row=12, padx=10, columnspan=2)

# Now packing entry widget -------------------------------------------------------------------------#

name_entry.grid(row=5, column=1, padx=5, ipadx=25, ipady=12, pady=5)
age_entry.grid(row=6, column=1,padx=5, ipadx=25, ipady=12, pady=5)
gender_entry.grid(row=7, column=1,padx=5, ipadx=25, ipady=12, pady=5)
mono_entry.grid(row=8, column=1,padx=5, ipadx=25, ipady=12, pady=5)

root.mainloop()
