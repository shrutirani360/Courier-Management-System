import sqlite3              
from tkinter import *
from datetime import datetime

def register():
    ext=Tk()
    ext.title("SIGN UP")
    l5=Label(ext,text="REGISTRATION",fg="yellow",bg="black")
    l5.grid(row=0,column=0,padx=130,pady=40)
    l6=Label(ext,text="Name")
    l6.grid(row=2,column=0)
    l7=Label(ext,text="Phone Number")
    l7.grid(row=3,column=0)
    I8=Label(ext,text="SETUP A PASSWORD",fg="yellow",bg="black")
    I8.grid(row=4,column=0,padx=130,pady=40)
    I9=Label(ext,text="Registration No.")
    I9.grid(row=5,column=0,pady=5)
    I10=Label(ext,text="Password")
    I10.grid(row=6,column=0)
    Name=StringVar()
    Phone_no=StringVar()
    Registration_no=StringVar()
    Password=StringVar()
    e3=Entry(ext,bg="white",textvariable=Name)
    e4=Entry(ext,bg="white",textvariable=Phone_no)
    e5=Entry(ext,bg="white",textvariable=Registration_no)
    e6=Entry(ext,bg="white",textvariable=Password)
    e3.grid(row=2,column=1,pady=5)
    e4.grid(row=3,column=1)
    e5.grid(row=5,column=1)
    e6.grid(row=6,column=1)
    b4=Button(ext,text="Submit",fg="yellow",bg="black",width=10,height=2,command=lambda:[f1(),sign_in()])
    b4.grid(row=8,column=1,padx=50,pady=10)
    def f1():
        a=e3.get()
        b=e4.get()
        global c
        c=e5.get()
        global d
        d=e6.get()
        conn=sqlite3.connect('CMS_DB.db')
        conn.cursor()
        conn.execute('CREATE table if not exists CMS(Name text,Phone_Number real,Registration_No real,password text)');
        conn.execute('insert into CMS(Name,Phone_Number,Registration_No,Password)Values(?,?,?,?)',(a,b,c,d))
        conn.commit()
  
def sign_in():
    ent=Tk()
    ent.title("SIGN IN") 
    l1=Label(ent,text="LOGIN PAGE",fg="yellow",bg="black")
    l1.grid(row=0,column=0,padx=100,pady=50)
        
    l2=Label(ent,text="Registration Number")
    l2.grid(row=2,column=0)
    l3=Label(ent,text="Password")
    l3.grid(row=3,column=0)
    Registration_No=StringVar()
    Password=StringVar()
    e7=Entry(ent,bg="white",textvariable=Registration_No)
    e8=Entry(ent,bg="white",textvariable=Password)
    e7.grid(row=2,column=1,padx=50,pady=5)
    e8.grid(row=3,column=1,padx=50,pady=5)
    def database():
        e=e7.get()
        f=e8.get()
       

    b3=Button(ent,text="Submit",fg="Yellow",bg="Black",width=10,height=1,command=lambda:[database(),after_enter(ent)])
    b3.grid(row=4,column=1,padx=30,pady=30)



def after_enter(ent):
	ent.destroy()
	from tkinter import messagebox
	message=messagebox.showinfo("Logged In Successfully")
	ext1=Tk()
	l11=Label(ext1,text="Enter The Track Consignment Number",fg="black")
	l11.grid(row=1,column=4,padx=30,pady=5)
	entrty=Entry(ext1)
	entrty.grid(row=1,column=10)
	b4=Button(ext1,text="Submit",fg="yellow",bg="Black",width=10,height=2,command=lambda:[Msg(ext1)])
	b4.grid(row=2,column=2,padx=10,pady=10)

def Msg(ext1):
	ext1.destroy()
	axt=Tk()
	l12=Label(axt,text="COLLECT YOUR COURIER FROM OFFICE..!!!",fg="black",bg="white")                
	l12.grid(row=1,column=1,padx=20,pady=10)


cms=Tk()
cms.title("HOME PAGE")
b1=Button(cms,text="Sign In",bd=5,fg="yellow",bg="black",width=50,height=2,command=sign_in)
b1.grid(row=0,column=0,padx=200,pady=20)

b2=Button(cms,text="Sign Up",bd=5,fg="yellow",bg="black",width=50,height=2,command=register)
b2.grid(row=0,column=1,padx=100,pady=20)

cms.mainloop()

