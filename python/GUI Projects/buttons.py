from tkinter import *


root=Tk()
def myClick():
    myLabel=Label(root, text="Look! I created a blue button!")  #fg="blue",bg="yellow"
    myLabel.pack()

myButton=Button(root,text="Click Me!",command=myClick)  #state=DISABLED padx=10 pady=10
myButton.pack()


root.mainloop()
