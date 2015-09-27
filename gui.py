#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from tkMessageBox import askokcancel 
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from Tkinter import Tk
from tkFileDialog import *
from main import main_route
from plot import plotter
from PIL import Image

def start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, photo
    root = Tk()
    root.title('Bolztrap Plotter')
    geom = "603x452+509+260"
    root.geometry(geom)
    photo=PhotoImage(file='/home/bumble/Desktop/Chemical_Potential_Plot/logo-1.png')
    w = New_Toplevel_1 (root)
    root.mainloop()

def ext_cmd():
    main_route.extract(file_path,temp.get())

def plt():
    global temp,r,u
    plotter.plotting(r.get(),u.get(),temp.get(),file_path)

def quit():
    global root
    ans = askokcancel('Verify exit', "Really quit?")
    if ans:
        root.destroy()

def from_files():
    global s, file_path
    file_path = askdirectory()
    s.set(file_path) 


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Tibetan Machine Uni} -size 12 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        master.configure(highlightcolor="black")
        global r, temp, u, s, photo
        s = StringVar()
        r = IntVar()
        u = IntVar()
        temp = StringVar()

        self.Frame1 = Frame(master)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.97, relwidth=0.97)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=585)

        self.Step1 = LabelFrame(self.Frame1)
        self.Step1.place(relx=0.05, rely=0.22, relheight=0.7, relwidth=0.43)
        self.Step1.configure(relief=GROOVE)
        self.Step1.configure(text='''Step1''')
        self.Step1.configure(width=250)

        self.Label2 = Label(self.Step1)
        self.Label2.place(relx=0.16, rely=0.25, height=23, width=154)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font=font11)
        self.Label2.configure(text='''Enter Temperature in K''')

        self.Entry1 = Entry(self.Step1)
        self.Entry1.place(relx=0.16, rely=0.31, relheight=0.06, relwidth=0.62)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(takefocus="0", textvariable=temp)

        self.Message1 = Message(self.Step1)
        self.Message1.place(relx=0.08, rely=0.06, relheight=0.16, relwidth=0.85)
        self.Message1.configure(font=font11)
        self.Message1.configure(text='''To extract data from .trace file enter the temperature at which you require your data''')
        self.Message1.configure(width=213)

        self.Button1 = Button(self.Step1)
        self.Button1.place(relx=0.24, rely=0.82, height=27, width=127)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Extract''')
        self.Button1.configure(command=ext_cmd)

        self.Label3 = Label(self.Step1)
        self.Label3.place(relx=0.04, rely=0.65, height=39, width=236)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font=font11)
        self.Label3.configure(text='''To begin extracting press below''')

        self.Step2 = LabelFrame(self.Frame1)
        self.Step2.place(relx=0.53, rely=0.22, relheight=0.7, relwidth=0.43)
        self.Step2.configure(relief=GROOVE)
        self.Step2.configure(text='''Step2''')
        self.Step2.configure(width=250)

        self.Label1 = Label(self.Step2)
        self.Label1.place(relx=0.08, rely=0.11, height=29, width=201)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font=font10)
        self.Label1.configure(text='''Select any data to plot''')

        self.DOS = Radiobutton(self.Step2)
        self.DOS.place(relx=0.16, rely=0.25, relheight=0.07, relwidth=0.26)
        self.DOS.configure(activebackground="#d9d9d9")
        self.DOS.configure(font=font11)
        self.DOS.configure(justify=LEFT)
        self.DOS.configure(takefocus="0")
        self.DOS.configure(text='''DOS''')
        self.DOS.configure(value="3",variable=r)

        self.Seebeck_Coefficient = Radiobutton(self.Step2)
        self.Seebeck_Coefficient.place(relx=0.16, rely=0.34, relheight=0.07
                , relwidth=0.64)
        self.Seebeck_Coefficient.configure(activebackground="#d9d9d9")
        self.Seebeck_Coefficient.configure(font=font11)
        self.Seebeck_Coefficient.configure(justify=LEFT)
        self.Seebeck_Coefficient.configure(takefocus="0")
        self.Seebeck_Coefficient.configure(text='''Seebeck Coefficient''')
        self.Seebeck_Coefficient.configure(value="4",variable=r)

        self.Electrical_Conductivity = Radiobutton(self.Step2)
        self.Electrical_Conductivity.place(relx=0.16, rely=0.42, relheight=0.07
                , relwidth=0.71)
        self.Electrical_Conductivity.configure(activebackground="#d9d9d9")
        self.Electrical_Conductivity.configure(font=font11)
        self.Electrical_Conductivity.configure(justify=LEFT)
        self.Electrical_Conductivity.configure(takefocus="0")
        self.Electrical_Conductivity.configure(text='''Electrical Conductivity''')
        self.Electrical_Conductivity.configure(value="5",variable=r)

        self.Carrier_Concentration = Radiobutton(self.Step2)
        self.Carrier_Concentration.place(relx=0.16, rely=0.59, relheight=0.07
                , relwidth=0.68)
        self.Carrier_Concentration.configure(activebackground="#d9d9d9")
        self.Carrier_Concentration.configure(font=font11)
        self.Carrier_Concentration.configure(justify=LEFT)
        self.Carrier_Concentration.configure(takefocus="0")
        self.Carrier_Concentration.configure(text='''Carrier Concentration''')
        self.Carrier_Concentration.configure(value="2",variable=r)

        self.Thermal_Conductivity = Radiobutton(self.Step2)
        self.Thermal_Conductivity.place(relx=0.16, rely=0.51, relheight=0.07
                , relwidth=0.69)
        self.Thermal_Conductivity.configure(activebackground="#d9d9d9")
        self.Thermal_Conductivity.configure(font=font11)
        self.Thermal_Conductivity.configure(justify=LEFT)
        self.Thermal_Conductivity.configure(takefocus="0")
        self.Thermal_Conductivity.configure(text='''Thermal Conductivity''')
        self.Thermal_Conductivity.configure(value="7",variable=r)

        self.Plot = Button(self.Step2)
        self.Plot.place(relx=0.24, rely=0.82, height=27, width=134)
        self.Plot.configure(activebackground="#d9d9d9")
        self.Plot.configure(takefocus="0")
        self.Plot.configure(text='''Plot''')
        self.Plot.configure(width=134)
        self.Plot.configure(command=plt)

        self.u_Ry = Radiobutton(self.Step2)
        self.u_Ry.place(relx=0.16, rely=0.73, relheight=0.06, relwidth=0.26)
        self.u_Ry.configure(activebackground="#d9d9d9")
        self.u_Ry.configure(justify=LEFT)
        self.u_Ry.configure(text=u'''\u03bc (Ry)''')
        self.u_Ry.configure(value="0",variable=u)

        self.u_eV = Radiobutton(self.Step2)
        self.u_eV.place(relx=0.52, rely=0.73, relheight=0.06, relwidth=0.34)
        self.u_eV.configure(activebackground="#d9d9d9")
        self.u_eV.configure(justify=LEFT)
        self.u_eV.configure(text=u'''\u03bc - Ef (eV)''')
        self.u_eV.configure(value="10",variable=u)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.02, rely=0.95, relheight=0.05, relwidth=0.1)
        self.Message2.configure(text='''Ver 0.1''')
        self.Message2.configure(width=70)

        self.Quit = Button(self.Frame1)
        self.Quit.place(relx=0.8, rely=0.93, height=27, width=91)
        self.Quit.configure(activebackground="#d9d9d9")
        self.Quit.configure(text='''Quit''')
        self.Quit.configure(command=quit)

        self.Path = Button(self.Frame1)
        self.Path.place(relx=0.41, rely=0.06, height=27, width=98)
        self.Path.configure(activebackground="#d9d9d9")
        self.Path.configure(text='''Import Path''')
        self.Path.configure(command=from_files)

        self.Message3 = Label(self.Frame1)
        self.Message3.place(relx=0.22, rely=0.14, relheight=0.05, relwidth=0.59)
        self.Message3.configure(cursor="xterm")
        self.Message3.configure(textvariable=s)
        self.Message3.configure(width=70)

        self.logo = Canvas(self.Frame1)
        self.logo.place(relx=0.02, rely=0.02, relheight=0.18, relwidth=0.16)
        self.logo.configure(borderwidth="2")
        # self.logo.configure(relief=RIDGE)
        self.logo.configure(selectbackground="#c4c4c4")
        self.logo.configure(width=94)
        self.logo.create_image(20,20, image=photo)
                       
if __name__ == '__main__':
    start_gui()