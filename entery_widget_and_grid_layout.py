"""
Author - Anant luthra
Date - 22/12/21
Purpose - To learn and practice entery widget and grid layout in tkiter.
"""

from tkinter import *
root = Tk()
root.geometry("470x300")
root.title("Tell your name")
def submit_kr():
    print(f"Your name is {main_name_entery.get()}")
    print(f"and your sir name is {sir_name_entery.get()}")



name = Label(root, text="Enter your name and sir name\nin the following boxes",
 font=("bell MT", 20),
fg="Green", bg="cyan", padx=80)

# lable_name.grid(row=1, column=2) -> Another way to showing a lable or etc on our GUI window
# This function is like pack function but this works like cells in excel
# like their are rows and coloumn in excel and similiar concept applies here.
name.grid(column=2)


# ----------------------------------------------------------------------------------------#

# Variable classes in tkinter
# StringVar, IntVar, BooleanVar, DoubleVar 

# String_Var 

main_name = StringVar()
sir_name = StringVar()

main_name_entery = Entry(root, textvariable= main_name, width=20)
sir_name_entery = Entry(root, textvariable= sir_name, width=20)


# arguments of .grid() function. ---------------------------------------------------------# 

# - row=10 .. same as MS Excel
# - column=10 .. same as MS Excel
# - ipadx and ipady = inner size of entry box
# - padx and pady = spaces to leave from x and y axis of the label.


main_name_entery.grid(row=6, column=2, pady=10, ipadx=20, ipady=16)
sir_name_entery.grid(row=8, column=2,pady=10, ipadx=20, ipady=16)

Button(root, text="OK", font="comicsans 20 italic", bg="Green",
 fg="white", relief=SUNKEN, command=submit_kr).grid(row=10, column=2)


root.mainloop()


#-----------------------------------------------------------------------------------------#