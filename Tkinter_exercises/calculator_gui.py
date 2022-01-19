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

    def all_buttons(self):
        
        self.frame1 = Frame(self, height=100, width=380, bg="")
        
        # button 9
        self.button = Button(self.frame1, text="9", command=lambda: self.give("9"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=1, row=1)

        # button 8
        self.button = Button(self.frame1, text="8", command=lambda: self.give("8"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6",  pady=13, padx=14)
        self.button.grid(padx=2, column=2, row=1)

        # button 7
        self.button = Button(self.frame1, text="7", command=lambda: self.give("7"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=3, row=1)

        # sign %
        self.button = Button(self.frame1, text="%", command=lambda: self.give("%"), font=("cambria", 25), bg="#49b7e6", pady=20, padx=12)
        self.button.grid(padx=2, column=4, row=1)

        # button 6
        self.button = Button(self.frame1, text="6", command=lambda: self.give("6"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=1, row=2)

        # button 5
        self.button = Button(self.frame1, text="5", command=lambda: self.give("5"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=2, row=2)

        # button 4
        self.button = Button(self.frame1, text="4", command=lambda: self.give("4"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=3, row=2)

        # sign -
        self.button = Button(self.frame1, text="-", command=lambda: self.give("-"), font=("cambria", 25), bg="#49b7e6", pady=20, padx=24)
        self.button.grid(padx=1, column=4, row=2)

        # button 3
        self.button = Button(self.frame1, text="3", command=lambda: self.give("3"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=1, row=3)

        # button 2
        self.button = Button(self.frame1, text="2", command=lambda: self.give("2"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=2, row=3)

        # button 1
        self.button = Button(self.frame1, text="1", command=lambda: self.give("1"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=3, row=3)

        # sign +
        self.button = Button(self.frame1, text="+", command=lambda: self.give("+"), font=("cambria", 25), bg="#49b7e6", pady=13, padx=14)
        self.button.grid(padx=2, column=4, row=3)

        # button 0
        self.button = Button(self.frame1, text="0", command=lambda: self.give("0"), font=("cambria", 25),
                             bg="#75c4e6", activebackground="#91cce6", pady=13, padx=14)
        self.button.grid(padx=2, column=2, row=4)


        self.frame1.pack(fill=X, side=TOP)


if __name__ == "__main__":
    window = Calculator()

    window.entry()
    window.all_buttons()

    # window.functions("+")
    # window.functions("-")
    # window.functions("%")
    # window.functions("*")
    # window.functions("**")
    # window.functions("/")
    # window.functions("=")
    # window.functions("C")
    window.mainloop()
