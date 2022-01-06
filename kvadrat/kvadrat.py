from math import sqrt
from tkinter import *
def solver(a,b,c):
    D=b*b-4*a*c
    if D>=0:
        x1=(-b+sqrt(D))/(2*a)
        x1=(-b-sqrt(D))/(2*a)
        text="D=%s\n x1=s% \n"%(D,x1,x2)
    else:
        text="D=%s \n Это уравнение не имеет корней" % D
        return text
def inserter():
    output.delete("0.0",END)
    output.insert("0.0",value)

def handler():
    try:
        a_val=float(a.get())
        b_val=float(b.get())
        c_val=float(c.get())
        inserter(solver(a_val,b_val,c_val))
    except ValueError:
        inserter("Убедитесь что ввели 3 числа")




aken=Tk()
aken.title("Какулятор квадратного уравнения")
aken.geometry("500x300")
nupp=Button(aken,font="Arial 9",fg="black",bg="green",height=2,width=10,relief=GROOVE,text="Решить")
a=Entry(aken,width=4,font="Arial 18",fg="black",bg="lightblue",justify=CENTER)
b=Entry(aken,width=4,font="Arial 18",fg="black",bg="lightblue",justify=CENTER)
c=Entry(aken,width=4,font="Arial 19",fg="black",bg="lightblue",justify=CENTER)
lbl=Label(aken,text="Решение квадратного уравнения",font="Arial 13",bg="lightblue",fg="green")
lbl1=Label(aken,text="x**2+",font="Arial 19",fg="green")
lbl2=Label(aken,text="x+",font="Arial 19",fg="green")
lbl3=Label(aken,text="=0",font="Arial 19",fg="green")
lbl4=Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")






lbl3.place(x=300,y=80)
lbl2.place(x=195,y=80)
lbl1.place(x=60,y=80)
lbl.place(x=130,y=30)
nupp.place(x=340,y=72,height=60)
a.place(x=10,y=80,height=35)
b.place(x=135,y=81,height=35)
c.place(x=230,y=81,height=35)
lbl4.place(x=30,y=120)
nupp.bind("<Button-1>",solver)


aken.mainloop()
