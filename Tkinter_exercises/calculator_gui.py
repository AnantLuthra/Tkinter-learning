"""
Author - Anant Luthra
Date - 16/1/22
Purpose - To make a calculator GUI through tkinter.
"""

from tkinter import *

class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("380x470")
        self.title("Calculator - By Anant Luthra")
        self.wm_iconbitmap("calculator.ico")
        self.config(bg="#13aaeb")

    def frame(self):
        "This function is made for making frames in which our calculator's buttons will be placed."

        frame1 = Frame(self, height=100, width=380)
        frame1.pack(fill=X)

    def give(self, digit):
        "This function is used to handle pressed button action. wheather it's a digit or a function button"

        if digit == "=":
            value = eval(self.value.get())
        elif digit == "C":
            value = ""
        else:
            value = self.value.get() + digit

        self.value.set(value)
        self.update()

    def entry(self):
        "This function is used to make entry widget for visible calculations."
        self.value = StringVar()
        self.value.set("")
        self.entery = Entry(self, font=("Bahnschrift Light ", 25), textvariable=self.value, bg="#b7dbeb")
        self.entery.pack(fill=X, anchor="n", ipady=10, pady=5, padx=4)

    def numeric_buttons(self, number: str, row: int):
        
        self.frame1 = Frame(self, height=100, width=380)
        self.button = Button(self.frame1, text=number, command=lambda: self.give(number), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6")
        self.button.pack(padx=2, side=LEFT)

        
        self.frame1.pack(fill=X, side=TOP)

        # if row == 1:
        #     self.frame1 = Frame(self, height=100, width=380)
        #     self.button = Button(self.frame1, text=number, command=lambda: self.give(number), font=("cambria", 20),
        #                             bg="#75c4e6", activebackground="#91cce6")
        #     self.button.pack(padx=2, side=LEFT)
        #     self.frame1.pack(fill=X, side=TOP)

        # elif row == 2:
        #     self.frame2 = Frame(self, height=100, width=380)
        #     self.button = Button(self.frame2, text=number, command=lambda: self.give(number), font=("cambria", 20),
        #                             bg="#75c4e6", activebackground="#91cce6")
        #     self.button.pack(padx=2, side=LEFT)
        #     self.frame2.pack(fill=X, side=TOP)

        # elif row == 3:
        #     self.frame3 = Frame(self, height=100, width=380)
        #     self.button = Button(self.frame3, text=number, command=lambda: self.give(number), font=("cambria", 20),
        #                             bg="#75c4e6", activebackground="#91cce6")
        #     self.button.pack(padx=2, side=LEFT)
        #     self.frame3.pack(fill=X, side=TOP)

        # elif row == 4:
        #     self.frame4 = Frame(self, height=100, width=380)
        #     self.button = Button(self.frame4, text=number, command=lambda: self.give(number), font=("cambria", 20),
        #                             bg="#75c4e6", activebackground="#91cce6")
        #     self.button.pack(padx=2, side=LEFT)
        #     self.frame4.pack(fill=X, side=TOP)

        # elif row == 5:
        #     self.frame5 = Frame(self, height=100, width=380)
        #     self.button = Button(self.frame5, text=number, command=lambda: self.give(number), font=("cambria", 20),
        #                             bg="#75c4e6", activebackground="#91cce6")
        #     self.button.pack(padx=2, side=LEFT)
        #     self.frame5.pack(fill=X, side=TOP)
        
        

    def functions(self, sign):
        self.button = Button(self, text=sign, command=lambda: self.give(sign), font=("cambria", 20), bg="#49b7e6")
        self.button.pack(side=LEFT, padx=2)



if __name__ == "__main__":
    window = Calculator()

    window.entry()
    window.numeric_buttons("9", 1)
    window.numeric_buttons("8", 1)
    window.numeric_buttons("7", 1)
    window.numeric_buttons("6", 2)
    window.numeric_buttons("5", 2)
    window.numeric_buttons("4", 2)
    window.numeric_buttons("3", 3)
    window.numeric_buttons("2", 3)
    window.numeric_buttons("1", 3)
    window.numeric_buttons("0", 4)

    window.functions("+")
    window.functions("-")
    window.functions("%")
    window.functions("*")
    window.functions("**")
    window.functions("/")
    window.functions("=")
    window.functions("C")
    window.mainloop()
