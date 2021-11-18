from tkinter import *
root = Tk()

# gui logic yaha pr.
# Width x height.
root.geometry("733x434")
# width, height
root.minsize("733", "434")
# width, height
root.maxsize("733", "434")
main_txt = Label(
    text="PyCharm Community Edition\nVersion-2020.3.2\n\n\n:- Create New project\n:- Open\n:- Check Out our pro version")
main_txt.pack() # for printing text in our window..
root.mainloop()

