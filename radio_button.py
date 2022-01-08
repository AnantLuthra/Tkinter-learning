"""
Author - Anant Luthra
Date - 8/1/22
Purpose - To learn about radio buttons in tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.geometry("500x400")
root.title("Injected radio buttons.")

main_var = IntVar()
main_var.set(1)

"""
Radio button widget is like MCQs in exam, once we select any one option and after that when we select another
option then previously selected option is diselected and in other words we can say at one time only one option 
can be selected. 
"""

Label(root, text="")
readio_button_1 = Radiobutton(root, )


root.mainloop()
