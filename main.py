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
for i in range(325):
    boxes[i] = Text(root, height = 1, width = 2)
    #boxes[i] = Text(root)
    boxes[i].config(font = "Consolas 50")
    boxes[i].tag_configure("center", justify='center')
    boxes[i].insert(END, str(randint(0, 9)), )
    boxes[i].tag_add("center", '1.0', 'end')
    if c < 25:
        boxes[i].grid(row = r, column = c)
        c += 1
    else:
        c = 0
        r += 1
        boxes[i].grid(row = r, column = c)
        c += 1

#mainloop()



