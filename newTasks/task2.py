from tkinter import *
from tkinter.ttk import *
from datetime import datetime

adult_list = []
children_list = []
months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
             'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
#######################CLASS
class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        res = 'Name - ' + str(self.get_name()) + 'Surname - ' + str(self.get_surname()) + 'Age - ' + str(self.get_age())
        return res

    #Getters
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_age(self):
        return self.__age
    # setters
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
    def set_surname(self, surname):
        if surname.isalpha():
            self.__surname = surname
    def set_age(self, age):
        self.__age = age






########################################

def save():
    month = 1
    if months.get(combobox_month.get()):
        month = months.get(combobox_month.get())
    date_time_obj = datetime(int(spinbox_year.get()), month, int(spinbox_day.get()))
    today = datetime.today()
    difference = today-date_time_obj
    age_days = int(difference.days/365)

    p1 = Person(entry_name.get(), entry_surname.get(), age_days)

    if p1.get_age() < 18:
        children_list.append(p1)
    else:
        adult_list.append(p1)

    # print all
    print("Children list: ", [str(p) for p in children_list])
    print("Adult list: ", [str(p) for p in adult_list], end="\n\n")


window = Tk()
window.title('TKinter program')
window.geometry('400x300')

#Name
label_name = Label(text='Name: ')
label_name.grid(column = 0, row=0, padx=10, pady=10)
entry_name = Entry()
entry_name.grid(column = 1, row=0, padx=10, pady=10)

#Surname
label_surname = Label(text='Surame: ')
label_surname.grid(column = 0, row=1, padx=10, pady=10)
entry_surname = Entry()
entry_surname.grid(column = 1, row=1, padx=10, pady=10)

#Date
spinbox_day= Spinbox(window, from_=1, to= 31, width=3)
spinbox_day.grid(column = 0, row=2)

combobox_month = Combobox(window, width=10)
combobox_month['values']=('January', 'February', 'March','April', 'May', 'June','July','August','September','October','November','December')
combobox_month.grid(column = 1, row=2)
combobox_month.current(0)

spinbox_year= Spinbox(window, from_=1900, to= 2020, width=5)
spinbox_year.grid(column = 3, row=2)


btn = Button(text= 'SAVE', command = save)
btn.grid(column = 1, row=3, padx=10, pady=10)



window.mainloop()