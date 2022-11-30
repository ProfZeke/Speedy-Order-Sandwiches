#Provided by prof zeke and yilong musk
#Free Code For Speedy Order Sandwiches Payslip

import tkinter as tk
from tkinter import *
from tkinter import ttk
class Frames(object):
    def mainFrame(s, r):
        r.title('SANDWICHES YUMM')
        r.geometry("850x500")
        r.config(bg='gray')

        frame1=Frame(r,width=300,height=100,bg='gray',  
        highlightcolor="gray",highlightbackground="white",  
        highlightthickness=3).grid(padx = 260, pady = 160)
        
        lblinfo=Label(font=('arial',24,'bold','underline'),text="Speedy Order Sandwiches",bd=10,fg="Black", bg='gray')
        lblinfo.grid(row=0,column=0)
        lblinfo.place(x=230, y=10)
        n = Label(text ='What kind of sandwich do you like?', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'),bg='gray')
        n.place(x=320, y=100)
        s.sw=tk.StringVar()
        pc=ttk.Combobox(r, textvariable=s.sw)
        pc['values']= ('Hotdog','Burger','Club House')
        pc.place(x=350, y=120)
        n = Label(text ='Would you like fries with that?', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'), bg='gray')
        n.place(x=330, y=150)
        s.r = StringVar()
        a = Radiobutton(r, text='Yes', variable=s.r, value='A', bg='gray')
        a.place(x=340, y=185)
        b = Radiobutton(r, text='No', variable=s.r, value='B', bg='gray')
        b.place(x=440, y=185)
        c = Button(r, text="Compute", command=s.cp)
        c.place(x=400, y=450)
        cl = Button(r, text="Clear", command=s.cl)
        cl.place(x=360, y=450)
        s.var1 = IntVar()
        Checkbutton(r, text="Catsup", variable=s.var1, onvalue=1, offvalue=0, bg='gray').place(x=330,y=278)
        s.var2 = IntVar()
        Checkbutton(r, text="Mustard", variable=s.var2, onvalue=1, offvalue=0, bg='gray').place(x=400, y=278)
        s.var3 = IntVar()
        Checkbutton(r, text="Pickles", variable=s.var3, onvalue=1, offvalue=0, bg='gray').place(x=470, y=278)
        n = Label(text ='(Php 10.00)', anchor="e", justify=LEFT,
                  font=('Arial',7), bg='gray')
        n.place(x=330, y=300)
        n = Label(text ='(Php 12.00)', anchor="e", justify=LEFT,
                  font=('Arial',7), bg='gray')
        n.place(x=400, y=300)
        n = Label(text ='(Php 15.00)', anchor="e", justify=LEFT,
                  font=('Arial',7), bg='gray')
        n.place(x=470, y=300)
        s.r.set(None)
        s.ov=Entry(r)
        n = Label(text ='(Php 20.00)', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'), bg='gray')
        n.place(x=380, y=220)
        n = Label(text ='Condiments:', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'), bg='gray')
        n.place(x=240, y=280)
        n = Label(text ='Sizes:', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'), bg='gray')
        n.place(x=300, y=320)
        s.pa=tk.StringVar()
        pd=ttk.Combobox(r, textvariable=s.pa)
        pd['values']= ('Small','Medium','Large')
        pd.place(x=350, y=320)
        n = Label(text ='Amount Payable(12% VAT Included):', anchor="e", justify=LEFT,
                  font=('Arial',9,'bold'), bg='gray')
        n.place(x=240,y=350)
        s.ns = Entry(r)
        s.ns.place(x=450,y=350)

    def cp(s):
        sel = s.sw.get()
        print(sel)
        if sel =='Hotdog':
            p = 50
        elif sel =='Burger':
            p = 60
        elif sel =='Club House':
            p = 90
        if s.r.get()=='A':
            print('with fries +20')
            p+=20
        if s.var1.get()==1:
            print('with c')
            p+=10
        if s.var2.get()==1:
            print('with m')
            p+=12
        if s.var3.get()==1:
            print('with p')
            p+=15
        p*=1.12
        print(p)
        s.ns.delete(0, END)
        s.ns.insert(0,p)

    def cl(s):
        s.sw.set('')
        s.pa.set('')
        s.r.set(None)
        s.var1.set(0)
        s.var2.set(0)
        s.var3.set(0)
        print(s.sw.get())
        s.ns.delete(0, END)

r = Tk()
a = Frames()
a.mainFrame(r)
r.mainloop()
