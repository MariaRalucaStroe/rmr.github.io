from tkinter import *

root=Tk()

myLabel1=Label(root,text="Hello and welcome!")
myLabel2=Label(root,text="I am creating my first grid in Python.")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()
