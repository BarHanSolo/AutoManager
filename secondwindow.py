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
import random, os
from firstwindow import MenuMenu, MenuOptions
from inspect import getfullargspec
import math
#def callback():
#    print("click!")
#saveName='sav1'
windowWidth=800
windowHeight=400
buttonWidth=mfloor((windowWidth/7)/7.5)
trackname1="Tu na razie jest ściernisco ale będzie San Francisco"
data={}
color0hex='Red'
color1hex='Red'
color2hex='Red'
colorbgmenu='#ff2800'
colortextmenu='#FCD112'

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Lato', size=18, weight="bold", slant="italic")
        self.bgCol = color0hex
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        print(container)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StatsPage, CarPage, DriversPage, MoneyPage, WikiPage, RanksPage, EscPage, MenuMenu, OptionsMenu, NewGameMenu, LoadGameMenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            if "Menu" in page_name:
                frame.config(bg=colorbgmenu, )
            else:
                frame.config(bg=color0hex, ) #color for entire frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MenuMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def reload_frames(self):
        pass

    def save_game(self, save_name):
        '''save all things'''
        with open(save_name, 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        messagebox.showinfo(save_name, "Game saved")

class GameLoading(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

    def load_game(self, save_name):
        '''load all things'''
        global data
        with open('saves/'+save_name, 'rb') as f:
            data = pickle.load(f)
        color0=data['playercolors'][0]
        color1=data['playercolors'][1]
        color2=data['playercolors'][2]
        color0hex='#%02x%02x%02x' % color0
        color1hex='#%02x%02x%02x' % color1
        color2hex='#%02x%02x%02x' % color2
        #messagebox.showinfo(save_name, "Game loaded")
        self.controller.show_frame("StatsPage")

class Draw(tk.Frame):
    def colors(name, count):
        my_dict = {}
        fake=Faker()
        fake.seed(name)
        my_dict['col0']=fake.hex_color()
        my_dict['col1']=fake.hex_color()
        h,s,l = random.random(), 0.5 + random.random()/2.0, random.random()
        r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
        col0 = (r,g,b)
        col0 = '#%02x%02x%02x' % col0
        my_dict['col0']=col0
        col0=Color(my_dict['col0'])
        h,s,l = random.random(), 0.5 + random.random()/2.0, random.random()
        r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
        col1 = (r,g,b)
        col1 = '#%02x%02x%02x' % col1
        col1=Color(my_dict['col1'])
        if "Ferrari" in name:
            col0='#D40000'
            my_dict['col0']=col0
            col0=Color(my_dict['col0'])
        elif "McLaren" in name:
            col0='#c0c0c0'
            my_dict['col0']=col0
            col0=Color(my_dict['col0'])
        elif "Jaguar" in name:
            col0='#004225'
            my_dict['col0']=col0
            col0=Color(my_dict['col0'])
        elif "Gordini" in name:
            col0='#318CE7'
            my_dict['col0']=col0
            col0=Color(my_dict['col0'])
        collist = list(col0.range_to(Color(col1),6,))
        print(collist)
        for x in range(1,count):
            colname='col'+str(x+1)
            my_dict[colname]=collist[x].hex
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
    def trackGen(name):
        pixels=100
        fake=Faker()
        fake.seed(name)
        trackTable=[]
        for x in range(pixels):
            for y in range(pixels):
                num = fake.pydecimal(left_digits=3, right_digits=0, positive=True)
                if num==0.0:
                    trackTable.append(1)
                else:
                    trackTable.append(0)
        return trackTable
    def trackGen2(name):
        pixels=100
        from random import seed
        from random import randint
        seed(name)
        curvenum=randint(11,21)
        dots=[]
        for x in range(curvenum):
            dots.append([randint(0,pixels-1),randint(0,pixels-1)])
        return dots
    def clockwiseangle_and_distance(point):
        origin=[60,70]
        refvec = [0, 1]
        # Vector between point and the origin: v = p - o
        vector = [point[0]-origin[0], point[1]-origin[1]]
        # Length of vector: ||v||
        lenvector = math.hypot(vector[0], vector[1])
        # If length is zero there is no angle
        if lenvector == 0:
            return -math.pi, 0
        # Normalize vector: v/||v||
        normalized = [vector[0]/lenvector, vector[1]/lenvector]
        dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
        diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
        angle = math.atan2(diffprod, dotprod)
        # Negative angles represent counter-clockwise angles so we need to subtract them
        # from 2*pi (360 degrees)
        if angle < 0:
            return 2*math.pi+angle, lenvector
        # I return first the angle because that's the primary sorting criterium
        # but if two vectors have the same angle then the shorter distance should come first.
        return angle, lenvector
    def trackDraw(name, canvas):
        dots=Draw.trackGen2(name)
        #dots=[]
        #for x in range(100):
    #        for y in range(100):
    #            if trackList[(x*100)+y]==1:
    #                dots.append([x,y])
        print(dots)
        dots=sorted(dots, key=Draw.clockwiseangle_and_distance)
        print(dots)
        #key=lambda k: [k[0]+k[1],k[0]]
        out = []
        for x,y in dots:
            out += [x*5, y*4]
        canvas.create_polygon(out, fill='', outline='black', smooth=0, width=8, joinstyle=ROUND, splinesteps=5)

class BackMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        Frame(self, bg=colortextmenu, height=5, width=windowWidth).grid(row=0, column=1, columnspan=7)
        Frame(self, bg=colortextmenu, height=5, width=windowWidth).grid(row=10, column=1, columnspan=7)
        tk.Button(self, text="Back", command=lambda: controller.show_frame("MenuMenu"), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=11, column=2, pady=10)
         #przyciski na dole z paskiem, back oraz ok

class MenuMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Frame(self, bg=colortextmenu, height=5, width=windowWidth).grid(row=0, column=1, columnspan=7)
        tk.Button(self, text="New game", command =lambda: controller.show_frame("NewGameMenu"), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=1, column=4, pady=10)
        tk.Button(self, text="Load game", command =lambda: controller.show_frame("LoadGameMenu"), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=2, column=4, pady=10)
        tk.Button(self, text="Options", command =lambda: controller.show_frame("OptionsMenu"), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=3, column=4, pady=10)
        tk.Button(self, text="Exit game", command =lambda: sys.exit(), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=4, column=4, pady=10)
        Frame(self, bg=colortextmenu, height=5, width=windowWidth).grid(row=10, column=1, columnspan=7)

class OptionsMenu(BackMenu):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        BackMenu.__init__(self, parent, controller)

class NewGameMenu(BackMenu):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        BackMenu.__init__(self, parent, controller)

class LoadGameMenu(BackMenu):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        BackMenu.__init__(self, parent, controller)
        tk.Label(self, text="Choose your savefile:", font=controller.title_font, bg=colorbgmenu, fg=colortextmenu).grid(row=3, column=1, columnspan=3, pady=10)
        listbox=tk.Listbox(self, bg=colortextmenu, fg=colorbgmenu,selectbackground="Red",highlightcolor="Red")
        listbox.grid(row=5, column=3, columnspan=3, pady=10)
        for name in os.listdir('./saves'):
            listbox.insert('end', name)
        tk.Button(self, text="OK", command=lambda: GameLoading.load_game(self, listbox.get(listbox.curselection())), width = buttonWidth, bg=colorbgmenu, fg=colortextmenu).grid(row=11, column=6, pady=10)


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        buttonWidth=mfloor((windowWidth/7)/7.5)
        tk.Button(self, text="Stats", command=lambda: controller.show_frame("StatsPage"), width = buttonWidth, bg=color0hex, fg=color1hex).grid(row=0, column=1, pady=10)
        tk.Button(self, text="Drivers", command=lambda: controller.show_frame("DriversPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=2)
        tk.Button(self, text="Cars", command=lambda: controller.show_frame("CarPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=3)
        tk.Button(self, text="Money", command=lambda: controller.show_frame("MoneyPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=4)
        tk.Button(self, text="Ranks", command=lambda: controller.show_frame("RanksPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=5)
        tk.Button(self, text="Wiki", command=lambda: controller.show_frame("WikiPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=6)
        tk.Button(self, text="Menu", command=lambda: controller.show_frame("EscPage"), width = buttonWidth, bg=color0hex).grid(row=0, column=7)
        Frame(self, bg=color2hex, height=5, width=windowWidth).grid(row=2, column=1, columnspan=7) #linia przerwy między menu, a resztą strony
        Frame(self, bg=color2hex, height=5, width=windowWidth).grid(row=10, column=1, columnspan=7) #linia przerwy między resztą strony, a paskiem czasu, przyciski na górze

class StatsPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        tk.Label(self, text="Stats of Your team", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)
        #tk.Label(self, text=color0, font=controller.title_font,bg=controller.bgCol).grid(row=3, column=1, columnspan=7)
        #tk.Label(self, text=color1, font=controller.title_font,bg=controller.bgCol).grid(row=4, column=1, columnspan=7)
        #tk.Label(self, text=color2, font=controller.title_font,bg=controller.bgCol).grid(row=5, column=1, columnspan=7)

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
        tk.Label(self, text=trackname1, font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=3, column=1, columnspan=7, padx=10)
        self.helmet1=tk.Canvas(self, width=500, height=500, highlightthickness=0)
        self.helmet1.grid(sticky="W",row=4, column=1, columnspan=7, padx=10)
        self.helmet2=tk.Canvas(self, width=500, height=200, highlightthickness=0)
        self.helmet2.grid(sticky="W",row=5, column=1, columnspan=7, padx=10)

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

class EscPage(MenuPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MenuPage.__init__(self, parent, controller)
        buttonWidth=mfloor((windowWidth/7)/7.5)
        tk.Label(self, text="Menu", font=controller.title_font,bg=controller.bgCol).grid(sticky="W",row=1, column=1, columnspan=7, padx=10)
        #tk.Button(self, text="Save", command=lambda: controller.save_game('sav1'), width = buttonWidth, bg=color0hex).grid(row=3, column=4)
        tk.Button(self, text="Load", command=lambda: controller.load_game("EscPage"), width = buttonWidth, bg=color0hex).grid(row=4, column=4)
        tk.Button(self, text="Options", command=lambda: controller.show_frame("EscPage"), width = buttonWidth, bg=color0hex).grid(row=5, column=4)
        tk.Button(self, text="Exit to main menu", command =lambda: controller.show_frame("MenuMenu"), width = buttonWidth, bg=color0hex).grid(row=6, column=4)
        tk.Button(self, text="Exit to OS", command=lambda: sys.exit(), width = buttonWidth, bg=color0hex).grid(row=7, column=4)

if __name__ == "__main__":
    app = SampleApp()
    app.title("AutoManager")
    #Draw.helmetDraw("Ferrario12345678", app.frames['DriversPage'].helmet1)
    #Draw.trackDraw(trackname1, app.frames['DriversPage'].helmet1)
    back = tk.Frame(master=app, width=windowWidth, height=windowHeight, bg=color0hex)
    back.pack()
    app.mainloop()
