"""
Author - Anant Luthra
Date - 5/1/22
Purpose - To try something newly learned.
"""

from tkinter import *
import wikipedia


def search_wiki():
    global conclusion 
    command = search.get()
    try:
        # print("Searching Wikipedia....")
        command = command.replace("wikepedia", "")
        results = wikipedia.summary(command, sentences=2)
        conclusion.configure(text=results)
        # Label(text=simplified_text(results)).grid(columnspan=2)

    except wikipedia.exceptions.PageError:
        print("Could not find about the given data..")
    root.update()

root = Tk()
root.geometry("600x500")
root.minsize("600", "500")
# root.maxsize("600", "500")
root.config(bg="black")
root.title("Search Wikipedia")
Label(text="Search Wikipedia", font=("constantia", 30, "bold"),bg="black", fg="light green").grid(
    columnspan=2, pady=30)
Label(text="Enter Topic - ", font=("constantia", 30, "bold"), bg="black", fg="light yellow").grid(row=1, padx=10)
search = StringVar()
search_entery = Entry(textvariable=search, font=("century", 20))
search_entery.grid(row=1, column=1)
Button(text="Search", fg="light green", bg="black", font=("bell MT", 20, "bold"),
command=search_wiki).grid(columnspan=2, row=2, pady=60)
conclusion = Label(text="",font=("mongolian baiti", 10),
         bg="light yellow", fg="Black", wraplength=550)
conclusion.grid(columnspan=2)
root.mainloop()
