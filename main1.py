from tkinter import *
from tkinter import ttk
from defs import*

#from defs import reading
hc=Rotronic()
root = Tk()
root.geometry("800x600")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)
memo = hc.get_humidity()
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
label = Label(frame, text='temp '+hc.get_temp())
label.pack()
szabel=Label(frame,text=memo)
szabel.pack()
root.title(f"HC2 - nr. ser: {hc.get_serial_number()}" )
root.update()



root.mainloop()


