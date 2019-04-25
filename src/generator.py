import io
import pickle
import wcag_contrast_ratio as contrast
import datetime
from faker import Faker
seed = "3815637451969776267516610984202742489301"
numberofteams = 10
numberofraces = 20


def seedmaker(seed):
    """makes numerical seed from string"""
    numbers = ""
    for x in seed:
        if x.isnumeric():
            numbers = numbers+x
        else:
            numbers = numbers+str(ord(x))
    while len(numbers) < 40:
        for y in range(40-len(numbers)):
            numbers = numbers+numbers[y]
    if len(numbers) > 40:
        numbers = numbers[0:40]
    return numbers


def numberofteamsgenerator(seed):
    """makes number of teams"""
    initial = int(seed[13:15])
    # number of teams should be between 7 and 13 inclusive, which gives range of 7
    initial = initial % 7
    return initial + 7


def numberofracesgenerator(seed):
    """makes number of races"""
    initial = seed[23:25]
    # number of races should be between 17 and 23 inclusive, which gives range of 7
    initial = initial % 7
    return initial + 7


def teammaker(numberofteams, seed):
    """provides list of teams in correct number"""
    f = open("teamlist.txt", "w+")  # file with empty teamlist
    g = open("teams1.txt", "r+")  # file with prefix
    h = open("teams2.txt", "r+")  # file with suffix
    linesg = g.readlines()
    linesh = h.readlines()
    initial = int(seed[7]+seed[17])
    plus = int(seed[15]+seed[8])
    for x in range(numberofteams):  # generating each team
        while initial+plus > len(linesh)-1:
            initial = initial-len(linesh)
            while initial > len(linesg)-1:
                initial = initial-len(linesg)
        if initial > len(linesg)-1:
            initial = initial-len(linesg)
        var1 = linesg[initial].rstrip()
        var2 = linesh[initial+plus].rstrip()
        ff = open("teamlist.txt", "r")
        # check if var2 already exists
        extras=1
        while var2 in ff.read():
            var2 = linesh[initial+plus+extras].rstrip()
            extras += 1
        ff.close()
        # combine them all depending on the -fix
        if var1 == '':
            f.write(var2+'\n')
        elif var1 == 'GP' or var1 == 'Racers' or var1 == 'Racing':
            f.write(var2+' '+var1+'\n')
        else:
            f.write(var1 + ' '+var2+'\n')
        while plus > 39:
            plus = plus-40
        initial = initial+int(seed[plus])
        plus = plus+int(seed[initial])
    f.close()
    g.close()
    h.close()


def personmaker(numberofnames, seed, who):
    """provides lists of persons"""
    whonuma = ''  # number connected to who
    for y in range(len(who)):
        whonuma = whonuma+str(ord(who[y]))
    f = open("localizations.txt", "r+")
    with io.open(who+".txt", 'w+', encoding='utf8') as g:
        h = open(who+"coun.txt", "w+")
        linesf = f.readlines()
        for x in range(numberofnames):
            numa = seed[x:x+3]  # quasi random number from seed to generate country
            countrynumber = (int(numa)+int(whonuma)) % len(linesf)
            country = linesf[countrynumber].split(' - ')
            fake = Faker(country[0])
            fake.seed(seed+str(x))
            var1 = fake.name()+'\n'
            g.write(var1)
            h.write(country[1])
        h.close()
    f.close()


def colorpicker(numberofsets, seed, who):
    """provides sets of 3 colors and saves in file"""
    whonuma = ''  # number connected to who
    for y in who:
        whonuma = whonuma + str(ord(y))
    f = open("colors.txt", "r+")
    linesf = f.readlines()
    g = open(who+"colors.txt", "w+")
    for x in range(numberofsets):
        numa0 = seed[x:x+3]  # quasi random number from seed to generate palette
        numa1 = int(seed[x:x+3])*7.5  # and two more of those to generate 3 colors in total
        numa2 = int(seed[x:x+4])/3.14
        prevcolor = ''
        for y in range(3):
            colortuple = ()
            colornumber = ((int(eval("numa"+str(y)))+int(whonuma))%len(linesf))  # picking color number
            color = linesf[colornumber].rstrip()
            colorbase = color[1:len(color)-1].split(',')
            for val in colorbase:  # converting string color to tuple, changing it's value to use in contrast
                val = int(val)/255
                colortuple = colortuple+(val,)
            if prevcolor != '':  # if previous color exists, check if it is AA; cryterium of minimum contrast
                con = contrast.rgb(colortuple, prevcolor)
                print(con)
                while con < 4.5:
                    colornumber = colornumber+1
                    color = linesf[colornumber].rstrip()
                    colorbase = color[1:len(color)-1].split(',')
                    colortuple = ()
                    for val in colorbase:
                        val = int(val)/255
                        colortuple = colortuple+(val,)
                    con = contrast.rgb(colortuple, prevcolor)
            prevcolor = colortuple
            g.write(color+' ')
        g.write('\n')
    g.close()
    f.close()


def statsmaker(numberofsets, seed, who, howmany):
    """makes list of statistics of whatever we want; numbers are from 1 to 10"""
    f = open(who+"stats.txt", "w+")
    whonuma = ''  # number connected to who
    for y in range(len(who)):
        whonuma = whonuma+str(ord(who[y]))
    for x in range(numberofsets):
        stats_list = []
        for y in range(howmany):
            tempnumber = int(seed[x+y])*(int(whonuma)+int(seed[y]))
            stats_list.append((tempnumber % 11))
        avg = 0
        for item in stats_list:
            avg = avg+item
            f.write(str(item)+' ')
        f.write(str(avg/howmany)+' ')
        f.write('\n')
    f.close()


def leaguechooser(seed):
    f = open("leagues.txt", "r+")
    linesf = f.readlines()
    initial = seed[18:23]
    leaguenumber = int(initial) % len(linesf)
    league = linesf[leaguenumber]
    leaguelist = league.split("\t")
    pickle.dump(leaguelist, open("league.p", "wb"))


def carmaker(seed):  # todo
    pass


def leaguemaker():  # to change when i have two upper
    leaguelist = pickle.load(open("league.p", "rb"))
    nameofleague = leaguelist[0]
    date = datetime.date(int(leaguelist[1])+int(seed[39]), 1, 1)
    car = leaguelist[2]
    trackset = leaguelist[3]
    tracknum = leaguelist[4]
    return nameofleague, date, car, trackset, tracknum


def tracksmaker(numberofraces, seed):
    import random
    random.seed(seed)

    f = open("localizations.txt", "r+")
    linesf = f.readlines()
    with io.open("tracklist.txt", 'w+', encoding='utf8') as g:  # to delete previous file, find better way
        g.writelines(random.sample(linesf, numberofraces))

    f.close()

tracksmaker(numberofraces, seed)
