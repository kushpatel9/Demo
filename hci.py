from tkinter import *
parent = Tk()
parent.geometry("500x200")
name = Button(parent,text = "Name",bg='pink').grid(row = 0, column =
0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Button(parent,text = "Password",bg='pink').grid(row = 1,
column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent, text = "Submit",bg='blue',
fg='white',activebackground='pink').grid( row = 5, column = 1)
parent.mainloop()
