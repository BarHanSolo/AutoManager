import pygame
import io
import pickle
import wcag_contrast_ratio as contrast
import datetime
from faker import Faker
seed="3815637451969776267516610984202742489301"
numberofteams=10
numberofraces=20

def seedmaker(seed): #makes numerical seed from string
    numbers="";
    for x in range(len(seed)):
        if (seed[x].isnumeric()==True):
            numbers=numbers+seed[x]
        else:
            numbers=numbers+str(ord(seed[x]))
    while len(numbers)<40:
        for y in range(40-len(numbers)):
            numbers=numbers+numbers[y]
    if (len(numbers)>40):
        numbers=numbers[0:40]
    return numbers

def numberofteamsgenerator(seed): #makes number of teams
    initial=seed[13:14]
    while int(initial)<7 or int(initial)>13:
        initial=int(initial)+5
    return initial

def numberofracesgenerator(seed): #makes number of races
    initial=seed[23:25]
    while int(initial)<17 or int(initial)>23:
        initial=int(initial)+5
    return initial

def teammaker(numberofteams, seed): #provides list of teams in correct number
    f= open("teamlist.txt","w+") #file with empty teamlist
    g= open("teams1.txt","r+") #file with prefix
    h= open("teams2.txt","r+") #file with suffix
    linesg=g.readlines()
    linesh=h.readlines()
    initial=int(seed[7]+seed[17]);
    plus=int(seed[15]+seed[8]);
    for x in range(numberofteams): #generating each team
        while initial+plus>len(linesh)-1:
            initial=initial-len(linesh)
            while initial>len(linesg)-1:
                initial=initial-len(linesg)
        if (initial>len(linesg)-1):
            initial=initial-len(linesg)
        var1 = linesg[initial].rstrip()
        var2 = linesh[initial+plus].rstrip()
        f.close()
        ff= open("teamlist.txt","r")
        #check if var2 allready exists
        extras=1
        while var2 in ff.read():
            var2 = linesh[initial+plus+extras].rstrip()
            extras+=1
        ff.close()
        f=open("teamlist.txt","a")
        #combine them all depending on the -fix
        if var1=='':
            f.write(var2+'\n')
        elif var1=='GP' or var1=='Racers' or var1=='Racing':
            f.write(var2+' '+var1+'\n')
        else:
            f.write(var1 + ' '+var2+'\n')
        while plus>39:
            plus=plus-40
        initial=initial+int(seed[plus])
        plus=plus+int(seed[initial])
    f.close()
    g.close()
    h.close()

def personmaker(numberofnames, seed, who): #provides lists of persons
    whonuma='' #number connected to who
    for y in range(len(who)):
        whonuma=whonuma+str(ord(who[y]))
    f= open("localizations.txt","r+")
    with io.open(who+".txt", 'w+', encoding='utf8') as g:
        h= open(who+"coun.txt","w+")
        linesf=f.readlines()
        for x in range(numberofnames):
            numa=seed[x:x+3] #quasi random number from seed to generate country
            countrynumber=(int(numa)+int(whonuma))%len(linesf)
            country=linesf[countrynumber].split(' - ')
            fake = Faker(country[0])
            fake.seed(seed+str(x))
            var1 = fake.name()+'\n'
            g.write(var1)
            h.write(country[1])
        f.close()
        g.close()
        h.close()

def colorpicker(numberofsets, seed, who): #provides sets of 3 colors and saves in file
    whonuma='' #number connected to who
    for y in range(len(who)):
        whonuma=whonuma+str(ord(who[y]))
    f= open("colors.txt","r+")
    linesf=f.readlines()
    g= open(who+"colors.txt","w+")
    for x in range(numberofsets):
        numa0=seed[x:x+3] #quasi random number from seed to generate palette
        numa1=int(seed[x:x+3])*7.5 #and two more of those to generate 3 colors in total
        numa2=int(seed[x:x+4])/3.14
        prevcolor=''
        for y in range(3):
            colortuple=()
            colornumber=((int(eval("numa"+str(y)))+int(whonuma))%len(linesf)) #picking color number
            color=linesf[colornumber].rstrip()
            colorbase=color[1:len(color)-1].split(',')
            for val in colorbase: #converting string color to tuple, changing it's value to use in contrast
                val=int(val)/255
                colortuple = colortuple+(val,)
            if prevcolor!='': #if previos color exists, check if it is AA; cryterium of minimum contrast
                con=contrast.rgb(colortuple, prevcolor)
                print(con)
                while con<4.5:
                    colornumber=colornumber+1
                    color=linesf[colornumber].rstrip()
                    colorbase=color[1:len(color)-1].split(',')
                    colortuple=()
                    for val in colorbase:
                        val=int(val)/255
                        colortuple = colortuple+(val,)
                    con=contrast.rgb(colortuple, prevcolor)
            prevcolor=colortuple
            g.write(color+' ')
        g.write('\n')
    g.close()
    f.close()

def statsmaker(numberofsets, seed, who, howmany): #makes list of statistics of whatever we want; numbers are from 1 to 10
    f= open(who+"stats.txt","w+")
    whonuma='' #number connected to who
    for y in range(len(who)):
        whonuma=whonuma+str(ord(who[y]))
    for x in range(numberofsets):
        list=[]
        for y in range(howmany):
            tempnumber=int(seed[x+y])*(int(whonuma)+int(seed[y]))
            list.append((tempnumber%11))
        avg=0
        for item in list:
            avg=avg+item
            f.write(str(item)+' ')
        f.write(str(avg/howmany)+' ')
        f.write('\n')
    f.close()

def leaguechoser(seed):
    f= open("leagues.txt","r+")
    linesf=f.readlines()
    initial=seed[18:23]
    leaguenumber=int(initial)%len(linesf)
    league=linesf[leaguenumber]
    leaguelist=league.split("\t")
    pickle.dump(leaguelist, open("league.p", "wb"))

def carmaker(seed):#todo
    pass

def tracksmaker(numberofraces, seed):
    f= open("localizations.txt","r+")
    linesf=f.readlines()
    with io.open("tracklist.txt", 'w+', encoding='utf8') as g:
        for x in range(numberofraces):
            h=open("tracklist.txt", "r+")
            linesg=g.readlines()
            numa=seed[x+1:x+4] #quasi random number from seed to generate country
            countrynumber=(int(numa))%len(linesf)
            country=linesf[countrynumber].split(' - ')
            j=1
            g.close()
            print(*g)
            while country[1] in g:
                country = linesf[countrynumber+j].split(' - ')
                j=j+1
            fake = Faker(country[0])
            fake.seed(seed+str(x))
            var1 = fake.city()+'\n'
            g.write("GP of "+ country[1].rstrip()+ " in " + var1)
            h.close()
        f.close()
        g.close()

def leaguemaker(): #to change when i have two upper
    leaguelist=pickle.load(open("league.p", "rb"))
    nameofleague=leaguelist[0]
    date = datetime.date(int(leaguelist[1])+int(seed[39]), 1, 1)
    car = leaguelist[2]
    trackset = leaguelist[3]
    tracknum = leaguelist[4]
    return nameofleague, date, car, trackset, tracknum

#favorite_color = { "lion": "yellow", "kitty": "red" }
#pickle.dump( favorite_color, open( "save.p", "wb" ) )

tracksmaker(numberofraces, seed)
