import tkinter as tk
import pages


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = pages.PageOne (root)
    root.mainloop()

w = None
def create_PageOne(rt):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = pages.PageOne (w)
    return (w, top)


if __name__ == '__main__':
    vp_start_gui()
