import tkinter


w = tkinter.Tk()

myTitle = tkinter.Label(w, text='make it run')
myTitle.pack()


def main():
    b1 = tkinter.Button(w,text = '1',command = 'main')
    b1.pack()
    b2 = tkinter.Button(w,text = '2',command = 'main')
    b2.pack()
run = tkinter.Button(w,text = 'Press the button to run',command = 'main')
run.pack()
w.mainloop()