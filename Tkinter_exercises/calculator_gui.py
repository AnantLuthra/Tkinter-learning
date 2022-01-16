"""
Author - Anant Luthra
Date - 16/1/22
Purpose - To make a calculator GUI through tkinter.
"""

from tkinter import *

class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Calculator - By Anant Luthra")
        self.wm_iconbitmap("calculator.ico")

    def entry(self):
        self.value = StringVar()
        self.value.set("")
        

if __name__ == "__main__":
    window = Calculator()
    
    window.mainloop()
