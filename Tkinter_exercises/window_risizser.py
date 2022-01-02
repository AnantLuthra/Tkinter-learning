"""
Author - Anant Luthra
Date - 2/1/22
Purpose - To solve the exercise of window resizer problem
"""

def resize_the_window():
    width1 = (width.get())
    height1 = height.get()
    try:
        root.geometry(f"{width1}x{height1}")
    except Exception as e:
        print(e)


from tkinter import *

root = Tk()
root.geometry("500x350")
root.config(bg="light blue")
root.title("Resize your window.")

# widgets in the GUI window.

# here are some lables and direct packing through .gird()

Label(text="Enter your window size.", font=("pushster", 35, "italic")).grid(row=0, columnspan=2, pady=15)
Label(text="Width :-", font=("calisto mt", 20, "italic")).grid(row=1, column=0)
Label(text="Height :-", font=("calisto mt", 20, "italic")).grid(row=2, column=0)

# Making button
Button(text="Submit", font="arial 15", command=resize_the_window, activebackground="light green",
 activeforeground="Red",
 highlightbackground="light blue",
 highlightcolor="blue").grid(
    columnspan=2, row=3, pady=25)
    
# assigning string variables()

width = StringVar()
height = StringVar()

# Making entery widget

width_entery = Entry(root, textvariable=width, width=20)
height_entery = Entry(root, textvariable=height, width=20)

width_entery.grid(row=1, column=1, ipady=10, ipadx=25)
height_entery.grid(row=2, column=1, ipady=10, ipadx=25)


root.mainloop()
