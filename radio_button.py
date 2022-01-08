"""
Author - Anant Luthra
Date - 8/1/22
Purpose - To learn about radio buttons in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.geometry("600x400")
root.title("Injected radio buttons.")

def choose():
    msg.showinfo("Congratulations", f"You have choosed {main_var.get()} with {slide_var.get()}% surety in which almost no one went !")

# main_var = IntVar()   
main_var = StringVar()  # Or we can create string var for our radio buttons as our wish  
slide_var = IntVar()
slide_var.set(20)
main_var.set("Just programmer")

"""
Radio button widget is like MCQs in exam, once we select any one option and after that when we select another
option then previously selected option is diselected and in other words we can say at one time only one option 
can be selected. 
"""

Label(root, text="What would you choose as your future?", font=("californian fb", 26)).pack(
    fill=X, pady=15)

"""
We can put same name of Radiobutton and pack them directly this will also work and putting their different names 
and packing them seperatly will be same as below.
"""

# radio_button_1 = Radiobutton(root, text="Web Dev", variable=main_var, value=1, font=("arial", 15)).pack(pady=5, anchor="w", padx=70)
# radio_button_1 = Radiobutton(root, text="GUI dev", variable=main_var, value="nacho", font=("arial", 15)).pack(pady=5, anchor="w", padx=70)
# radio_button_1 = Radiobutton(root, text="Ethical Hacker", variable=main_var, value=3, font=("arial", 15)).pack(pady=5, anchor="w", padx=70)
# radio_button_1 = Radiobutton(root, text="Ml expert", variable=main_var, value=4, font=("arial", 15)).pack(pady=5, anchor="w", padx=70)

radio_button_1 = Radiobutton(root, text="Web Dev", variable=main_var, value="Web Dev", font=("arial", 15))
radio_button_2 = Radiobutton(root, text="GUI Dev", variable=main_var, value="GUI Dev", font=("arial", 15))
radio_button_3 = Radiobutton(root, text="Ethical Hacker", variable=main_var, value="Ethical Hacker", font=("arial", 15))
radio_button_4 = Radiobutton(root, text="ML Expert", variable=main_var, value="ML Expert", font=("arial", 15))

radio_button_1.pack(pady=5, anchor="w", padx=70)
radio_button_2.pack(pady=5, anchor="w", padx=70)
radio_button_3.pack(pady=5, anchor="w", padx=70)
radio_button_4.pack(pady=5, anchor="w", padx=70)

Label(text="Surety in %", font=("comicsans", 15, "italic")).pack()
Scale(root, from_=0, to=100, orient=HORIZONTAL, variable=slide_var).pack(pady=6)

Button(root, text="Choose", font=("book antiqua", 18), command=choose).pack(pady=10)

root.mainloop()
