from tkinter import Tk,Label,Button,Entry

def func():
    e.get()
    f=int(e.get())*9/5+32
    l=Label(r,text='temp in celc is'+str(f))
    l.pack()





r=Tk()
l=Label(r,text='enter temp in farhen')
l.pack()
e=Entry(r)
e.pack()
b=Button(r,text="enter",command=func)
b.pack()
r.mainloop()
