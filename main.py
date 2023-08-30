from tkinter import *

window = Tk()

titleLabel = Label(window,text='Enter your info',font=("Arial",30)).grid()

firstNameLabel = Label(window,text="Enter name: ",width=20,bg='red').grid(row=0,column=0)
firstNameEntry = Entry(window).grid(row=0,column=1)

lastNameLabel = Label(window,text="last name: ",bg='green').grid(row=1,column=0)
lastNameEntry = Entry(window).grid(row=1,column=1)

emailLabel = Label(window,text="email: ",bg='blue',width=30).grid(row=2,column=0)
emailEntry = Entry(window).grid(row=2,column=1)

submitButton = Button(window,text="Submit").grid(row=3,column=0,columnspan=2)

window.mainloop()