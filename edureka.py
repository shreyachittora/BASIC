import tkinter  #importing tinkter module to make things work

window = tkinter.Tk()
window.title("Edureka") # title of the window

#creating two frames i.e.; bottom and top

top_frame = tkinter.Frame(window).pack(side = "top")
bottom_frame = tkinter.Frame(window).pack(side="bottom")

# creating  4 buttons in the window

btn1 = tkinter.Button(top_frame, text="Button1", fg = "red",bg = "white").pack()
btn2 = tkinter.Button(top_frame, text="Button2", fg = "green",bg = "white").pack()
btn3 = tkinter.Button(bottom_frame, text="Button3", fg = "purple",bg = "white").pack(side = "left")
btn4 = tkinter.Button(bottom_frame, text="Button4", fg = "orange",bg = "white").pack(side = "right")

window.mainloop()

