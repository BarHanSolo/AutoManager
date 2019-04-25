import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont
from math import floor as mfloor
import pickle
#def callback():
#    print("click!")
saveName='sav1'
windowWidth=800
windowHeight=600
with open(saveName, 'rb') as f:
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
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StatsPage, CarPage, DriversPage, MoneyPage, WikiPage, RanksPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.config(bg=color0hex, ) #color for entire frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StatsPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        buttonWidth=mfloor((windowWidth/6)/7.5)
        tk.Button(self, text="Stats", command=lambda: controller.show_frame("StatsPage"), width = buttonWidth, bg=color0hex, fg=color1hex).grid(row=0, column=1, pady=10)
        tk.Button(self, text="Drivers", command=lambda: controller.show_frame("DriversPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=2)
        tk.Button(self, text="Cars", command=lambda: controller.show_frame("CarPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=3)
        tk.Button(self, text="Money", command=lambda: controller.show_frame("MoneyPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=4)
        tk.Button(self, text="Ranks", command=lambda: controller.show_frame("RanksPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=5)
        tk.Button(self, text="Wiki", command=lambda: controller.show_frame("WikiPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=6)
        Frame(self, bg=color2hex, height=5, width=windowWidth).grid(row=2, column=1, columnspan=6) #linia przerwy między menu, a resztą strony
        Frame(self, bg=color2hex, height=5, width=windowWidth).grid(row=10, column=1, columnspan=6) #linia przerwy między resztą strony, a paskiem czasu

class StatsPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Stats of Your team", font=controller.title_font,bg=color0hex).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)
        tk.Label(self, text=color0, font=controller.title_font,bg=color0hex).grid(row=3, column=1, columnspan=7)
        tk.Label(self, text=color1, font=controller.title_font,bg=color0hex).grid(row=4, column=1, columnspan=7)
        tk.Label(self, text=color2, font=controller.title_font,bg=color0hex).grid(row=5, column=1, columnspan=7)

class CarPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Cars", font=controller.title_font).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class DriversPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Drivers and Workers", font=controller.title_font).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class MoneyPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Money and Sponsors", font=controller.title_font).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class RanksPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Ranks for all Teams", font=controller.title_font).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class WikiPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Wikipedia of Motorsport", font=controller.title_font).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

if __name__ == "__main__":
    app = SampleApp()
    app.title("AutoManager")
    back = tk.Frame(master=app, width=windowWidth, height=windowHeight, bg=color0hex)
    back.pack()
    app.mainloop()
