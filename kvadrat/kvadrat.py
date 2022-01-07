from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
global a_val,b_val,c_val,D_,graf
graf=False
def res():
    global a_val,b_val,c_val,D_,t,graf
    if (a_val.get()!="" and b_val.get()!="" and c_val.get()!=""):
        a_=float(a_val.get())
        b_=float(b_val.get())
        c_=float(c_val.get())
        D_=b_*b_-4*a_*c_
        if D_>=0:
            x1=round((-b_+sqrt(D_))/(2*a_),2)
            x2=round((-b_-sqrt(D_))/(2*a_),2)
            t=f"X1={x1},\nX2={x2}"
            graf=True
        if D_==0:
            x1=round((-b_+sqrt(D_))/(2*a_),2)
            t="x1=%s\n"%(D_,x1,x2)
            graf=True
        else:
            t="D=%s \n Это уравнение не имеет корней" % D_
            a_val.configure(bg="lightblue")
            b_val.configure(bg="lightblue")
            c_val.configure(bg="lightblue")
            lbl4.configure(text=f"D={D_}\n{t}")
    else:
        if a_val.get()=="":
            a_val.configure(bg="red")
        else:
            a_val.configure(bg="lightblue")
        if b_val.get()=="":
            b_val.configure(bg="red")
        else:
            b_val.configure(bg="lightblue")
        if c_val.get()=="":
            c_val.configure(bg="red")
        else:
            c_val.configure(bg="lightblue")
    return graf,D_,t
def ins(event):
    output.delete("0.0",END)
    output.insert("0.0",value)

def dop(event):
    try:
        a_val=float(a.get())
        b_val=float(b.get())
        c_val=float(c.get())
        inserter(res(a_val,b_val,c_val))
    except ValueError:
        inserter("Убедитесь что ввели 3 числа")
def graafik(event):
    graf,D_,text=res()
    if graf==True:
        a_=float(a_val.get())
        b_=float(b_val.get())
        c_=float(c_val.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0*+b_*x0+c_
        x=np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,"b:o",x0,y0,"r-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина параболы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
        lbl4.configure(text=f"D={D}\n{t}\n{text}")


aken=Tk()
aken.title("Какулятор квадратного уравнения")
aken.geometry("500x300")
nupp=Button(aken,font="Arial 9",fg="black",bg="green",height=2,width=10,relief=GROOVE,text="Решить",command=res)
a_val=Entry(aken,width=4,font="Arial 18",fg="black",bg="lightblue",justify=CENTER)
b_val=Entry(aken,width=4,font="Arial 18",fg="black",bg="lightblue",justify=CENTER)
c_val=Entry(aken,width=4,font="Arial 19",fg="black",bg="lightblue",justify=CENTER)
lbl=Label(aken,text="Решение квадратного уравнения",font="Arial 13",bg="lightblue",fg="green")
lbl1=Label(aken,text="x**2+",font="Arial 19",fg="green")
lbl2=Label(aken,text="x+",font="Arial 19",fg="green")
lbl3=Label(aken,text="=0",font="Arial 19",fg="green")
lbl4=Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")
lbl5=Button(aken,width=5,text="График",font="Arial 20",fg="Black",bg="yellow")






lbl5.place(x=20,y=200)
lbl3.place(x=300,y=80)
lbl2.place(x=195,y=80)
lbl1.place(x=60,y=80)
lbl.place(x=130,y=30)
nupp.place(x=340,y=72,height=60)
a_val.place(x=10,y=80,height=35)
b_val.place(x=135,y=81,height=35)
c_val.place(x=230,y=81,height=35)
lbl4.place(x=30,y=120)
lbl5.bind("<Button-1>",graafik)
r1=Radiobutton(aken,text="Кит")
r2=Radiobutton(aken,text="Очки")





aken.mainloop()
