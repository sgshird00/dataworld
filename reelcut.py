from tkinter import *


def rc():
    h = float(hent.get())
    l = float(lent.get())
    w = float(went.get())
    if fent.get() == "":
        f = 25.4
    else:
        f = float(fent.get())
    reel.configure(text=f'REEL Size: {(h+w)/f}')
    cut.configure(text=f'CUT Size: {(((l+w)*2)+50)/f}')


win = Tk()
win.title('KS Packaging Reel Cut Formula')
win.geometry('400x300')
title = Label(
    win, text='Welcome\nEnter the corresponding\nheight, width, length and\n formula value if changed:').grid(column=0, row=0)
a1 = Label(win, text='*Height: ').grid(column=0, row=4)
hent = Entry(win, width=8)
hent.grid(column=1, row=4)
hent.focus()
a1 = Label(win, text='*Length: ').grid(column=0, row=5)
lent = Entry(win, width=8)
lent.grid(column=1, row=5)
a1 = Label(win, text='*Width: ').grid(column=0, row=6)
went = Entry(win, width=8)
went.grid(column=1, row=6)
a1 = Label(win, text='Formula(DEFAULT- 25.4): ').grid(column=0, row=7)
fent = Entry(win, width=8)
fent.grid(column=1, row=7)
rsz = Button(win, text='Result', command=rc,bg='black',fg='white').grid(column=1, row=9)
reel = Label(win, text='')
reel.grid(column=0, row=11)
cut = Label(win, text='')
cut.grid(column=0, row=12)
win.mainloop()
