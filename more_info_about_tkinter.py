"""
Author - Anant Luthra
Date - 15/1/22
Purpose - To practice more functions and tips & tricks of tkinter.
"""

from tkinter import *
import tkinter.messagebox as msg


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("Testing.")
        self.config(bg="Black")
        self.wm_iconbitmap("testing_icon.ico")
        
    def screen_size(self):
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        msg.showinfo("Done", "Size changed.")

    def buttons(self):
        button1 = Button(self, text="Change window size", command=self.screen_size, bg="#6a7317", fg="white", font=("arial", 25, "italic"))
        button1.pack(side=BOTTOM, pady=170)


if __name__ == "__main__":
    window = GUI()
    button_hamra = window.buttons()
    window.mainloop()
    