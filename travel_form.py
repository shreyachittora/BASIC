
# WHAT'S NEW:
# using checkboxes 
# taking user inupts: 


from tkinter import *

root = Tk()

# function for submission
def submit():
    print("Form got submitted") # gets printed in console/terminal

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), addressvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")

    with open("travel.txt", "a") as t:  #opening a text file in write(w) or append(a) mode
        t.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), addressvalue.get(), paymentmodevalue.get(),foodservicevalue.get()}\n")

# this makes a travel.txt file in out folder and saves the entered values inside it.
# get() and set() are two functions in python used while inputting or setting up values
# the checkbox returns '1' when selected and '0' when not in get function
# the "f" string used to print multiple values at one time as a string




root.geometry("600x600")
root.title("LAXMI TRAVELS TRAVEL FORM")



# main_frame = Frame(root)
# main_frame.grid(row= 0, column=1, pady=30)

# heading
Label(root, text="Welcome to LAXMI TRAVELS :)", font="comicsans 15 bold", bg="chocolate").grid(padx=10, pady=10)

#variables
name = Label(root, text="Name")
phone = Label(root, text="Phone No.")
address = Label(root, text="Address")
gender = Label(root, text="Gender")
paymentmode = Label(root, text="Payment Mode")

# setting variables in place
name.grid(row=21, column=0)
phone.grid(row=22, column=0)
address.grid(row=23, column=0)
gender.grid(row=24, column=0)
paymentmode.grid(row=25, column=0)


# variable classes for all variables
namevalue = StringVar()
phonevalue =StringVar()
addressvalue = StringVar()
gendervalue = StringVar()
paymentmodevalue = StringVar()
# making a checkbox
foodservicevalue = IntVar()


# entry space variables for all variables

name_entry = Entry(root, textvariable=namevalue)

phone_entry = Entry(root, textvariable=phonevalue)

gender_entry = Entry(root, textvariable=gendervalue)

address_entry = Entry(root, textvariable=addressvalue)

paymentmode_entry = Entry(root, textvariable=paymentmodevalue)

#  making entry spaces of variables

name_entry.grid(row=21,column=1)
phone_entry.grid(row=22,column=1)
gender_entry.grid(row=23,column=1)
address_entry.grid(row=24,column=1)
paymentmode_entry.grid(row=25,column=1)

# checkbox for food

foodservice = Checkbutton(text="include food with the booking?", variable = foodservicevalue)

foodservice.grid(row=26, column=1, pady=10)

# creating buttons and assigning it a command

submit_button = Button(text="SUBMIT", command=submit)

submit_button.grid(row=30, column=1)







root.mainloop()

