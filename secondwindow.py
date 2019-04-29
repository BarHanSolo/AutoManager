import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont
from math import floor as mfloor
from faker import Faker
from PIL import Image, ImageDraw
import pickle
from colour import Color
import colorsys
import random
#def callback():
#    print("click!")
saveName='sav1'
windowWidth=800
windowHeight=400
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
        self.title_font = tkfont.Font(family='Lato', size=18, weight="bold", slant="italic")
        self.bgCol = color0hex
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

class Draw(tk.Frame):
    def colors(name, count):
        my_dict = {}
        fake=Faker()
        fake.seed(name)
        my_dict['col0']=fake.hex_color()
        my_dict['col1']=fake.hex_color()
        col0=Color(my_dict['col0'])
        col1=Color(my_dict['col1'])
        h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
        r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
        col0 = (r,g,b)
        col0 = '#%02x%02x%02x' % col0
        my_dict['col0']=col0
        col0=Color(my_dict['col0'])
        #h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
        #r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
        #col1 = (r,g,b)
        #col1 = '#%02x%02x%02x' % col1
        #col1=Color(my_dict['col1'])
        collist = list(col0.range_to(Color(col1),10,))
        for x in range(1,count):
            colname='col'+str(x+1)
            my_dict[colname]=collist[x].hex
        print(my_dict)
        return my_dict
    def helmetDraw(name, canvas):
        from random import seed
        from random import randint
        seed(name)
        picnum=randint(0,6)
        col = Draw.colors(name, 2)
        imgname="src/helmets/helmet"+str(picnum)+".png"
        im = Image.open(imgname)
        pix=im.load()
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                tempcol=pix[x,y]
                tempcol=tempcol[0:3]
                tempcol='#%02x%02x%02x' % tempcol
                if (tempcol=="#ffffff"):
                    canvas.create_line(x,y,x+1,y, fill=color0hex)
                elif (tempcol=="#000000"):
                    canvas.create_line(x,y,x+1,y, fill=tempcol)
                elif (tempcol=="#ff0000"):
                    canvas.create_line(x,y,x+1,y, fill=col["col0"])
                elif (tempcol=="#00ff00"):
                    canvas.create_line(x,y,x+1,y, fill=col["col1"])
                elif (tempcol=="#0000ff"):
                    canvas.create_line(x,y,x+1,y, fill=col["col2"])
                elif (tempcol=="#ff00ff"):
                    canvas.create_line(x,y,x+1,y, fill="#808182")
                elif (tempcol=="#00ffff"):
                    canvas.create_line(x,y,x+1,y, fill="#7abcff")
    def carDraw(name, canvas):
        from random import seed
        from random import randint
        seed(name)
        picnum=randint(0,3)
        col = Draw.colors(name, 4)
        imgname="src/cars/car"+str(picnum)+".png"
        im = Image.open(imgname)
        pix=im.load()
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                tempcol=pix[x,y]
                tempcol=tempcol[0:5]
                tempcol='#%02x%02x%02x' % tempcol
                if (tempcol=="#ffffff"):
                    canvas.create_line(x,y,x+1,y, fill=color0hex)
                elif (tempcol=="#000000"):
                    canvas.create_line(x,y,x+1,y, fill=tempcol)
                elif (tempcol=="#ff0000"):
                    canvas.create_line(x,y,x+1,y, fill=col["col0"])
                elif (tempcol=="#00ff00"):
                    canvas.create_line(x,y,x+1,y, fill=col["col1"])
                elif (tempcol=="#0000ff"):
                    canvas.create_line(x,y,x+1,y, fill=col["col2"])
                elif (tempcol=="#ffff00"):
                    canvas.create_line(x,y,x+1,y, fill=col["col3"])
                elif (tempcol=="#00ffff"):
                    canvas.create_line(x,y,x+1,y, fill=col["col4"])

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
        tk.Label(self, text="Stats of Your team", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)
        tk.Label(self, text=color0, font=controller.title_font,bg=controller.bgCol).grid(row=3, column=1, columnspan=7)
        tk.Label(self, text=color1, font=controller.title_font,bg=controller.bgCol).grid(row=4, column=1, columnspan=7)
        tk.Label(self, text=color2, font=controller.title_font,bg=controller.bgCol).grid(row=5, column=1, columnspan=7)

class CarPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Cars", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class DriversPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Drivers and Workers", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)
        self.helmet1=tk.Canvas(self, width=500, height=137, highlightthickness=0)
        self.helmet1.grid(sticky="W",row=3, column=1, columnspan=7, padx=10)
        self.helmet2=tk.Canvas(self, width=500, height=137, highlightthickness=0)
        self.helmet2.grid(sticky="W",row=4, column=1, columnspan=7, padx=10)

class MoneyPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Money and Sponsors", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class RanksPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Ranks for all Teams", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

class WikiPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Wikipedia of Motorsport", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)

if __name__ == "__main__":
    app = SampleApp()
    app.title("AutoManager")
    Draw.carDraw("88888", app.frames['DriversPage'].helmet1)
    Draw.carDraw("88887", app.frames['DriversPage'].helmet2)
    back = tk.Frame(master=app, width=windowWidth, height=windowHeight, bg=color0hex)
    back.pack()
    app.mainloop()
