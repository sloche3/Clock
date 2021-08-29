from tkinter import *
from random import randint

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

        boxes[(c,r)] = Text(root, height = 1, width = 2)
        #print((c,r))
        #boxes[i] = Text(root)
        boxes[(c,r)].config(font = "Consolas 50")
        boxes[(c,r)].tag_configure("center", justify='center')
        boxes[(c,r)].insert(END, str(randint(0, 9)), )
        boxes[(c,r)].tag_add("center", '1.0', 'end')

        boxes[(c,r)].grid(row = r, column = c)
        c += 1
    else:
        c = 0
        r += 1

        boxes[(c,r)] = Text(root, height = 1, width = 2)
        #print((c,r))
        #boxes[i] = Text(root)
        boxes[(c,r)].config(font = "Consolas 50")
        boxes[(c,r)].tag_configure("center", justify='center')
        boxes[(c,r)].insert(END, str(randint(0, 9)), )
        boxes[(c,r)].tag_add("center", '1.0', 'end')

        boxes[(c,r)].grid(row = r, column = c)
        c += 1


def gogo(x, y):
    boxes[(x,y)].delete(1.0)
    #time.sleep(2)
    boxes[(x,y)].insert(END, str(randint(0, 9)), )
    boxes[(x,y)].tag_add("center", '1.0', 'end')

def rand():
    for x in range(3):
        for y in boxes:
            factor = randint(0,5)
            wait = (factor * 100) + 3000
            root.after(wait, gogo, y[0], y[1])
        #time.sleep(0.001)

root.after(1000, rand)

#mainloop()



