"""
Author - Anant Luthra
Date - 12/1/22
Purpose - To learn about using object oriented programming in tkinter.
"""

from tkinter import *

class GUI(Tk):

    # def __init__(self):
        # super().__init__()
        # self.geometry("500x400")
        # self.title("OOPs made GUI.")
        # self.config = ("red")

    def __init__(self, size, title, config: tuple):
        super().__init__()
        print(f"size is-{size}, title is-{title}, config is-{config}")
        self.geometry = size
        self.title = title
        self.config = config[0]
        
    def button_creator(self, text, font, command):
        self = Button()

if __name__ == '__main__':
    # window = GUI()
    window = GUI("500x400", "Welcome", ("red"))

    window.mainloop()
