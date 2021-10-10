from tkinter import *

root = Tk();

title = Label(root, text="Upload a song to check its genre")

def handleClick():
    label = Label(root, text="Fill this with music prediction logic")
    label.grid(row=1, column=0)

button = Button(root, text="Click Me", command=handleClick, fg="black", bg="white")

title.grid(row=0, column=0)
button.grid(row=2, column=0)


root.mainloop()