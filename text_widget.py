"""
Author - Anant luthra
Date - 11/1/22
Purpose - To test Text widget in tkinter.
"""

from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Text in tkinter like a notepad")

"""
For connecting scroll bar to a widget
1: Widget (yscrollcommand = scrollbar.set)
2: scrollbar.config(command=widget.yview)
"""



scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

first_text = Text(root, yscrollcommand= scrollbar.set, font=("book antiqua", 18))
first_text.pack(fill=BOTH)

scrollbar.config(command=first_text.yview)

main_menu = Menu(root)

option1 = Menu(main_menu, tearoff=0)
option1.add_command(label="New", command=lambda : print("new command runed sucessfuly"))
option1.add_command(label="New window", command=lambda : print("New widow command runed sucessfuly"))
option1.add_command(label="Open", command=lambda : print("Open command runed sucessfuly"))
option1.add_command(label="Save", command=lambda : print("Save command runed sucessfuly"))
option1.add_command(label="Save As", command=lambda : print("Save as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Page setup", command=lambda : print("Page setup as command runed sucessfuly"))
option1.add_command(label="Print", command=lambda : print("Print as command runed sucessfuly"))
option1.add_separator()
option1.add_command(label="Exit", command=lambda : print("Exit as command runed sucessfuly"))

option2 = Menu(main_menu, tearoff=0)
option2.add_command(label="Undo", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Cut", command=lambda: print("Command runned successfly"))
option2.add_command(label="Copy", command=lambda: print("Command runned successfly"))
option2.add_command(label="Paste", command=lambda: print("Command runned successfly"))
option2.add_command(label="Delete", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Search with Bing", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find next", command=lambda: print("Command runned successfly"))
option2.add_command(label="Find previous", command=lambda: print("Command runned successfly"))
option2.add_command(label="Replace", command=lambda: print("Command runned successfly"))
option2.add_command(label="Go to", command=lambda: print("Command runned successfly"))
option2.add_separator()
option2.add_command(label="Select All", command=lambda: print("Command runned successfly"))
option2.add_command(label="Time/Date", command=lambda: print("Command runned successfly"))

option3 = Menu(main_menu, tearoff=0)
option3.add_command(label="Word Wrap", command=lambda: print("Command runned successfly"))
option3.add_command(label="Font...", command=lambda: print("Command runned successfly"))

option4 = Menu(main_menu, tearoff=0)
option4.add_command(label="Zoom", command=lambda: print("Command runned successfly"))
option4.add_command(label="Status Bar", command=lambda: print("Command runned successfly"))

option5 = Menu(main_menu, tearoff=0)
option5.add_command(label="View Help", command=lambda: print("Command runned successfly"))
option5.add_command(label="Send Feedback", command=lambda: print("Command runned successfly"))
option5.add_separator()
option5.add_command(label="About Notepad", command=lambda: print("Command runned successfly"))

root.config(menu=main_menu)
main_menu.add_cascade(label="File", menu=option1)
main_menu.add_cascade(label="Edit", menu=option2)
main_menu.add_cascade(label="Format", menu=option3)
main_menu.add_cascade(label="View", menu=option4)
main_menu.add_cascade(label="Help", menu=option5)



root.mainloop()
