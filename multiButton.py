#!/usr/bin/env python3
'''
'''
from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def chtheme(*args):
    c = style.theme_names()*2
    style.theme_use(c[c.index(style.theme_use())+1])
    curstyle.set(style.theme_use())

root = Tk()
root.title("Feet to Meters")
style = ttk.Style()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
feet = StringVar()
meters = StringVar()
curstyle = StringVar()
curstyle.set(style.theme_use())
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, textvariable=curstyle, command=chtheme).grid(column=1, row=1, sticky = (N, W))
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
