from tkinter import *
from random import randint, choice
from datetime import datetime

# REMEMBER:
# X = Columns
# Y = Rows

ROWS = 13
COLUMNS = 25
TEXTBOX_BACKGROUND = (0, 34, 64)  # dark blue (r, g, b)
TEXT_BLUE = (81, 103, 193)  # light blue (r, g, b)
TEXT_GREEN = (6, 253, 73)  # green (r, g, b)

# instantiate tkinter (creates main window)
root = Tk()

# specify size of window, currently set to full screen,
# but the following can be used specify a different size: root.geometry("2000x1000")
root.attributes('-fullscreen', 1)

# the following was originally meant to "configure" the grid,
# the following commented out lines (1 and 2) are meant to add "weight"
# to the grid so that you can control the space between widgets on the screen,
# but I don't think it's necessary since I want all the widgets to touch and
# fill the screen, which I believe is done by default
#
# EDIT: so apparently this makes sure that everything stays on the screen with no overflow
r = 0
c = 0
for i in range(COLUMNS):
    if i < 13:
        root.rowconfigure(r, weight=1)  # 1
        r += 1

    root.columnconfigure(c, weight=1)  # 2
    c += 1

# the textboxes are kept in a dictionary where the textbox grid index is the key and the textbox
# is the value. the following loop will create all the textboxes, add the tags, fills it with a random
# character, and adds it to the grid
r = 0
c = 0
boxes = {}
for i in range(ROWS*COLUMNS):
    if c == COLUMNS:
        c = 0
        r += 1

    boxes[(c, r)] = Text(root, relief=RIDGE, height=1, width=2, bg="#%02x%02x%02x" % TEXTBOX_BACKGROUND)
    boxes[(c, r)].config(font="Consolas 50")
    boxes[(c, r)].tag_configure("center", justify='center')
    boxes[(c, r)].tag_configure("lightBlue", foreground="#%02x%02x%02x" % TEXT_BLUE)
    boxes[(c, r)].tag_configure("green", foreground="#%02x%02x%02x" % TEXT_GREEN)

    boxes[(c, r)].insert(END, chr(randint(48, 122)), )

    boxes[(c, r)].tag_add("center", '1.0', 'end')
    boxes[(c, r)].tag_add("lightBlue", "1.0", "1.4")

    boxes[(c, r)].grid(row=r, column=c)
    c += 1

# this function gets the current time/date info and chooses the random position
# that they will be placed in
def UpdatePositions():
    now = datetime.now()
    hour = now.strftime("%I")
    mins = now.strftime("%M")
    sec = now.strftime("%S")
    AmPm = now.strftime("%p")
    day = now.strftime("%A")
    month = now.strftime("%B")
    monthDay = now.strftime("%d")
    year = now.strftime("%Y")

    # since time/date are generated at random positions, i needed an easy way to keep
    # track of the "filled" positions to avoid overwriting anything, so i just used
    # a list to keep track of the free rows. freeRowsDate is just used for choosing
    # a date location because i needed more control/conditions to keep spacing the
    # way i wanted
    freeRows = [x for x in range(1, 11)]
    freeRowsDate = [x for x in range(1, 11)]

    # choose the time position
    timeStr = f'{hour}:{mins}:{sec}'
    timeX = randint(1,15)
    timeY = randint(1,10)
    freeRows.remove(timeY)
    freeRowsDate.remove(timeY)
    if timeY-1 in freeRows:
        freeRows.remove(timeY-1)
        freeRowsDate.remove(timeY-1)
    if timeY+1 in freeRows:
        freeRows.remove(timeY+1)
        freeRowsDate.remove(timeY+1)
    if timeY+2 in freeRows:
        freeRows.remove(timeY+2)
        freeRowsDate.remove(timeY+2)
    if timeY-2 in freeRowsDate:
        freeRowsDate.remove(timeY-2)

    # choose the date position
    dateStr = f'{month} {monthDay}'
    dateXEnd = 23 - len(dateStr)
    dateX = randint(1, dateXEnd)
    dateY = choice(freeRowsDate)
    freeRows.remove(dateY)
    if dateY-1 in freeRows:
        freeRows.remove(dateY-1)
    if dateY+1 in freeRows:
        freeRows.remove(dateY+1)
    if dateY+2 in freeRows:
        freeRows.remove(dateY+2)

    # choose the day of the week position
    dayXEnd = 23 - len(day)
    dayX = randint(1, dayXEnd)
    if 10 in freeRows:
        freeRows.append(11)
    dayY = choice(freeRows)

    # updates the time textboxes
    for i in timeStr:
        UpdateTextBox(timeX, timeY, i)
        root.after(400, FadeIn, boxes[(timeX, timeY)], list(TEXT_BLUE))
        timeX += 1

    # marks the position of the seconds textbox, which will be returned
    # so the seconds can be updated continuously
    secPos = (timeX-2, timeY)

    # updates the AM/PM textboxes
    timeX -= 8
    timeY += 1
    for i in AmPm:
        UpdateTextBox(timeX, timeY, i)
        root.after(400, FadeIn, boxes[(timeX, timeY)], list(TEXT_BLUE))
        timeX += 1

    # updates the date textboxes
    for i in dateStr:
        if i != ' ':
            UpdateTextBox(dateX, dateY, i)
            root.after(1200, FadeIn, boxes[(dateX, dateY)], list(TEXT_BLUE))
        dateX += 1

    # updates the year textboxes
    dateX -= 4
    dateY += 1
    for i in year:
        UpdateTextBox(dateX, dateY, i)
        root.after(1200, FadeIn, boxes[(dateX, dateY)], list(TEXT_BLUE))
        dateX += 1

    # updates the weekday textboxes
    for i in day:
        UpdateTextBox(dayX, dayY, i)
        root.after(800, FadeIn, boxes[(dayX, dayY)], list(TEXT_BLUE))
        dayX += 1

    return secPos

# updates textboxes
def UpdateTextBox(x, y, char):
    boxes[(x, y)].delete(1.0)
    boxes[(x, y)].insert(END, char, )
    boxes[(x, y)].tag_add("center", '1.0', 'end')
    boxes[(x, y)].tag_add("lightBlue", '1.0', 'end')

# fades TEXT_BLUE to TXT_GREEN
def FadeIn(box, currColor):
    currColor[0] -= 5
    currColor[1] += 10
    if currColor[2] > 79:
        currColor[2] -= 10
    box.tag_configure('tmp', foreground="#%02x%02x%02x" % tuple(currColor))
    box.tag_add('tmp', '1.0', '1.4')
    if currColor[0] != 6:
        root.after(200, FadeIn, box, currColor)
    else:
        box.tag_delete('tmp', '1.0', 'end')
        box.tag_add("green", '1.0', 'end')

# get the positions of the seconds textboxes and calls a function
# to start updating them
def GetNSendSecPos():
    pos = UpdatePositions()
    root.after(0, UpdateSeconds, pos[0], pos[1], True)

# updates textboxes for screen refresh
def Stagger(x, y, resetNum):
    boxes[(x, y)].delete(1.0)
    boxes[(x, y)].insert(END, chr(randint(48, 122)), )
    boxes[(x, y)].tag_add("center", '1.0', 'end')
    boxes[(x, y)].tag_add("lightBlue", "1.0", "1.4")
    if x == 24 and y == 12 and resetNum == 3:
        root.after(0, GetNSendSecPos())

# causes all textboxes to reset several times to get the
# desired visual effect
def RefreshScreen():
    for x in range(4):
        for y in boxes:
            factor = randint(0, 5)

            # this is here to keep track of the last box to rest,
            # so that you know when the refresh process is over
            # so you can generate time/date again
            if y[0] == 24 and y[1] == 12 and x == 3:
                root.after(500, Stagger, y[0], y[1], x)
            else:
                root.after(factor*100, Stagger, y[0], y[1], x)

# updates the seconds
# afterRefresh isa bool used to know if the function was just called after
# a screen refresh, if so the text color needs to be set to "lightBlue"
def UpdateSeconds(x, y, afterRefresh):

    rn = datetime.now()
    currSec = rn.strftime("%S")

    boxes[(x, y)].delete(1.0)
    boxes[(x, y)].insert(END, currSec[0], )
    boxes[(x, y)].tag_add("center", '1.0', 'end')

    boxes[(x+1, y)].delete(1.0)
    boxes[(x+1, y)].insert(END, currSec[1], )
    boxes[(x+1, y)].tag_add("center", '1.0', 'end')

    if 'tmp' in boxes[(x-1, y)].tag_names():
        boxes[(x, y)].tag_add("tmp", '1.0', 'end')
        boxes[(x+1, y)].tag_add("tmp", '1.0', 'end')
    elif afterRefresh:
        boxes[(x, y)].tag_add("lightBlue", '1.0', 'end')
        boxes[(x+1, y)].tag_add("lightBlue", '1.0', 'end')
    else:
        boxes[(x, y)].tag_add("green", '1.0', 'end')
        boxes[(x+1, y)].tag_add("green", '1.0', 'end')

    if currSec == '59':
        root.after(1000, RefreshScreen)
    else:
        root.after(1000, UpdateSeconds, x, y, False)


# main
sp = UpdatePositions()
root.after(0, UpdateSeconds, sp[0], sp[1], True)
root.mainloop()