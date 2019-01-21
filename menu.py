from tkinter import *
win = Tk()
win.title("Menu App")
win.geometry('280x280')
#functions
def new():
    labl.configure(text="Newfile Clicked")
    submenu1.entryconfig("New", state='disabled')
#Main Menu Points
menu1 = Menu(win)
submenu1 = Menu(menu1,tearoff=0)
submenu2 = Menu(menu1)
submenu3 = Menu(menu1,tearoff=0)
subsubmenu1 = Menu(menu1,tearoff=0)
menu1.add_cascade(label='File', menu=submenu1)
menu1.add_cascade(label='Edit', menu=submenu2)
menu1.add_cascade(label='Help', menu=submenu3)
    # File Menu
submenu1.add_command(label='New',command=new)
submenu1.add_command(label='Open')
submenu1.add_separator()
        # Settings Cascade Ready
submenu1.add_cascade(label='Settings', menu=subsubmenu1)
subsubmenu1.add_command(label='settting1')
subsubmenu1.add_command(label='settting2')
subsubmenu1.add_separator()
subsubmenu1.add_command(label='settting3')

submenu1.add_separator()
submenu1.add_command(label='Exit',command=exit)
    #Edit Menu
submenu2.add_command(label='Copy', state= 'disabled')
submenu2.add_command(label='Paste')
submenu2.add_command(label='Cut', state= 'normal')
submenu2.add_separator()
submenu2.add_command(label='Find')
    #Help Menu
submenu3.add_command(label='Welcome')
submenu3.add_command(label='Tips')
submenu3.add_command(label='Updates')
submenu3.add_command(label='License')
submenu3.add_separator()
submenu3.add_command(label='About')

labl=Label(win,text="Welcome")
labl.grid(column=0,row=1)
win.config(menu=menu1)

win.mainloop()