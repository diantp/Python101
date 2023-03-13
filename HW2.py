from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('Information')
GUI.geometry('400x250')
name_var = StringVar()
surname_var = StringVar()
age_var = StringVar()

L1 = Label(GUI, text='your information :', font=('Bloomer DEMO', 20), fg='#151B54')
#############################



#############################
    
nameLabel = Label(GUI, text="Name :")
nameBox = Entry(GUI, textvariable = name_var)

surnameLabel = Label(GUI, text="Surname :")
surnameBox = Entry(GUI, textvariable = surname_var)

ageLabel = Label(GUI, text="Age :")
ageBox = Entry(GUI, textvariable = age_var)

L1.grid(row=0,column=0)
nameLabel.grid(row=1, column=0)
nameBox.grid(row=1, column=1)
surnameLabel.grid(row=2, column=0)
surnameBox.grid(row=2, column=1)
ageLabel.grid(row=3, column=0)
ageBox.grid(row=3, column=1)
#############################

def submit():
    name = name_var.get()
    surname = surname_var.get()
    age = age_var.get()
    
    print("Your name is : " + name + ' ' + surname)
    print("Age : " + age)
    
    name_var.set("")
    surname_var.set("")
    age_var.set("")
    
submitBut = ttk.Button(GUI, text='Submit', command = submit)
submitBut.grid(row=4, column=1)
#############################

GUI.mainloop()
