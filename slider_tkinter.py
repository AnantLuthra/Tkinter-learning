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

# Here is a label

def get_girls():
    msg.showinfo("Outcome",
     f"So your order have been sent to the basement. You will receive {second_slider.get()} girls in 1 hour at your door.")
    msg.showinfo("Oops !!",
     "This message has also sent to your parents. So be ready for 50 chappal of your mother and 50 slaps of your father.")

Label(root, text="How many girlfriends do you want?", font=("candara", 30), bg="#ebe213").pack(fill=X, pady=15)


# While making Slider we give an argument named as tickinterval for marking values as per the given value by the user.
second_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)

# To set default value of our slider we use .set() function.

second_slider.set(20)
second_slider.pack(pady=25)

Button(text="Get", font=("bookman old style", 20), command=get_girls, bg="#e6e4b1").pack(pady=50)

root.mainloop()
