#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 14, 2021 03:03:54 PM +04  platform: Darwin

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

import pagefour_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = PageFour (root)
    pagefour_support.init(root, top)
    root.mainloop()

w = None
def create_PageFour(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_PageFour(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = PageFour (w)
    pagefour_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PageFour():
    global w
    w.destroy()
    w = None

class PageFour:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("980x500+203+145")
        top.minsize(72, 15)
        top.maxsize(1440, 766)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#09573f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.224, rely=0.28, height=94, width=554)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#09573f")
        self.Label1.configure(font="-family {Kohinoor Devanagari} -size 42 -weight bold")
        self.Label1.configure(foreground="#ad6505")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Thanks for your Purchase''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.347, rely=0.5, height=52, width=149)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(relief="raised")
        self.Button1.configure(text='''New Order''')

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.52, rely=0.5, height=52, width=149)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(relief="raised")
        self.Button1_1.configure(text='''Exit''')

if __name__ == '__main__':
    vp_start_gui()





