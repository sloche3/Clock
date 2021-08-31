from tkinter import *
from random import randint, choice
from datetime import datetime
import time

root = Tk()

# specify size of window.
#root.geometry("2000x1000")

root.attributes('-fullscreen', 1)

rows = 0
cols = 0
while True:
    if rows < 13:
        root.rowconfigure(rows, weight = 1)
        rows += 1
    if cols < 25:
        root.columnconfigure(cols, weight = 1)
        cols += 1
    if rows == 13 and cols == 25:
        break

boxes = {}
r = 0
c = 0
for i in range(325): # i got lazy here...
    ##    boxes[(c,r)] = Text(root, height = 1, width = 2)
    ##    print((c,r))
    ##    #boxes[i] = Text(root)
    ##    boxes[(c,r)].config(font = "Consolas 50")
    ##    boxes[(c,r)].tag_configure("center", justify='center')
    ##    boxes[(c,r)].insert(END, str(randint(0, 9)), )
    ##    boxes[(c,r)].tag_add("center", '1.0', 'end')
    if c < 25:

        boxes[(c,r)] = Text(root, relief = RIDGE, height = 1, width = 2, bg = "#%02x%02x%02x" % (0,34,64))
        #print((c,r))
        #boxes[i] = Text(root)
        boxes[(c,r)].config(font = "Consolas 50")
        boxes[(c,r)].tag_configure("center", justify='center')
        boxes[(c,r)].insert(END, chr(randint(48,122)), )
        boxes[(c,r)].tag_add("center", '1.0', 'end')
        boxes[(c,r)].tag_configure("here", foreground= "#%02x%02x%02x" % (81,103,193))
        #boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (255,131,43)) # orange
        #boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (5,252,79))
        boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (6,253,73))
        boxes[(c,r)].tag_configure("trueGreen", foreground= "#%02x%02x%02x" % (6,253,73))
        boxes[(c,r)].tag_add("here", "1.0", "1.4")

        boxes[(c,r)].grid(row = r, column = c)
        c += 1
    else:
        c = 0
        r += 1

        boxes[(c,r)] = Text(root, relief = RIDGE, height = 1, width = 2, bg = "#%02x%02x%02x" % (0,34,64))
        #print((c,r))
        #boxes[i] = Text(root)
        boxes[(c,r)].config(font = "Consolas 50")
        boxes[(c,r)].tag_configure("center", justify='center')
        boxes[(c,r)].insert(END, chr(randint(48,122)), )
        boxes[(c,r)].tag_add("center", '1.0', 'end')
        #boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (255,131,43))
        #boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (5,252,79))
        boxes[(c,r)].tag_configure("here", foreground= "#%02x%02x%02x" % (81,103,193))
        boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (6,253,73))
        boxes[(c,r)].tag_configure("trueGreen", foreground= "#%02x%02x%02x" % (6,253,73))
        boxes[(c,r)].tag_add("here", "1.0", "1.4")

        boxes[(c,r)].grid(row = r, column = c)
        c += 1

def gogo(x, y, times):
    boxes[(x,y)].delete(1.0)
    #time.sleep(2)
    boxes[(x,y)].insert(END, chr(randint(48,122)), )
    boxes[(x,y)].tag_add("center", '1.0', 'end')
    boxes[(x,y)].tag_add("here", "1.0", "1.4")
    if x == 24 and y == 12 and times == 3:
        #time.sleep(.5)
        #sp = UpdateForMin()
        root.after(0, fuck)
        print("      gogo")
        #print("here")


def rand():
    for x in range(4):
        for y in boxes:
            factor = randint(0,5)
            if y[0] == 24 and y[1] == 12 and x == 3:
                root.after(500, gogo, y[0], y[1], x)
                print("   rand")
            else:
                root.after(factor*100, gogo, y[0], y[1], x)
        #time.sleep(0.001)

#root.after(1000, rand)


def UpdateForMin():
    # returns secPos

    now = datetime.now()
    hour = now.strftime("%I")
    mins = now.strftime("%M")
    sec = now.strftime("%S")
    AmPm = now.strftime("%p")
    day = now.strftime("%A")
    month = now.strftime("%B")
    monthDay = now.strftime("%d")
    year = now.strftime("%Y")

    ##06:59:12
    ##PM
    ##
    ##Saturday
    ##
    ##August 28
    ##     2018


    tmp = [x for x in range(1, 12)]

    timeStr = f'{hour}:{mins}:{sec}'
    timeX = randint(1,15)
    timeY = randint(1,10)
    print(f'time: {(timeX,timeY)}')
    tmp.remove(timeY)
    tmp.remove(timeY+1)
    if timeY-1 in tmp:
        tmp.remove(timeY-1)
    if timeY+2 in tmp:
        tmp.remove(timeY+2)


    #######

    dateStr = f'{month} {monthDay}'
    dateXEnd = 23 - len(dateStr)
    dateX = randint(1, dateXEnd)
    dateY = choice(tmp)
    print(f'date: {(dateX,dateY)}')
    tmp.remove(dateY)
    if dateY-1 in tmp:
        tmp.remove(dateY-1)
    if dateY+1 in tmp:
        tmp.remove(dateY+1)
    if dateY+2 in tmp:
        tmp.remove(dateY+2)

    #######

    dayX = randint(1, dateXEnd)
    dayY = choice(tmp)

    #######

    for i in timeStr:
        boxes[(timeX,timeY)].delete(1.0)
        #time.sleep(2)
        boxes[(timeX,timeY)].tag_configure("blueColor", foreground='blue')
        boxes[(timeX,timeY)].insert(END, i, )
        boxes[(timeX,timeY)].tag_add("center", '1.0', 'end')
        boxes[(timeX,timeY)].tag_add('here', '1.0', 'end')
        root.after(400, FadeIn, boxes[(timeX,timeY)], [81,103,193])
        timeX += 1

    secPos = (timeX-2,timeY)

    timeX -= 8
    timeY += 1
    for i in AmPm:
        boxes[(timeX,timeY)].delete(1.0)
        boxes[(timeX,timeY)].tag_configure("blueColor", foreground='blue')
        #time.sleep(2)
        boxes[(timeX,timeY)].insert(END, i, )
        boxes[(timeX,timeY)].tag_add("center", '1.0', 'end')
        boxes[(timeX,timeY)].tag_add("here", '1.0', 'end')
        root.after(400, FadeIn, boxes[(timeX,timeY)], [81,103,193])
        timeX += 1

    #######

    for i in dateStr:
        if i != ' ':
            boxes[(dateX,dateY)].delete(1.0)
            boxes[(dateX,dateY)].tag_configure("blueColor", foreground='blue')
            #time.sleep(2)
            boxes[(dateX,dateY)].insert(END, i, )
            boxes[(dateX,dateY)].tag_add("center", '1.0', 'end')
            boxes[(dateX,dateY)].tag_add("here", '1.0', 'end')
            root.after(1200, FadeIn, boxes[(dateX,dateY)], [81,103,193])
            #dateX += 1
        dateX += 1

    dateX -= 4
    dateY += 1
    for i in year:
        boxes[(dateX,dateY)].delete(1.0)
        boxes[(dateX,dateY)].tag_configure("blueColor", foreground='blue')
        #time.sleep(2)
        boxes[(dateX,dateY)].insert(END, i, )
        boxes[(dateX,dateY)].tag_add("center", '1.0', 'end')
        boxes[(dateX,dateY)].tag_add("here", '1.0', 'end')
        root.after(1200, FadeIn, boxes[(dateX,dateY)], [81,103,193])
        dateX += 1

    #######

    for i in day:
        boxes[(dayX,dayY)].delete(1.0)
        boxes[(dayX,dayY)].tag_configure("blueColor", foreground='blue')
        #time.sleep(2)
        boxes[(dayX,dayY)].insert(END, i, )
        boxes[(dayX,dayY)].tag_add("center", '1.0', 'end')
        boxes[(dayX,dayY)].tag_add("here", '1.0', 'end')
        root.after(800, FadeIn, boxes[(dayX,dayY)], [81,103,193])
        dayX += 1

    # X = Columns
    # Y = Rows

    return secPos

def fuck():
    sss = UpdateForMin()
    root.after(0, runn, sss[0], sss[1], True)
    print("         fuck")
    print("------------------")


def runn(x,y, firstIter):

    rn = datetime.now()
    currSec = rn.strftime("%S")

    boxes[(x,y)].delete(1.0)
    boxes[(x,y)].tag_configure("blueColor", foreground='blue')
    boxes[(x,y)].insert(END, currSec[0], )
    boxes[(x,y)].tag_add("center", '1.0', 'end')
    #boxes[(x,y)].tag_add("tmpp", '1.0', 'end')

    boxes[(x+1,y)].delete(1.0)
    boxes[(x+1,y)].tag_configure("blueColor", foreground='blue')
    boxes[(x+1,y)].insert(END, currSec[1], )
    boxes[(x+1,y)].tag_add("center", '1.0', 'end')
    #boxes[(x+1,y)].tag_add("tmpp", '1.0', 'end')


    if 'tmpp' in boxes[(x-1,y)].tag_names():
        boxes[(x,y)].tag_add("tmpp", '1.0', 'end')
        boxes[(x+1,y)].tag_add("tmpp", '1.0', 'end')
    elif firstIter:
        boxes[(x,y)].tag_add("here", '1.0', 'end')
        boxes[(x+1,y)].tag_add("here", '1.0', 'end')
    else:
        boxes[(x,y)].tag_add("trueGreen", '1.0', 'end')
        boxes[(x+1,y)].tag_add("trueGreen", '1.0', 'end')

    #print(boxes[(x-1,y)].tag_names())

    ##    if currSec == '00':
    ##        boxes[(x,y)].tag_add("here", '1.0', 'end')
    ##        boxes[(x+1,y)].tag_add("here", '1.0', 'end')
    ##    else:
    ##        boxes[(x,y)].tag_add("tmpp", '1.0', 'end')
    ##        boxes[(x+1,y)].tag_add("tmpp", '1.0', 'end')

    if currSec == '59':
        #rand()
        root.after(1000, rand)
        print("runn")
        #root.after(0, rand)
        ###root.after(1500, fuck)
        #time.sleep(1.5)
        #sp = UpdateForMin()
        #root.after(500, runn, sp[0], sp[1])
    else:
        root.after(1000, runn, x, y, False)


##for i in timeStr:
##    boxes[(timeX,timeY)].delete(1.0)
##    #time.sleep(2)
##    boxes[(timeX,timeY)].tag_configure("blueColor", foreground='blue')
##    boxes[(timeX,timeY)].insert(END, i, )
##    boxes[(timeX,timeY)].tag_add("center", '1.0', 'end')
##    boxes[(timeX,timeY)].tag_add('purp', '1.0', 'end')
##    timeX += 1

##  boxes[(c,r)].tag_configure("purp", foreground= "#%02x%02x%02x" % (5,252,79))
##  boxes[(c,r)].tag_configure("here", foreground= "#%02x%02x%02x" % (81,103,193))

##  boxes[(c,r)].tag_add("here", "1.0", "1.4")



def FadeIn(box, currColor):
    currColor[0] -= 5
    currColor[1] += 10
    if currColor[2] > 79:
        currColor[2] -= 10
    box.tag_configure('tmpp', foreground = "#%02x%02x%02x" % tuple(currColor))
    box.tag_add('tmpp', '1.0', '1.4')
    if currColor[0] != 6:
        root.after(200, FadeIn, box, currColor)
    else:
        box.tag_delete('tmpp', '1.0', 'end')
        box.tag_add('trueGreen', '1.0', 'end')


sp = UpdateForMin()
root.after(1, runn, sp[0], sp[1], True)

root.mainloop()