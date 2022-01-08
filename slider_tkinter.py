"""
Author - Anant Luthra
Date - 7/1/22
Purpose - To learn about sliders in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.geometry("750x550")
root.title("Slider test kr liye tumhare bhai ne.")
root.config(bg="#232bc2")

# Sliders are basically their for getting user experience through slid bars, in this we get the value through 
# the value which have been set by the user.

# Slider which is verticle 

# first_slider = Scale(root, from_=0, to=100, orient=VERTICAL)
# first_slider.pack()

# Here is a label.

def get_followers():
    msg.showinfo("Outcome",
     f"You will get {second_slider.get()} followers in 24 hours.")

Label(root, text="How many insta followers do you want?", font=("candara", 30), bg="#ebe213").pack(fill=X, pady=15)


# While making Slider we give an argument named as tickinterval for marking values as per the given value by the user.
second_slider = Scale(root, from_=0, to=10000, orient=HORIZONTAL)
second_slider2 = Scale(root, from_=0, to=10000, orient=HORIZONTAL)

# To set default value of our slider we use .set() function.
second_slider2.pack(pady=20)
second_slider.set(20)
second_slider.pack(pady=25)

Button(text="Get", font=("bookman old style", 20), command=get_followers, bg="#e6e4b1").pack(pady=50)

root.mainloop()
