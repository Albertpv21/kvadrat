from tkinter import *


aken=Tk()
aken.title("Какулятор квадратного уравнения")
aken.geometry("400x400")
nupp=Button(aken,font="Arial 10",fg="black",bg="green",height=2,width=8,relief=GROOVE,text="Решить")#relief RAISED,SUNKEN
txt=Entry(aken,width=5,font="Arial 20",fg="black",bg="green",justify=CENTER)
txt1=Entry(aken,width=5,font="Arial 20",fg="black",bg="green",justify=CENTER)
txt2=Entry(aken,width=5,font="Arial 20",fg="black",bg="green",justify=CENTER)










nupp.pack(side=RIGHT,padx=10,pady=20)#side=LEFT,TOP,RIGHT
txt.pack(side=LEFT,padx=10,pady=15)
txt1.pack(side=BOTTOM,padx=10,pady=15)

aken.mainloop()
