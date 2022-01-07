"""
Author - Anant Luthra
Date - 7/1/22
Purpose - To Explore message box in tkinter
"""

from tkinter import *
import tkinter.messagebox as msg

root = Tk()

root.geometry("750x550")
root.title("Notepad")

def send_feedback():

    # For just showing info about.
    # msg.showinfo("Feedback", "Was your experience good?")

    a = msg.askquestion("Feedback", "Was your experience good?")
    if a == "yes":
        msg.showinfo("Thanks", "Please rate us on Microsoft store..")
    else:
        msg.showinfo("Thanks", "Thanks for feedback !!")
        

def girlfriend_checker(name):
    if name == "Vibhuti":
        a = msg.askyesno("Sent", "What do you think?, She will accept your request or not?")
        if a:
            msg.showinfo(
                "Oh bro", "Do you think one girl who have hundred's of requests of boys from your school will accept your request, if you think this you are fool")
        else:
            msg.showinfo("Good job", "Good bro ignoring girls is an art, three things can destroy a man\n1: Money\n2: Power\n3: Hole")

    elif name == "Anamika":
        a = msg.askyesno("Sent", "What do you think?, She will accept your request or not?")
        
        if a:
            msg.showinfo(
                "Oh bro", "Oh bro, Do you think one girl who have hundred's of requests of boys from your school will accept your request, if you think this you are fool\nOnly topper's request in acceptable")
            msg.showinfo("Another info", "Basically these girl accept request of those boys who are of full kamina thinking.")

        else:
            msg.showinfo("Good job", "Good bro ignoring girls is an art, three things can destroy a man\n1: Money\n2: Power\n3: Hole")
    
    elif name == "Sneha":
        msg.showinfo(":))", "Do you even know about this girl, or you are just sending this request knowing that she is a girl, having a girl in your life is blessing, so bro your thinking is wrong!!")

    else:    
        # msg.askquestion("Here is a question", "what is the name of your crush")
        a = msg.askyesnocancel("Serious question", "Are you a virgin")
        if a:
            msg.showinfo("Sorry !", "Sorry bro you can go on your work !!")
        elif a == False:
            msg.showinfo("Guess", "So I guess you are serious for your future, so I appreciate you good job bro just keep struggling.")
        else:
            pass


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
option5.add_command(label="Send Feedback", command=send_feedback)
option5.add_separator()
option5.add_command(label="About Notepad", command=lambda: print("Command runned successfly"))

option6 = Menu(main_menu, tearoff=0)
option6.add_command(label="Vibhuti", command=lambda: girlfriend_checker("Vibhuti"))
option6.add_command(label="Anamika", command=lambda: girlfriend_checker("Anamika"))
option6.add_command(label="Sneha", command=lambda: girlfriend_checker("Sneha"))
option6.add_command(label="I don't want", command=lambda : girlfriend_checker("Dont want"))

root.config(menu=main_menu)
main_menu.add_cascade(label="File", menu=option1)
main_menu.add_cascade(label="Edit", menu=option2)
main_menu.add_cascade(label="Format", menu=option3)
main_menu.add_cascade(label="View", menu=option4)
main_menu.add_cascade(label="Help", menu=option5)
main_menu.add_cascade(label="Girldfriend", menu=option6)

main_content = StringVar()
main_entery = Entry(textvariable=main_content, font=("arial rounded mt bold", 20))
main_entery.pack(ipadx=750, ipady=550)


root.mainloop()
