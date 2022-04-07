#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 14, 2021 01:32:19 PM +04  platform: Darwin

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

import pagethree_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = PageThree (root)
    pagethree_support.init(root, top)
    root.mainloop()

w = None
def create_PageThree(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_PageThree(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = PageThree (w)
    pagethree_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PageThree():
    global w
    w.destroy()
    w = None

class PageThree:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x450+287+143")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#09573f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.018, height=63, width=670)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {American Typewriter} -size 44 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Personal Information''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.538, rely=0.222, relheight=0.669, relwidth=0.411)

        self.Text1.configure(background="#ccc")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.05, rely=0.2, height=34, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#09573f")
        self.Label2.configure(font="-family {Avenir Next Condensed} -size 16 -weight bold")
        self.Label2.configure(foreground="#ad6505")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Card Number''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.051, rely=0.267, height=35, relwidth=0.378)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
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

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.25, rely=0.444, height=35, relwidth=0.178)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(relx=0.051, rely=0.444, height=35, relwidth=0.178)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")

        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(relx=0.051, rely=0.622, height=35, relwidth=0.178)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="blue")
        self.Entry1_3.configure(selectforeground="white")

        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(relx=0.25, rely=0.622, height=35, relwidth=0.178)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="blue")
        self.Entry1_4.configure(selectforeground="white")

        self.Entry1_5 = tk.Entry(top)
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
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''Pay 30$''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.163, rely=0.222, height=14, width=136)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#09573f")
        self.Label2_5.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.Label2_5.configure(foreground="#f00")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Wrong Card Number''')

        self.Label2_5_1 = tk.Label(top)
        self.Label2_5_1.place(relx=0.138, rely=0.4, height=14, width=136)
        self.Label2_5_1.configure(activebackground="#f9f9f9")
        self.Label2_5_1.configure(activeforeground="black")
        self.Label2_5_1.configure(background="#09573f")
        self.Label2_5_1.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.Label2_5_1.configure(foreground="#f00")
        self.Label2_5_1.configure(highlightbackground="#d9d9d9")
        self.Label2_5_1.configure(highlightcolor="black")
        self.Label2_5_1.configure(text='''Wrong Expiry date''')

        self.Label2_5_2 = tk.Label(top)
        self.Label2_5_2.place(relx=0.1, rely=0.578, height=14, width=76)
        self.Label2_5_2.configure(activebackground="#f9f9f9")
        self.Label2_5_2.configure(activeforeground="black")
        self.Label2_5_2.configure(background="#09573f")
        self.Label2_5_2.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.Label2_5_2.configure(foreground="#f00")
        self.Label2_5_2.configure(highlightbackground="#d9d9d9")
        self.Label2_5_2.configure(highlightcolor="black")
        self.Label2_5_2.configure(text='''Wrong CVC''')

        self.Label2_5_3 = tk.Label(top)
        self.Label2_5_3.place(relx=0.338, rely=0.578, height=14, width=96)
        self.Label2_5_3.configure(activebackground="#f9f9f9")
        self.Label2_5_3.configure(activeforeground="black")
        self.Label2_5_3.configure(background="#09573f")
        self.Label2_5_3.configure(font="-family {Avenir Next Condensed} -size 13 -weight bold")
        self.Label2_5_3.configure(foreground="#f00")
        self.Label2_5_3.configure(highlightbackground="#d9d9d9")
        self.Label2_5_3.configure(highlightcolor="black")
        self.Label2_5_3.configure(text='''Wrong Zip Code''')

if __name__ == '__main__':
    vp_start_gui()





