"""
Author - Anant Luthra
Date - 16/1/22
Purpose - To make a calculator GUI through tkinter.
"""

from tkinter import *

class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("380x480")
        self.title("Calculator - By Anant Luthra")
        self.wm_iconbitmap("calculator.ico")
        self.config(bg="#96170e")

    # def frame(self):
    #     self.frame_digits = Frame(self, height=)

    def give(self, digit):

        if digit == "=":
            value = eval(self.value.get())
        else:
            value = self.value.get() + digit

        
        self.value.set(value)
        self.update()

    def entry(self):
        self.value = StringVar()
        self.value.set("")
        self.entery = Entry(self, font=("Bahnschrift Light ", 25), textvariable=self.value, bg="#fa5137")
        self.entery.pack(fill=X, anchor="n", ipady=10, pady=5, padx=4)

    def numeric_buttons(self, number: str, row: int):
        
        if row == 1:
            self.button = Button(self, text=number, command=lambda: self.give(number), font=("cambria", 20), bg="#47120e")
            self.button.pack(side=LEFT, padx=2)
        
        elif row == 2:
            self.button = Button(self, text=number, command=lambda: self.give(number), font=("cambria", 20), bg="#47120e")
            self.button.pack(padx=2)

    def functions(self, sign):
        self.button = Button(self, text=sign, command=lambda: self.give(sign), font=("cambria", 20), bg="#96170e")
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

    window.numeric_buttons("3", 2)
    window.numeric_buttons("2", 2)
    window.numeric_buttons("1", 2)
    window.numeric_buttons("0", 2)

    window.functions("+")
    window.functions("-")
    window.functions("%")
    window.functions("*")
    window.functions("**")
    window.functions("/")
    window.functions("=")
    window.mainloop()
