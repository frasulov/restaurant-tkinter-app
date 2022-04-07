from tkinter import *
labels = False

def save_info():
    name_info = name.get()
    surname_info = surname.get()
    phone_info = phone.get()
    email_info = email.get()
    print(name_info, surname_info, phone_info, email_info)
    global labels
    labels = True
    createLabels(name_info, surname_info, phone_info, email_info)
    name.set("")
    surname.set("")
    phone.set("")
    email.set("")

def delete_info():
    global labels
    labels = False
    createLabels()





def createLabels(name=None, surname=None, phone=None, email=None):
    global name_text
    global surname_text
    global phone_text
    global email_text
    global labels
    if not labels:
        name_text.configure(text=f"name: ")
        surname_text.configure(text=f"surname: ")
        phone_text.configure(text=f"phone: ")
        email_text.configure(text=f"email: ")
    else:
        name_text.configure(text=f"name: {name}")
        surname_text.configure(text=f"surname: {surname}")
        phone_text.configure(text=f"phone: {phone}")
        email_text.configure(text=f"email: {email}")

    name_text.place(x=15, y=450)
    surname_text.place(x=15, y=480)
    phone_text.place(x=15, y=510)
    email_text.place(x=15, y=540)


    labels = True



window = Tk()
window.title('Personal informtion')
window.geometry('600x600')

label = Label(text='Personal information', bg='grey', fg='black')
label.pack()

name_text = Label(text='name', bg='grey', fg='black')
surname_text = Label(text='surname', bg='grey', fg='black')
phone_text = Label(text='phone', bg='grey', fg='black')
email_text = Label(text='email', bg='grey', fg='black')
name_text.place(x=15, y=70)
surname_text.place(x=15, y=140)
phone_text.place(x=15, y=210)
email_text.place(x=15, y=280)

name = StringVar()
surname = StringVar()
phone = StringVar()
phone.set("")
email = StringVar()

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
phone_entry = Entry(textvariable=phone)
email_entry = Entry(textvariable=email)

name_entry.place(x=15, y=100)
surname_entry.place(x=15, y=170)
phone_entry.place(x=15, y=240)
email_entry.place(x=15, y=310)

save = Button(text='save', command=save_info, bg='grey', fg='black', width='30', height='2')
save.place(x=15, y=360)


delete = Button(text='delete', command=delete_info, bg='grey', fg='black', width='30', height='2')
delete.place(x=15, y=410)


name_text = Label(text='name: ', bg='grey', fg='black')
surname_text = Label(text='surname: ', bg='grey', fg='black')
phone_text = Label(text='phone: ', bg='grey', fg='black')
email_text = Label(text='email: ', bg='grey', fg='black')


window.mainloop()