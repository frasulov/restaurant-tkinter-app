import tkinter as tk
import datetime

class PageOne:
    def __init__(self, top=None):

        top.geometry("980x500+137+113")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("Restaurant Management")
        top.configure(borderwidth="2")
        top.configure(background="#09573f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.204, rely=0.14, height=114, width=638)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {Muna} -size 40 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Restaurant Management System''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.255, rely=0.44, height=34, width=128)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#09573f")
        self.Label2.configure(font="-family {Baghdad} -size 24")
        self.Label2.configure(foreground="#ad6505")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Full name''')


        self.fullname_var = tk.StringVar()
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.388, rely=0.43, height=35, relwidth=0.308)
        self.Entry1.configure(background="#ccc", textvariable=self.fullname_var)
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#000")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="#000")
        self.Entry1.configure(selectbackground="#fff")
        self.Entry1.configure(selectforeground="white")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.439, rely=0.6, height=52, width=189)
        self.Button1.configure(background="#a80000", foreground="#000",text='''Next''',command=lambda : self.next_page(PageTwo, top))
        self.Button1.bind("<Enter>", lambda e: self.Button1.config(fg='#ad6505', bg='#00f', highlightbackground="#fff"))
        self.Button1.bind("<Leave>", lambda e: self.Button1.config(fg='#000', bg='#0f0', highlightbackground="#a80000"))
        self.Button1.configure(font="-family {American Typewriter} -size 24 -weight bold")
        self.Button1.configure(highlightbackground="#a80000")
        self.Button1.configure(highlightcolor="black")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.184, rely=0.06, height=64, width=638)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#09573f")
        self.Label1_1.configure(font="-family {Muna} -size 40 -weight bold")
        self.Label1_1.configure(foreground="#ad6505")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Welcome to''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.388, rely=0.52, height=24, width=296)
        self.Label3.configure(background="#09573f")
        self.Label3.configure(font="-family {Apple SD Gothic Neo} -size 16 -weight bold")
        self.Label3.configure(foreground="#f00")
        self.Label3.configure(text='''''')


    def next_page(self, page, root):
        self.name=self.fullname_var.get()
        if not self.Entry1.get():
            self.Label3.configure(text='''Please, Enter full name!''')
            return
        root.destroy()
        root = tk.Tk()
        top = page(self.fullname_var.get(),root)

class PageTwo:
    def __init__(self, fullname, top=None):
        self.fullname=fullname
        top.geometry("980x500+146+113")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("Restaurant Management")
        top.configure(borderwidth="2")
        top.configure(background="#09573f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.184, rely=-0.04, height=114, width=638)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {Muna} -size 40 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Restaurant Management System''')

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.031, rely=0.14, relheight=0.81, relwidth=0.945)

        self.Canvas1.configure(background="#15ab7d")
        self.Canvas1.configure(borderwidth="10")
        self.Canvas1.configure(closeenough="0.0")
        self.Canvas1.configure(cursor="fleur")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(insertborderwidth="2")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white", highlightthickness=0)


        self.Button1_1 = tk.Button(self.Canvas1)
        self.Button1_1.place(relx=0.694, rely=0.6, height=52, width=189)
        self.Button1_1.configure(activebackground="#a80000")
        self.Button1_1.configure(activeforeground="white")
        self.Button1_1.configure(activeforeground="#a80000")
        self.Button1_1.configure(background="#a80000")
        self.Button1_1.configure(disabledforeground="#a80000")
        self.Button1_1.configure(font="-family {American Typewriter} -size 24 -weight bold")
        self.Button1_1.configure(foreground="#a80000")
        self.Button1_1.configure(highlightbackground="#a80000")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(relief="raised")
        self.Button1_1.configure(text='''Payment Info''',
                                 command=lambda : self.next_page(PageThree, top))


        self.price_list = {}
        self.reciept = {}
        self.datas = {}

        self.read_ui_from_file()
        self.read_headers_from_file(top)



        for id, data in self.datas.items():
            # check button
            self.price_list[id] = data["price"]
            setattr(self, f"second-entry-{id}", tk.Entry(self.Canvas1))
            getattr(self, f"second-entry-{id}").place(relx=float(data["e2-relx"]), rely=float(data["e2-rely"]), height=float(data["e2-height"]), width=float(data["e2-width"]))
            getattr(self, f"second-entry-{id}").configure(background="#fff")
            getattr(self, f"second-entry-{id}").configure(cursor="fleur")
            getattr(self, f"second-entry-{id}").configure(font="TkFixedFont")
            getattr(self, f"second-entry-{id}").configure(foreground="#000000")
            getattr(self, f"second-entry-{id}").configure(highlightbackground="#d9d9d9")
            getattr(self, f"second-entry-{id}").configure(highlightcolor="black")
            getattr(self, f"second-entry-{id}").configure(insertbackground="black")
            vcmd = (getattr(self, f"second-entry-{id}").register(self.callback))
            getattr(self, f"second-entry-{id}").configure(selectforeground="white", validate='all', validatecommand=(vcmd, '%P'))
            getattr(self, f"second-entry-{id}").configure(selectbackground="blue", state='disabled')
            var2 = tk.StringVar()
            var2.set(data["price"])
            getattr(self, f"second-entry-{id}").configure(textvariable = var2)


            setattr(self, f"entry-{id}", tk.Entry(self.Canvas1))
            getattr(self, f"entry-{id}").place(relx=float(data["e1-relx"]), rely=float(data["e1-rely"]), height=float(data["e1-height"]), width=float(data["e1-width"]))
            vcmd = (getattr(self, f"entry-{id}").register(self.callback))
            getattr(self, f"entry-{id}").configure(
                background="#fff",
                cursor="fleur",
                font="TkFixedFont",
                foreground="#000",
                highlightbackground="#d9d9d9",
                highlightcolor="black",
                selectbackground="blue",
                validate='all',
                validatecommand=(vcmd, '%P'),
                insertbackground="black",
                state='disabled',
            )
            var = tk.StringVar()
            var.set(0)
            var.trace("w", lambda name, index, mode, var=var, var2=var2, id=id: self.get_value_callback(var, var2, id))
            getattr(self, f"entry-{id}").configure(textvariable=var)

            setattr(self, f"checkbutton-{id}", tk.Checkbutton(self.Canvas1, command=lambda id=id: self.toggleDisabled(id)))
            getattr(self, f"checkbutton-{id}").place(relx=float(data["cb-relx"]), rely=float(data["cb-rely"]), height=float(data["cb-height"]), width=float(data["cb-width"]))
            getattr(self, f"checkbutton-{id}").configure(activebackground="#15ab7d")
            getattr(self, f"checkbutton-{id}").configure(activeforeground="white")
            getattr(self, f"checkbutton-{id}").configure(activeforeground="#000000")
            getattr(self, f"checkbutton-{id}").configure(background="#15ab7d")
            getattr(self, f"checkbutton-{id}").configure(font="-family {Arial Black} -size 16 -weight bold")
            getattr(self, f"checkbutton-{id}").configure(foreground="#000000")
            getattr(self, f"checkbutton-{id}").configure(highlightbackground="#d9d9d9")
            getattr(self, f"checkbutton-{id}").configure(highlightcolor="black")
            getattr(self, f"checkbutton-{id}").configure(justify='left')
            getattr(self, f"checkbutton-{id}").configure(text=data["text"])

    def next_page(self, page, root):
        root.destroy()
        root = tk.Tk()
        top = page({"reciept": self.reciept,
                    "data": self.datas,
                    "fullname": self.fullname}, root)

    def read_headers_from_file(self, top):
        file1 = open('headers.txt', 'r')
        lines = file1.readlines()


        for line in lines:
            data = line.split(";")
            setattr(self, f"label-{data[0]}",tk.Label(top))
            getattr(self, f"label-{data[0]}").place(
                relx = float(data[1]),
                rely = float(data[2]),
                height = float(data[3]),
                width = float(data[4]),
            )

            getattr(self, f"label-{data[0]}").configure(
                text = data[5],
                activebackground="#f9f9f9",
                activeforeground="black",
                background="#15ab7d",
                font="-family {Muna} -size 24 -weight bold",
                foreground="#ad6505",
                highlightbackground="#d9d9d9",
                highlightcolor="black",
            )

    def read_ui_from_file(self):
        file1 = open('pages.txt', 'r')

        lines = file1.readlines()
        for line in lines:
            data = line.split(";")
            self.datas[data[0]] = {
                "id": data[0],

                "cb-relx":float(data[1]),
                "cb-rely":float(data[2]),
                "cb-height": float(data[3]),
                "cb-width": float(data[4]),

                "text": data[5],

                "e1-relx":float(data[6]),
                "e1-rely":float(data[7]),
                "e1-height": float(data[8]),
                "e1-width": float(data[9]),

                "e2-relx":float(data[10]),
                "e2-rely":float(data[11]),
                "e2-height": float(data[12]),
                "e2-width": float(data[13]),
                "price":float(data[14])
            }

    def get_value_callback(self, var, var2, id):
        price = float(self.price_list.get(id))


        if var.get():
            if var.get()[0] == '0':
                var.set(var.get()[1:])
        else:
            var.set(0)

        if var.get() == '0':
            var2.set(price)
            if self.reciept.get(id):
                self.reciept.pop(id)
        else:
            var2.set(round(price*int(var.get()),2))
            self.reciept[id] = int(var.get())

    def toggleDisabled(self, id):
        entry = getattr(self, f"entry-{id}")
        if entry['state'] == 'disabled':
            entry.configure(state='normal')
        else:
            if self.reciept.get(id):
                self.reciept.pop(id)
            entry.configure(state='disabled')


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

class PageThree:


    def __init__(self, data_info, top=None):

        top.geometry("800x450+287+143")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#09573f")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.018, height=63, width=670)
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {American Typewriter} -size 44 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(text='''Personal Information''')


        self.reciept = data_info["reciept"]
        self.data = data_info["data"]
        self.fullname = data_info["fullname"]
        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.51, rely=0.222, relheight=0.669, relwidth=0.47) #0.411

        self.Text1.configure(background="#ccc")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.sum = 0
        self.display_text()


        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.051, rely=0.2, height=34, width=84)
        self.Label2.configure(background="#09573f")
        self.Label2.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2.configure(foreground="#ad6505")
        self.Label2.configure(text='''Card Number''')

        self.card_number = tk.StringVar()
        self.Entry1 = tk.Entry(top, textvariable=self.card_number)
        vcmd = (self.Entry1).register(self.callback)
        self.Entry1.configure(validate='all', validatecommand=(vcmd, '%P'))
        self.Entry1.place(relx=0.051, rely=0.267, height=35, relwidth=0.378)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectforeground="white")

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.041, rely=0.378, height=34, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#09573f")
        self.Label2_1.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2_1.configure(foreground="#ad6505")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Expiry date''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.02, rely=0.556, height=34, width=84)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#09573f")
        self.Label2_2.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2_2.configure(foreground="#ad6505")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''CVC''')

        self.Label2_3 = tk.Label(top)
        self.Label2_3.place(relx=0.238, rely=0.556, height=34, width=84)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#09573f")
        self.Label2_3.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2_3.configure(foreground="#ad6505")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Zip code''')

        self.Label2_4 = tk.Label(top)
        self.Label2_4.place(relx=0.02, rely=0.733, height=34, width=84)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#09573f")
        self.Label2_4.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2_4.configure(foreground="#ad6505")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''Tip''')

        self.expiry_date_year = tk.StringVar()
        self.Entry1_1 = tk.Entry(top, textvariable=self.expiry_date_year)
        vcmd = (self.Entry1_1).register(self.callback)
        self.Entry1_1.configure(validate='all', validatecommand=(vcmd, '%P'))
        self.Entry1_1.place(relx=0.25, rely=0.444, height=35, relwidth=0.178)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.expiry_date_month = tk.StringVar()
        self.Entry1_2 = tk.Entry(top, textvariable=self.expiry_date_month)
        vcmd = (self.Entry1_2).register(self.callback)
        self.Entry1_2.configure(validate='all', validatecommand=(vcmd, '%P'))
        self.Entry1_2.place(relx=0.051, rely=0.444, height=35, relwidth=0.178)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.cvc = tk.StringVar()
        self.Entry1_3 = tk.Entry(top, textvariable=self.cvc)
        vcmd = (self.Entry1_3).register(self.callback)
        self.Entry1_3.configure(validate='all', validatecommand=(vcmd, '%P'))
        self.Entry1_3.place(relx=0.051, rely=0.622, height=35, relwidth=0.178)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="blue")
        self.Entry1_3.configure(selectforeground="white")

        self.zip_code = tk.StringVar()
        self.Entry1_4 = tk.Entry(top, textvariable=self.zip_code)
        self.Entry1_4.place(relx=0.25, rely=0.622, height=35, relwidth=0.178)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="blue")
        self.Entry1_4.configure(selectforeground="white")

        self.tip = tk.StringVar()

        self.tip.trace("w", lambda name, index, mode: self.get_tip_callback())
        self.Entry1_5 = tk.Entry(top, textvariable=self.tip)
        vcmd = (self.Entry1_5).register(self.callback)
        self.Entry1_5.configure(validate='all', validatecommand=(vcmd, '%P'))
        self.Entry1_5.place(relx=0.051, rely=0.8, height=35, relwidth=0.165)
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(font="TkFixedFont")
        self.Entry1_5.configure(foreground="#000000")
        self.Entry1_5.configure(highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black")
        self.Entry1_5.configure(insertbackground="black")
        self.Entry1_5.configure(selectbackground="blue")
        self.Entry1_5.configure(selectforeground="white")

        self.Button1 = tk.Button(top)


        self.Button1.place(relx=0.25, rely=0.8, height=32, width=139)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a80000")
        self.Button1.configure(disabledforeground="#a80000")
        self.Button1.configure(font="-family {American Typewriter} -size 16 -weight bold")
        self.Button1.configure(foreground="#a80000")
        self.Button1.configure(highlightbackground="#a80000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text=f"Pay {self.sum}$", command=lambda : self.next_page(PageFour, top))

        self.label_card_number = tk.Label(top)
        self.label_card_number.place(relx=0.163, rely=0.222, height=14, width=136)
        self.label_card_number.configure(activebackground="#f9f9f9")
        self.label_card_number.configure(activeforeground="black")
        self.label_card_number.configure(background="#09573f")
        self.label_card_number.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.label_card_number.configure(foreground="#f00")
        self.label_card_number.configure(highlightbackground="#d9d9d9")
        self.label_card_number.configure(highlightcolor="black")
        self.label_card_number.configure(text='''''')

        self.label_expiry_date = tk.Label(top)
        self.label_expiry_date.place(relx=0.138, rely=0.4, height=14, width=136)
        self.label_expiry_date.configure(activebackground="#f9f9f9")
        self.label_expiry_date.configure(activeforeground="black")
        self.label_expiry_date.configure(background="#09573f")
        self.label_expiry_date.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.label_expiry_date.configure(foreground="#f00")
        self.label_expiry_date.configure(highlightbackground="#d9d9d9")
        self.label_expiry_date.configure(highlightcolor="black")
        self.label_expiry_date.configure(text='''''')

        self.label_cvc = tk.Label(top)
        self.label_cvc.place(relx=0.1, rely=0.578, height=14, width=76)
        self.label_cvc.configure(activebackground="#f9f9f9")
        self.label_cvc.configure(activeforeground="black")
        self.label_cvc.configure(background="#09573f")
        self.label_cvc.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.label_cvc.configure(foreground="#f00")
        self.label_cvc.configure(highlightbackground="#d9d9d9")
        self.label_cvc.configure(highlightcolor="black")
        self.label_cvc.configure(text='''''')

        self.label_zip_code = tk.Label(top)
        self.label_zip_code.place(relx=0.338, rely=0.578, height=14, width=96)
        self.label_zip_code.configure(activebackground="#f9f9f9")
        self.label_zip_code.configure(activeforeground="black")
        self.label_zip_code.configure(background="#09573f")
        self.label_zip_code.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.label_zip_code.configure(foreground="#f00")
        self.label_zip_code.configure(highlightbackground="#d9d9d9")
        self.label_zip_code.configure(highlightcolor="black")
        self.label_zip_code.configure(text='''''')

    def get_tip_callback(self):
        if self.tip.get():
            self.display_text(float(self.tip.get()))
            self.Button1.configure(text=f"Pay {self.sum}$")
        elif self.tip.get() == "":
            self.display_text()
            self.Button1.configure(text=f"Pay {self.sum}$")
        print(self.tip.get())

    def next_page(self, page, root):
        count = 0
        if not self.card_number.get():
            self.label_card_number.configure(text='''Wrong Card Number''')
            count += 1
        else:
            if len(self.card_number.get()) != 16:
                self.label_card_number.configure(text='''Card needs 16 number''')
                count += 1
            else:
             self.label_card_number.configure(text='''''')

        if not self.expiry_date_month.get() or not self.expiry_date_year.get():
            self.label_expiry_date.configure(text='''Wrong Expery date''')
            count +=1
        else:
            if int(self.expiry_date_month.get()) <1 and int(self.expiry_date_month.get()) > 12:
                self.label_expiry_date.configure(text='''Wrong Expery date''')
                count +=1
            else:
                self.label_expiry_date.configure(text='''''')

        if not self.cvc.get():
            self.label_cvc.configure(text='''Wrong CVC''')
            count += 1
        else:
            self.label_cvc.configure(text='''''')

        if not self.zip_code.get():
            self.label_zip_code.configure(text='''Wrong Zip Code''')
            count += 1
        else:
            self.label_zip_code.configure(text='''''')



        if count:
            return
        root.destroy()
        root = tk.Tk()
        top = page(root)


    def display_text(self, tip=None):
        self.sum = 0
        self.Text1.configure(state='normal')
        text_display = f"Recipient name\t\t\t{self.fullname}\n\n"
        text_display += "Item\t\tPrice\tNo of Items\t    Total\n"
        for key, value in self.reciept.items():
            item = self.data.get(key)
            price = float(item["price"])
            self.sum += price*int(value)
            text_display += item["text"] + "\t\t"+str(price)+"\t"+str(value)+"\t     "+str(round(price*value,2))+"$\n"

        if tip:
            text_display += "Tip\t\t\t\t     " + str(tip) + "$"
            self.sum += float(tip)

        self.sum = round(self.sum, 2)
        text_display += "\nTotal\t\t\t\t     " + str(self.sum) + "$\n"
        today = datetime.datetime.now()
        text_display += "\nToday's Date:\t\t" + today.strftime("%B %d, %Y %H:%M:%S")

        self.Text1.delete("1.0", "end")
        self.Text1.insert(tk.END, text_display)
        self.Text1.configure(state='disabled')

    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

class PageFour:
    def __init__(self, top=None):

        top.geometry("980x500+203+145")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#09573f")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.224, rely=0.28, height=94, width=554)
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {Kohinoor Devanagari} -size 42 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(text='''Thanks for your Purchase''')


        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.347, rely=0.5, height=52, width=149)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a80000")
        self.Button1.configure(disabledforeground="#a80000")
        self.Button1.configure(font="-family {American Typewriter} -size 16 -weight bold")
        self.Button1.configure(foreground="#a80000")
        self.Button1.configure(highlightbackground="#a80000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''New Order''', command=lambda : self.next_page(PageOne, top))

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.52, rely=0.5, height=52, width=149)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#a80000")
        self.Button1_1.configure(disabledforeground="#a80000")
        self.Button1_1.configure(font="-family {American Typewriter} -size 16 -weight bold")
        self.Button1_1.configure(foreground="#a80000")
        self.Button1_1.configure(highlightbackground="#a80000")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(relief="raised")
        self.Button1_1.configure(text='''Exit''', command=lambda root=top: self.destroy(root))


    def destroy(self, root):
        root.destroy()


    def next_page(self, page, root):
        root.destroy()
        root = tk.Tk()
        top = page(root)
