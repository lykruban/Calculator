from cProfile import label
import tkinter as tk
from tkinter import *
strips ={0:'black',1:'brown',2:'red',3:'orange',4:'yellow',5:'green',6:'blue',7:'violet',8:'grey',9:'white','5%':'golden','10%':'silver'}

stripall= []
x=[]
def runresult():
    x.append(1)
    print(len(x))

    if len(x)==5:
        execfile('main.py')

    elif len(stripall)==4:
        if type(stripall[3])==str:
            sum=((stripall[0]*10)+stripall[1])*((10**stripall[2]))
            answer=[sum,'Ω',stripall[3]]
            if stripall[2]>2:
                sum=sum/1000
                ans=[sum,'kΩ',stripall[3]]
                text1_Input.set(ans)
            else:
                text1_Input.set(answer)

        else:
            text1_Input.set('The 4th value must \n be Gold or Silver')
    elif len(stripall)==5:
        if type(stripall[4])==str:
            sum=((stripall[0]*100)+(stripall[1]*10)+stripall[2])*((10**stripall[3]))
            answer=[sum,'Ω',stripall[4]]
            if stripall[3]>2:
                sum=sum/1000
                ans=[sum,'kΩ',stripall[4]]
                text1_Input.set(ans)
            else:
                text1_Input.set(answer)
        else:
            text1_Input.set('The 5th value must \n be Gold or Silver')
    elif len(stripall)<4:
        text1_Input.set('Put in more values')
    else:
        text1_Input.set('Too many values')


def deletevalue():
    x.clear()
    p=len(stripall)-1
    if p>=0:
        text1_Input.set(p)
        stripall.pop(p)
        text_Input.set(stripall)
    else:
        text1_Input.set('ADD COLOR')

def on_click(x,y):
    if len(stripall)<=5:
        text1_Input.set(y)
        stripall.append(x)
        text_Input.set(stripall)
    else:
        text1_Input.set('too many values')

root=tk.Tk()
root.geometry('570x600')    
root.resizable(False, False)
root.configure(bg='#A3C2C0')
root.title('resistance calculator by ruban and ethan')
text1_Input=StringVar()
text1_Input.set("START")
text_Input=StringVar()
text_Input.set('values')

label = tk.Label(root,width=25,height=2,font=('arial',30) ,bg='#53D1C8',textvariable=text1_Input)
label.pack(pady=20)
Label(root,width=7,height=2,font=('arial',30) ,bg='#53D1C8',textvariable=text_Input).place(x=190,y=490)



Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='black',
    text='BLACK',
    command=lambda: [on_click(0,'Black')]).place(x=10,y=130)
     
Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#6D4343',
    text='BROWN',
    command=lambda: [on_click(1,'Brown')]).place(x=190,y=130)

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#DD3838',
    text='RED',
    command=lambda: [on_click(2,'Red')]).place(x=370,y=130)
     
Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#DF592B',
    text='ORANGE',
    command=lambda: [on_click(3,'Orange')]).place(x=10,y=220)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#F0DF10',
    text='YELLOW',
    command=lambda: [on_click(4,'Yellow')]).place(x=190,y=220)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#50C135',
    text='GREEN',
    command=lambda: [on_click(5,'GREEN')]).place(x=370,y=220)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='blue',
    text='BLUE',
    command=lambda: [on_click(6,'Blue')]).place(x=10,y=310)
     


Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#A213DC',
    text='VIOLET',
    command=lambda: [on_click(7,'Violet')]).place(x=190,y=310)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#909090',
    text='GREY',
    command=lambda: [on_click(8,'Grey')]).place(x=370,y=310)
     


Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#000',bg='#FFFFFF',
    text='WHITE',
    command=lambda: [on_click(9,'White')]).place(x=190,y=400)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#FFD700',
    text='GOLD',
    command=lambda: [on_click("5%",'Gold')]).place(x=10,y=400)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#C0C0C0',
    text='SILVER',
    command=lambda: [on_click("10%",'Silver')]).place(x=370,y=400)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E4053',
    text='RUN',
    command=lambda: [runresult()]).place(x=370,y=490)
     

Button(
    root,
    width=7,height=1,font=('arial',30,'bold'),bd=1,fg='#fff',bg='#2E4053',
    text='Delete',
    command=lambda: [deletevalue()]).place(x=10,y=490)


root.mainloop()