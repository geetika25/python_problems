#calculator : program to illustrate calculator,this is my first gui program in python
#import tkinder library
from tkinter import *
#function defination here (click)
def btnClick(numbers):
 global operator
 operator=operator+str(numbers)
 text_Input.set(operator)

#function defination(clear function)
def btnClear():
 global operator
 operator=""
 text_Input.set("")
#function defination (equal function)
def btnEquals() :
 global operator
 sumup=str(eval(operator))
 text_Input.set(sumup)
 operator= ""
#constractor
cal=Tk()
#tittle method
cal.title("calculator")
operator=''
#to store the operator as string
text_Input= StringVar()
textDisplay = Entry(cal,font=("arial",20,'bold'),textvariable=text_Input,bd=30,insertwidth=3,bg='white',justify='right').grid(columnspan=4)
#number of bottons in the calculator
#button 7
button7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='7',command=lambda:btnClick(7))
button7.grid(row=1,column=0)
#botton 8
button8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='8',command=lambda:btnClick(8))
button8.grid(row=1,column=1)
#botton 9
button9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='9',command=lambda:btnClick(9))
button9.grid(row=1,column=2)
#botton add
buttonAdd=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='+',command=lambda:btnClick("+"))
buttonAdd.grid(row=1,column=3)
#botton 4
button4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='4',command=lambda:btnClick(4))
button4.grid(row=2,column=0)
#botton 5
button5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='5',command=lambda:btnClick(5))
button5.grid(row=2,column=1)
#botton 6
button6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='6',command=lambda:btnClick(6))
button6.grid(row=2,column=2)
#botton -
buttonSub=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='-',command=lambda:btnClick("-"))
buttonSub.grid(row=2,column=3)
#botton 1
button1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='1',command=lambda:btnClick(1))
button1.grid(row=3,column=0)
#botton 2
button2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='2',command=lambda:btnClick(2))
button2.grid(row=3,column=1)
#botton 3
button3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='3',command=lambda:btnClick(3))
button3.grid(row=3,column=2)
#botton *
buttonMul=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='*',command=lambda:btnClick("*"))
buttonMul.grid(row=3,column=3)
#botton 0
button0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='0',command=lambda:btnClick(0))
button0.grid(row=4,column=0)
#botton clr
buttonClr=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='clr',command=btnClear)
buttonClr.grid(row=4,column=1)
#botton equ
buttonEqu=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='=',command=btnEquals)
buttonEqu.grid(row=4,column=2)
#botton /
buttonDiv=Button(cal,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text='/',command=lambda:btnClick("/"))
buttonDiv.grid(row=4,column=3)
cal.mainloop()