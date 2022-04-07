#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 30, 2021 10:07:55 AM +04  platform: Darwin

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        self.aviable_cars = ['Opel', 'Kia']
        self.rent_list = {
            "Tayota": "Fagan"
        }



        top.geometry("880x450+308+228")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#fff")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.023, rely=0.022, relheight=0.9, relwidth=0.47)
        self.Canvas1.configure(background="#fff")
        self.Canvas1.configure(highlightthickness=4, highlightbackground="black")

        self.Canvas1_2 = tk.Canvas(top)
        self.Canvas1_2.place(relx=0.477, rely=0.022, relheight=0.9, relwidth=0.473)
        self.Canvas1_2.configure(background="#fff")
        self.Canvas1_2.configure(highlightthickness=4, highlightbackground="black")

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.002, rely=0, height=32, width=149)
        self.Button1.configure(activebackground="#fff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#fff")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#fff")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightthickness=3, highlightbackground="black")
        self.Button1.configure(text='''User Tab''')

        self.Button1_1 = tk.Button(self.Canvas1)
        self.Button1_1.place(relx=0.355, rely=0.000, height=32, width=149)
        self.Button1_1.configure(activebackground="#fff")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#fff")
        self.Button1_1.configure(disabledforeground="#fff")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightthickness=3, highlightbackground="black")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(text='''Admin Tab''')

        self.Label1_1 = tk.Label(self.Canvas1)
        self.Label1_1.place(relx=0.024, rely=0.37, height=24, width=83)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#fff")
        self.Label1_1.configure(cursor="fleur")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Name''')

        self.Label1_2 = tk.Label(self.Canvas1)
        self.Label1_2.place(relx=0.048, rely=0.617, height=24, width=83)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#fff")
        self.Label1_2.configure(cursor="fleur")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Car name''')

        self.Entry1 = tk.Entry(self.Canvas1)
        self.Entry1.place(relx=0.072, rely=0.42, height=30, relwidth=0.585)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(highlightthickness=3, highlightbackground="black")
        self.Entry1.configure(selectforeground="white")

        self.Entry1_1 = tk.Entry(self.Canvas1)
        self.Entry1_1.place(relx=0.072, rely=0.667, height=30, relwidth=0.585)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(highlightthickness=3, highlightbackground="black")
        self.Entry1_1.configure(selectforeground="white")

        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(relx=0.121, rely=0.79, height=42, width=199)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightthickness=3, highlightbackground="black", command=self.rent_car)
        self.Button2.configure(text='''Rent''')

        self.Label1_3 = tk.Text(self.Canvas1)
        self.Label1_3.place(relx=0.07, rely=0.148, height=30, width=300)
        self.set_aviable_cars_left()



        self.Label1_3_1 = tk.Text(self.Canvas1_2)
        self.Label1_3_1.place(relx=0.048, rely=0.05, height=60, width=350)
        self.set_aviable_cars_right()

        self.Label1_3_2 = tk.Text(self.Canvas1_2)
        self.Label1_3_2.place(relx=0.048, rely=0.222, height=60, width=350)
        self.set_rented_cars()



        self.Label1_1_1 = tk.Label(self.Canvas1_2)
        self.Label1_1_1.place(relx=0.048, rely=0.37, height=24, width=83)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(background="#fff")
        self.Label1_1_1.configure(foreground="#000000")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Car name''')

        self.Entry1_1_1 = tk.Entry(self.Canvas1_2)
        self.Entry1_1_1.place(relx=0.096, rely=0.42, height=30, relwidth=0.582)
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(foreground="#000000")
        self.Entry1_1_1.configure(highlightcolor="black")
        self.Entry1_1_1.configure(insertbackground="black")
        self.Entry1_1_1.configure(selectforeground="white")
        self.Entry1_1_1.configure(highlightthickness=3, highlightbackground="black")

        self.Button2_1 = tk.Button(self.Canvas1_2)
        self.Button2_1.place(relx=0.168, rely=0.543, height=42, width=199)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#d9d9d9")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightthickness=3, highlightbackground="black")
        self.Button2_1.configure(text='''Return car''', command=self.return_car)


    def rent_car(self):
        name = self.Entry1.get()
        car_name = self.Entry1_1.get()

        if name and car_name:
            if car_name in self.aviable_cars:
                self.rent_list[car_name] = name
                self.aviable_cars.remove(car_name)
                self.set_aviable_cars_left()
                self.set_rented_cars()
                self.set_aviable_cars_right()
            else:
                print("No such aviable car")
        else:
            print("Entry values empty")

    def return_car(self):
        str = self.Entry1_1_1.get()
        if str:
            if self.rent_list.get(str):
                self.rent_list.pop(str)
                print(self.rent_list)
                self.aviable_cars.append(str)
                self.set_aviable_cars_right()
                self.set_aviable_cars_left()
                self.set_rented_cars()
            else:
                print("No such renter Car")
        else:
            print("Entry is empty")

    def set_aviable_cars_right(self):
        self.Label1_3_1.configure(state='normal')
        str_list = f"Aviable cars: {', '.join(self.aviable_cars)}\t(list)"
        self.Label1_3_1.delete("1.0", "end")
        self.Label1_3_1.insert(tk.END, str_list)
        self.Label1_3_1.configure(state='disabled')

    def set_aviable_cars_left(self):
        self.Label1_3.configure(state='normal')
        str_list = f"{', '.join(self.aviable_cars)}\t(list)"

        self.Label1_3.delete("1.0", "end")
        self.Label1_3.insert(tk.END, str_list)
        self.Label1_3.configure(state='disabled')

    def set_rented_cars(self):
        self.Label1_3_2.configure(state='normal')
        str_list = f"Renter cars: "
        for key, value in self.rent_list.items():
            str_list += f"{key} - {value}, "
        str_list = str_list[0:len(str_list)-2]
        str_list += "\t(dictionary)"
        self.Label1_3_2.delete("1.0", "end")
        self.Label1_3_2.insert(tk.END, str_list)
        self.Label1_3_2.configure(state='disabled')


if __name__ == '__main__':
    vp_start_gui()




