import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox
from math import floor as mfloor
from faker import Faker
from PIL import Image, ImageDraw
import pickle
from colour import Color
import colorsys
import random
saveName='sav1'
windowWidth=800
windowHeight=400
buttonWidth=mfloor((windowWidth/7)/7.5)
with open('sav1', 'rb') as f:
    data = pickle.load(f)
color0=data['playercolors'][0]
color1=data['playercolors'][1]
color2=data['playercolors'][2]
color0hex='#%02x%02x%02x' % color0
color1hex='#%02x%02x%02x' % color1
color2hex='#%02x%02x%02x' % color2

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Lato', size=18, weight="bold", slant="italic")
        self.bgCol = color0hex
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MenuMenu, MenuOptions):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.config(bg=color0hex, )
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def save_game(self, save_name):
        '''save all things'''
        with open(save_name, 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        messagebox.showinfo(save_name, "Game saved")

    def load_game(self, save_name):
        '''load all things'''
        global data
        with open(save_name, 'rb') as f:
            data = pickle.load(f)
        messagebox.showinfo(save_name, "Game loaded")

    def open(self, windowname):
        exec(compile(open(windowname, "rb").read(), windowname, 'exec'), )

class MenuMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Button(self, text="New game", command =lambda: SampleApp.open(self, "secondwindow.py"), width = buttonWidth, bg=color0hex).grid(row=1, column=1, pady=10)
        tk.Button(self, text="Load game", width = buttonWidth, bg=color0hex).grid(row=2, column=1, pady=10)
        tk.Button(self, text="Options",  width = buttonWidth, bg=color0hex).grid(row=3, column=1, pady=10)
        tk.Button(self, text="Exit game", command =lambda: sys.exit(), width = buttonWidth, bg=color0hex).grid(row=4, column=1, pady=10)

    def opener(self):
        with open("secondwindow.py") as f:
            code = compile(f.read(), "somefile.py", 'exec')
            exec(code)

class MenuOptions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

if __name__ == "__main__":
    app = SampleApp()
    app.title("AutoManager")
    back = tk.Frame(master=app, width=windowWidth, height=windowHeight, bg=color0hex)
    back.pack()
    app.mainloop()
