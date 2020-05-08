from tkinter import *
from tkinter import messagebox
import random
wn=Tk()
wn.title('rock paper scissor game made by Ishanth')
wn.geometry('280x280')
wn.configure(background='light grey')
def game ():
    var=StringVar()
    var1=StringVar()
    var2=IntVar()
    var3=IntVar()
    wn2=Toplevel(wn)
    wn2.geometry('280x280')
    wn2.title('rock paper scissor game made by Ishanth')
    wn2.configure(background='light grey')


    def OnButtonClick (Buttonid):
        if (Buttonid==1):
            var.set('Rock')
        elif (Buttonid==2):
            var.set('Paper')
        else:
            var.set('Scissor')
        compAI=random.randint(1,3)
        if (compAI==1):
            var1.set('Rock')
        elif (compAI==2):
            var1.set('Paper')
        else:
            var1.set('Scissor')
        if (var.get()=='Rock'and var1.get()=='Scissor'):
            var2.set(var2.get()+1)
        if (var.get()=='Rock'and var1.get()=='Paper'):
            var3.set(var3.get()+1)
        if (var.get()=='Scissor'and var1.get()=='Rock'):
            var3.set(var3.get()+1)
        if (var.get()=='Scissor'and var1.get()=='Paper'):
            var2.set(var2.get()+1)
        if (var.get()=='Paper'and var1.get()=='Scissor'):
            var3.set(var3.get()+1)
        if (var.get()=='Paper'and var1.get()=='Rock'):
            var2.set(var2.get()+1) 


    def f ():
        if (var2.get()==var3.get()):
            messagebox.showinfo('TIE!','Nobody won')
            var2.set(0)
            var3.set(0)               
        elif (var2.get()>var3.get()):
            messagebox.showinfo('Success','you won')
            var2.set(0)
            var3.set(0)
        else:
            messagebox.showerror('Failure','you lost')
            var2.set(0)
            var3.set(0)


    Label(wn2,text='User',).place(x=40,y=20,width=50,height=20)
    Label(wn2,text='Python AI',).place(x=150,y=20,width=90,height=20)


    Entry(wn2,textvariable=var).place(x=40,y=70,width=50,height=20)
    Label(wn2,text='V/S',font='Helvetica 10 bold').place(x=110,y=15,width=30,height=20)
    Entry(wn2,textvariable=var1).place(x=170,y=70,width=50,height=20)


    
    Entry(wn2,textvariable=var2).place(x=40,y=140,width=50,height=20)
    var2.set(0)
    Entry(wn2,textvariable=var3).place(x=170,y=140,width=50,height=20)
    var3.set(0)

    Button(wn2,text='ROCK',command=lambda:OnButtonClick(1)).place(x=40,y=170,width=50,height=20)
    Button(wn2,text='PAPER',command=lambda:OnButtonClick(2)).place(x=90,y=170,width=50,height=20)
    Button(wn2,text='SCISSOR',command=lambda:OnButtonClick(3)).place(x=140,y=170,width=60,height=20)

    Button(wn2,text='Done',command=f).place(x=40,y=210,width=50,height=20)
    Button(wn2,text='Exit',command=wn2.destroy).place(x=90,y=210,width=50,height=20)

       
       
                
Button(wn,text='exit',font='Helvetica 10 bold',command=wn.destroy).place(x=40,y=20,width=80,height=30)
Button(wn,text='play',font='Helvetica 10 bold',command=game).place(x=150,y=20,width=80,height=30)
wn.mainloop()





























