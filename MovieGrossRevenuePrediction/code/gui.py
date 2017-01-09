import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
"""
B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

var = StringVar()
label = Message( top, textvariable=var, relief=RAISED )

var.set("enter budget")
label.pack()

B.pack()
"""

L1 = Label(top, text="Budget")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)



top.mainloop()