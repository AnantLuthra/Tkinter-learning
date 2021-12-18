"""
Author - Anant Luthra
Date - 18/12/21
Purpose - To make welcome screen of Pycharm
"""

from tkinter import *
from PIL import ImageTk, Image
root = Tk()

# gui logic yaha pr.
# Width x height.
root.geometry("700x510")
# width, height
root.minsize("600", "490")
# width, height
root.maxsize("720", "520")
heading = Label(
    text="PyCharm Community Edition", font="Arial 20 bold")
sub_text1 = Label(text="Version-2020.3.2\n\n", font="Cooper 15")
sub_text2 = Label(text=":- Create New project", font="Comicsans 12")
sub_text3 = Label(text=":- Check Out our pro version", font="Comicsans 12")
sub_text4 = Label(text=":- Shorya is a very shy person.", font="Comicsans 12")
sub_text5 = Label(text=":- Checkout my insta for DM - @anant_luthra_07", font="cambria 12")
root.title("Pycharm welcome Screen")
file = Image.open("pycharm.jpg")
main_image = ImageTk.PhotoImage(file) # for printing text in our window..
logo_image = Label(image=main_image)
logo_image.pack()
heading.pack()
sub_text1.pack()
sub_text2.pack()
sub_text3.pack()
sub_text4.pack()
sub_text5.pack()

root.mainloop()
