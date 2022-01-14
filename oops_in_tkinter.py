"""
Author - Anant Luthra
Date - 12/1/22
Purpose - To learn about using object oriented programming in tkinter.
"""

from tkinter import *

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("Welcome screen")
        self.config(bg="#bbf0af")
    
    def status_bar(self):
        self.var = "Ready"
        self.main_kuch = Label(self, text=self.var, anchor="w", relief=SUNKEN, font="arial", padx=7).pack(side=BOTTOM, fill=X)

    def button_creator(self, text1):
        Button(self, text=text1, font="comicsans 15"
        , command = lambda: print("Command runned successfuly")).pack()
    
    def label_adder(self, text1):
        Label(self, text = text1, font="arial").pack()


if __name__ == '__main__':
    window = GUI()
    window.button_creator("Click here")
    window.status_bar()
    window.label_adder("Ban gaya dekh lo")
    window.mainloop()
