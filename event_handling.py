"""
Author - Anant Luthra
Date - 30/12/21
Purpose - To learn event handling in tkinter.
"""

from tkinter import *

root = Tk()

# Basic details of GUI window.

root.title("Events in tkinter")
root.geometry("500x500")
button1 = Button(root, text="Click on me", font=("arial rounded mt bold", 40), bg="light grey") # Made a button

button1.pack(anchor="n", pady=150)        # And simply packed it through .pack() function

# after  packing of a button if we use .bind() function in that first we give the event like left click of mouse etc
# So we give event in first attribute and a function name as a second attribute, so if the event occurres that fuction will run.

# Different events of mouse
# left click - <Button-1>
# mouse wheel click - <Button-2>
# right click - <Button-3>

# For double click
# '<Double-Button-3>' = This event means double right click.

button1.bind('<Double-Button-3>', lambda event: print("Double Right click"))    # Now made a bind event handler 
button1.bind('<Double-Button-1>', lambda event: print("Double left click"))
button1.bind('<Button-1>', lambda event: print("Left click"))
button1.bind('<Button-3>', lambda event: print("Right click"))
button1.bind('<Button-2>', lambda event: print("Middle click"))
button1.bind('<Button-4>', lambda event: print("Middle click"))



root.mainloop()