"""
Author - Anant Luthra
Date - 5/1/22
Purpose - To try something newly learned.
"""

from tkinter import *
import wikipedia


def search_wiki(e):
    global conclusion 
    command = search.get()
    try:
        command = command.replace("wikepedia", "")
        results = wikipedia.summary(command, sentences=4)
        root.geometry("600x700")
        conclusion.configure(text=results)

    except wikipedia.exceptions.PageError:
        print("Could not find about the given data..")
    root.update()

# Basic details of our GUI =====================================================================================#

root = Tk()
root.geometry("600x330")
root.minsize("600", "330")
root.maxsize("620", "750")
root.config(bg="black")
root.title("Search Wikipedia")

# Widgets of GUI ========================================================================================================#

main_heading = Label(text="Search Wikipedia", font=("constantia", 30, "bold"),bg="black", fg="light green")
topic = Label(text="Enter Topic - ", font=("constantia", 30, "bold"), bg="black", fg="light yellow")

# Made string variabel for taking entery in it for searching wikipedia..

search = StringVar()
search_entery = Entry(textvariable=search, font=("century", 20))


# Button for searching on wikipedia =====================================================================================#
button1 = Button(text="Search", fg="light green", bg="black", font=("bell MT", 20, "bold"),
        command=lambda: search_wiki("e"))
conclusion = Label(text="", font=("mongolian baiti", 15),
         bg="light yellow", fg="Black", wraplength=550)

root.bind_all("<Return>", search_wiki)
# Packing widgets through .grid() funciton =============================================================================#

main_heading.grid(columnspan=2, pady=30, row=1)
topic.grid(row=2, padx=10)
search_entery.grid(row=2, column=1)
button1.grid(columnspan=2, row=3, pady=60)
conclusion.grid(columnspan=2)


root.mainloop()
