from tkinter import *

root = Tk()

entry = Entry(root, width=50)
entry.pack()

title = Label(root, text="Upload a song to check its genre")

def handleClick():
    label = Label(root, text="Fill this with music prediction logic")
    label.pack()

def printEntry():
    hello = "Hello there " + entry.get()
    label = Label(root, text=hello)
    label.pack()

button = Button(root, text="Click Me", command=printEntry, fg="blue", bg="red")

button.pack()

root.mainloop()