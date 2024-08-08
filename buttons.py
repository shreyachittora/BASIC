import tkinter 
from tkinter import *

root = Tk()

root.geometry("400x600")
root.title("Button Tutorial")

#function command for button1

def button1_do():
    print("This is done by BUTTON 1") # this o/p will b shown in terminal/console because the button functionality will be happenning in backend. it will not show up in our window/frame in event loop.


frame = Frame(root, borderwidth=4, bg="grey", relief=SUNKEN)
# frame.pack(side=LEFT, anchor="w")
frame.pack(pady=120)

button1 = Button(frame, fg="black", text="Click Me", command=button1_do)
button1.pack()


root.mainloop()

