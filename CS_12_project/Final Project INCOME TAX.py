# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:06:06 2020

@author: gkuma
"""

import tkinter
import csv
from tkinter import ttk
def makelabel(name,window,text,font,row,column,size=15):  #function to make labels
    name=tkinter.Label(window,text=str(text),font=(str(font),size))
    name.grid(column=int(column),row=int(row))

#
def back():
    exit2()
    a1()
pass1={}

#display tax records
def taxdatabase():
    f2=open('details.csv','r')
    x=csv.reader(f2)
    records=list(x)
    print(records)
    recordmatch=[]
    c=True
    pannum1=pannum.get()
    if len(pannum1)==10 and pannum1[0:4].isalpha()==True and pannum1[5:8].isnumeric()==True and pannum1[9].isalpha()==True:
        pass
    else:
        tkinter.messagebox.showerror('ERROR','Enter Valid PAN Number')
        c=False
    if c==True:
       # makelabel('records',f,'(Pan Number,GSL,RERC,INPD,HTX,LTCG,STCG,OIN,TI,ITax)','arial',4,0)
        for i in records:
            if i==[]:
                continue
            if i[0]==str(pannum1):
                recordmatch=recordmatch+[i]
        if recordmatch==[]:
            tkinter.messagebox.showerror('ERROR','PAN number Record Not found')
               
        else:
            for i in recordmatch:
                tree=ttk.Treeview(f)
                tree['columns']=('PAN Number','ITAX','Financial')
                tree.column('#0',width=120)
                tree.column('PAN Number',anchor='center',width=120)
                tree.column('ITAX',anchor='center',width=120)
                tree.column('Financial',anchor='center',width=120)
                tree.heading('#0',text='S.No.',anchor='center')
                tree.heading('PAN Number',text='PAN Number',anchor='center')
                tree.heading('ITAX',text='Income Tax',anchor='center')
                tree.heading('Financial',text='Financial Year',anchor='center')
                C=1
                for j in range(0,len(records)):
                    a=records[j]
                    if a==[]:
                        continue
                    elif a[0]==pannum1:
                        tree.insert(parent='',index='end',text=str(C),values=(a[0],a[-1],a[1]))
                        print(a)
                    C=C+1
                tree.grid(column=0,row=6)
 
    #'GSL','RERC','INPD','HTX','LTCG','STCG','OIN','TI',
    f2.close()
   
#to open tax calculation records
def taxdata():
    global pannum,f
    f=tkinter.Tk()
    f.title('income tax calculator')
    f.geometry('800x600')
    l1=tkinter.Label(f,text="Tax details",font=("ALGERIAN",30),bg="#f5e180")
    l1.grid(column=0,row=0,columnspan=4)
   
    pannuml=tkinter.Label(f,text="Enter pan number",font=("Times New Roman",30))
    pannuml.grid(column=0,row=1,columnspan=4)
    pannum=tkinter.Entry(f,width=20,borderwidth=2,font=("Times New Roman",20))
    pannum.grid(column=0,row=2,columnspan=2)
   
    b=tkinter.Button(f,text='Submit',font=("Times New Roman",20),command=taxdatabase)
    b.grid(row=3,column=0)


def update():
    exit4()
    a1('update')

#to update profile
def updatedel():
    global l2,name,email,ph_no,paswd,paswdcfm,username
    #exit3()
    username,name,email,ph_no,paswd,paswdcfm=prodata['USERNAME'],nm.get(),emlid.get(),pno.get(),pswd.get(),pswdcfm.get()
    l2=[username,name,email,ph_no,paswd,paswdcfm]
    c=True
   
    for i in l2:
        if (i.isspace() or len(i)==0 or i=='' ) and c==True :
            c=False
            tkinter.messagebox.showerror('ERROR','Empty Entry')
   
    if '@' not in l2[2] and c==True:
        tkinter.messagebox.showerror('ERROR','Enter valid email ID')
        c=False
    elif len(ph_no)!=10 and not ph_no.isdigit() and c==True:
        tkinter.messagebox.showerror('ERROR','Enter valid Phone Number')
        c=False
   
    elif str(paswd) != str(paswdcfm) and c==True :
        tkinter.messagebox.showerror('ERROR','Password and Password Confirm not matched')
        c=False
   
    elif True and c==True:
        namealpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
        for i in l2[1]:
            if i not in namealpha:
                tkinter.messagebox.showerror('ERROR','Invalid Name, Dont use special Characters')
                c=False
    if c==True:
        print(l2)
       
        import csv
        f1=open('data.csv','r')
        read=list(csv.reader(f1))
        f1.close()
        f1=open('data.csv','w')
        print('Record , ',read)
        for i in read:
            if i==[]:
                continue
            elif i[0]==l2[0]:
                recordnum=read.index(i)
                x=i
        print('x = ',x)
        for i in range(len(x)):
            x[i]=l2[i]
        print('x = ',x)
        read[recordnum]=x
        print('final',recordnum,read)
        write=csv.writer(f1)
        write.writerows(read)
        f1.close()
        tkinter.messagebox.showinfo('Profile','Profile Updated ')
        details()
        exit1()
       
def profile():
    global d,prodata
    try:
        exit3()
    except:
        pass
    try:
        exit1()
    except:
        pass
   
    d=tkinter.Tk()
    d.title('income tax calculator')
    d.geometry('400x350')
    l11=tkinter.Label(d,text="Profile",font=("ALGERIAN",30),bg="#f5e180")
    l11.grid(column=0,row=0,columnspan=4)
    pro1=open('data.csv','r')
    profiled=list(csv.reader(pro1))
    pro1.close()
    select=[]
   
    for i in profiled:
        i=list(i)
        print(i)
        if i==[]:
            continue
        elif i=='':
            continue
        elif str((i)[0])==str(usernameprofile):
            select=(i)
    print("Select",select)
    if select!=[]:
        prodata={"USERNAME":str(select[0]),"NAME":str(select[1]),"EMAIL":str(select[2]),"PHONE":str(select[3]),"PASSWORD":str(select[4])}
        row=1
        for i in prodata:
            makelabel('Profile',d,i,"Times New Roman",row,1,20)
            makelabel('Profile',d,prodata[i],"Times New Roman",row,2,20)
            row=row+1
    updateb=tkinter.Button(d,text='Update',font=("Times New Roman",20),command=update)
    updateb.grid(row=10,column=1)
    calcback=tkinter.Button(d,text='Back',font=("Times New Roman",20),command=details)
    calcback.grid(row=10,column=2)

#function for submit on sign in page
def del2():
    global user,pwdsign,passwd,pass1,f1,u,p,usernameprofile
    user,pwdsign=u.get(),p.get()
    pass1[user]=pwdsign  
    w=True                            
    for i in pass1:
        if pass1[i].isspace() or len(pass1[i])==0:
            tkinter.messagebox.showerror('ERROR','Empty Entry')
            w=False
            break
   
    found=False
    f1=open('data.csv','r')
    details1=csv.reader(f1)                            
    for r in details1 :
        print(r)
        if r==[]:
            continue                            
        elif str(user)==str(r[0]) and  pwdsign==r[4]:
            print('username matched')
            print('password matched')
            usernameprofile=str(user)
            found=True
            break
    if found==False:
         if w!=False:
             tkinter.messagebox.showerror('ERROR','Invalid username or password, please try again.')
             w=False
    else:
        details()
               
    #u.delete(0,len(user)) p.delete(0,len(pwdsign))
    f1.close()
def exit1():#to exit home page
    a.destroy()
def exit2():#to exit sign in page
    c.destroy()
def exit3():#to exit calculator
    b.destroy()
def exit4():#to exit profile
    d.destroy()    
           
def details(): #calculator
    global b,PI,PAN,FY,FYr,GS,OI,IP,RR,HT,LCG,SCG,GSL,RERC,INPD,HTX,LTCG,STCG,OIN,itax,itax1
    try:
        exit2()
    except:
        pass
    try:
        exit1()
    except:
        pass
    b=tkinter.Tk()
    b.title('income tax calculator')
    b.geometry('1050x600')
    l1=tkinter.Label(b,text="INCOME TAX CALCULATOR",font=("ALGERIAN",30),bg="#f5e180")
    l1.grid(column=0,row=0,columnspan=4)
   
    lp=tkinter.Label(b,text="Enter PAN ID:",font=("Times New Roman",20))
    lp.grid(column=0,row=2,sticky='W',columnspan=2)
   
    PI=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    PI.grid(column=2,row=2,columnspan=2)
   
    PAN=(PI.get())

    ly=tkinter.Label(b,text="Enter Financial Year:",font=("Times New Roman",20))
    ly.grid(column=0,row=3,sticky='W',columnspan=2)
   
    FY=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    FY.grid(column=2,row=3,columnspan=2)
   
    l=tkinter.Label(b,text="Enter the following details-",font=("Times New Roman",30))
    l.grid(column=0,row=1)
    #labels for calculationg income tax
    #total salary
    l2=tkinter.Label(b,text="Gross Salary (as given in Form 16):",font=("Times New Roman",20))
    l2.grid(column=0,row=4,sticky='W',columnspan=2)
    GS=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    GS.grid(column=2,row=4,columnspan=2)
 
    l3=tkinter.Label(b,text="Rental recieved from House Property: \n(if any)",font=("Times New Roman",20))
    l3.grid(column=0,row=5,sticky='W',columnspan=2)
    RR=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    RR.grid(column=2,row=5,columnspan=2)
 
    l4=tkinter.Label(b,text="Interest paid on Housing loan:",font=("Times New Roman",20))
    l4.grid(column=0,row=6,sticky='W',columnspan=2)
    IP=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    IP.grid(column=2,row=6,columnspan=2)
 
    l5=tkinter.Label(b,text="House Tax paid:",font=("Times New Roman",20))
    l5.grid(column=0,row=7,sticky='W',columnspan=2)
    HT=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    HT.grid(column=2,row=7,columnspan=2)
   
    l6=tkinter.Label(b,text="Income from long term Capital Gains:",font=("Times New Roman",20))
    l6.grid(column=0,row=8,sticky='W')
    LCG=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    LCG.grid(column=2,row=8)
   
    l7=tkinter.Label(b,text="Income from short term Capital Gains:",font=("Times New Roman",20))
    l7.grid(column=0,row=9,sticky='W',columnspan=2)
    SCG=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    SCG.grid(column=2,row=9,columnspan=2)
   
    l8=tkinter.Label(b,text="Other Income:",font=("Times New Roman",20))
    l8.grid(column=0,row=10,sticky='W',columnspan=2)
    OI=tkinter.Entry(b,width=20,borderwidth=2,font=("Times New Roman",20))
    OI.grid(column=2,row=10,columnspan=2)
   
    bsub=tkinter.Button(b,text='Submit',font=("Times New Roman",20),command=submitdata)
    bsub.grid(row=11,column=0)
   
    #to clear and retry
    bclear=tkinter.Button(b,text='Clear',font=("Times New Roman",20),command=cleardata)
    bclear.grid(row=11,column=2)
   
    #exit button for calculator
    be=tkinter.Button(b,text='Exit',font=("Times New Roman",20),command=exit3)
    be.grid(row=11,column=1)  
   
    GSL,RERC,INPD,HTX,LTCG,STCG,OIN=(GS.get()),(RR.get()),(IP.get()),(HT.get()),(LCG.get()),(SCG.get()),(OI.get())
   
    itax=tkinter.Label(b)
    itax1=tkinter.Label(b)
   
    profileback=tkinter.Button(b,text='Profile',font=("Times New Roman",20),command=profile)
    profileback.grid(row=2,column=4)  
   
    #add details to record
    br=tkinter.Button(b,text="Save Record",font=("Times New Roman",20),command=addrecord)
    br.grid(column=4,row=11)  
   
    taxdetail=tkinter.Button(b,text='Tax detail',font=("Times New Roman",20),command=taxdata)
    taxdetail.grid(row=6,column=4)

#clear data and recalculate
def cleardata():
    global PI,FY,FYr,PAN,GS,OI,IP,RR,HT,LCG,SCG,GSL,RERC,INPD,HTX,LTCG,STCG,OIN,ITax,itax,itax1
    GSL,RERC,INPD,HTX,LTCG,STCG,OIN=(GS.get()),(RR.get()),(IP.get()),(HT.get()),(LCG.get()),(SCG.get()),(OI.get())
    FYr=(FY.get())
    GS.delete(0,len(GSL))
    RR.delete(0,len(RERC))
    IP.delete(0,len(INPD))
    HT.delete(0,len(HTX))
    LCG.delete(0,len(LTCG))
    SCG.delete(0,len(STCG))
    OI.delete(0,len(OIN))
    PI.delete(0,len(PAN))
    FY.delete(0,len(FYr))
    ITax=0
    itax.destroy()
    itax1.destroy()

def submitdata():  #calculating income tax
    global PAN,FY,FYr,f1,f2,b,GS,OI,IP,RR,HT,LCG,SCG,GSL,RERC,INPD,HTX,LTCG,STCG,OIN,ITax,TI,itax,itax1,FY,FYr
    f2=open('details.csv','a')
    #dw=csv.writer(f2)
    FYr=FY.get()
    ITax=0
    PAN=PI.get()
    w=True
    if PAN=='' or len (PAN) == 0 :
        tkinter.messagebox.showerror('ERROR','Empty Entry (PAN Number)')
        w=False
           
    print(PAN,type(PAN))
    if len(PAN)==10 and PAN[0:4].isalpha()==True and PAN[5:8].isnumeric()==True and PAN[9].isalpha()==True:
        pass
    else:
        if w==True:
            tkinter.messagebox.showerror('ERROR','Enter Valid PAN Number')
            w=False
           
    if len(FYr)==4 and FYr.isdigit()==True:
        pass
    else:
        if w==True and len(FYr)!=4 or not FYr.isdigit():
            tkinter.messagebox.showerror('ERROR','Enter Valid Financial Year')
            w=False
           
    GSL,RERC,INPD,HTX,LTCG,STCG,OIN=(GS.get()),(RR.get()),(IP.get()),(HT.get()),(LCG.get()),(SCG.get()),(OI.get())
    T=GSL
    ld=[GSL,RERC,INPD,HTX,LTCG,STCG,OIN]
    T=GSL
    if GSL=='':
        GSL=ld[0]='0'
    if RERC=='':
        RERC=ld[1]='0'
    if INPD=='':
        INPD=ld[2]='0'
    if HTX=='':
        HTX=ld[3]='0'
    if LTCG=='':
        LTCG=ld[4]='0'
    if STCG=='':
        STCG=ld[5]='0'
    if OIN=='':
        OIN=ld[6]='0'
    for i in ld:
        if not i.isdigit() and w==True:
            tkinter.messagebox.showerror('ERROR','Enter Valid Numberic data ')
            w=False
   
    TI=int(GSL)+int(RERC)-0.3*int(RERC)-int(INPD)-int(HTX)+int(LTCG)+int(STCG)+int(OIN)
    print(TI)
    if TI<=250000:
        print('no income tax')
    if 1500000<TI:
        T=TI-1500000
        ITax=T*0.3  
        j=0.25  
        for i in range(5):
            ITax=ITax+(j*250000)
            j=j-0.05
        print('income tax is',ITax)
    elif 1250000<TI<=1500000:
        ITax=0
        T=TI-1250000
        ITax=T*0.25  
        j=0.20
        for i in range(4):
            ITax=ITax+(j*250000)
            j=j-0.05
        print('income tax is',ITax)      
    elif 1000000<TI<=1250000:
        ITax=0
        T=TI-1000000
        ITax=T*0.20  
        j=0.15
        for i in range(3):
            ITax=ITax+(j*250000)
            j=j-0.05
        print('income tax is',ITax)
    elif 750000<TI<=1000000:
        ITax=0
        T=TI-750000
        ITax=T*0.15  
        j=0.10
        for i in range(2):
            ITax=ITax+(j*250000)
            j=j-0.05
        print('income tax is',ITax)
    elif 500000<TI<=750000:
        ITax=0
        T=TI-500000
        ITax=T*0.10
        j=0.05
        for i in range(1):
            ITax=ITax+(j*250000)
            j=j-0.05
        print('income tax is',ITax)
    elif 250000<TI<=500000:
        ITax=0
        T=TI-250000
        ITax=T*0.05
        print('income tax is',ITax)
    print(ITax)
    #error.destroy()
    #makelabel('itax',b,'income tax is','arial 30',20,0)
    #makelabel('itax1',b,ITax,'arial 30',20,1)
    itax=tkinter.Label(b,text='Income Tax is',font=("Times New Roman",30))
    itax.grid(column=0,row=20,columnspan=2)
    itax1=tkinter.Label(b,text=ITax,font=("Times New Roman",30))
    itax1.grid(column=2,row=20,columnspan=2)
    f2.close()
#add calculator data to table
def addrecord():
    f2=open('details.csv','a')
    dw=csv.writer(f2)
    ld=[PAN,FYr,GSL,RERC,INPD,HTX,LTCG,STCG,OIN,TI,ITax,]
    dw.writerow(ld)
    tkinter.messagebox.showinfo('Saved','Record has been added!')
    f2.close()

#Sign in
def sign_in():  #taking sign in details
    exit1()
    global c,p,u,passwd    
    c=tkinter.Tk()
    c.title('sign in page')
    c.geometry('550x300')
    c.configure(bg="#f5e180")
    label=tkinter.Label(c,text="Sign In",font=("ALGERIAN",40),bg="#f5e180",)
    label.grid(column=1,row=0)
 
    label1=tkinter.Label(c,text="Username",font=("Times New Roman",20),bg="#f5e180")
    label1.grid(column=1,row=2)
    u=tkinter.Entry(c,width=20,borderwidth=2,font=("Times New Roman",20))
    u.grid(column=2,row=2)
 
    label2=tkinter.Label(c,text="Password",font=("Times New Roman",20),bg="#f5e180")
    label2.grid(column=1,row=3)
    p=tkinter.Entry(c,width=20,borderwidth=2,font=("Times New Roman",20),show='*')
    p.grid(column=2,row=3)
 
    submitbt=tkinter.Button(c,text="Submit",font=("Times New Roman",20),command=del2)
    submitbt.grid(column=1,row=4)
    be=tkinter.Button(c,text='Exit',font=("Times New Roman",20),command=exit2)
    be.grid(row=5,column=2)
    bbk=tkinter.Button(b,text='Back',font=("Times New Roman",20),command=back)
    bbk.grid(row=5,column=1)
    passwd=p.get()

#submit for sign up
def signupdel(function='signup'):  
    global l,l1,username,name,email,ph_no,paswd,paswdcfm
    username,name,email,ph_no,paswd,paswdcfm=usnm.get(),nm.get(),emlid.get(),pno.get(),pswd.get(),pswdcfm.get()
    #,usnm,nm,emlid,pno,pswd,pswdcfm,f1
    #signlist=[p1,p2,p3,p4,p5,p6]    
    c=True
    l1=[username,name,email,ph_no,paswd,paswdcfm]
    l2=[usnm,nm,emlid,pno,pswd,pswdcfm]
    store2={'usnm':username,'nm':name,'emlid':email,'pno':ph_no,'pswd':paswd,'pswdcfm':paswdcfm}
    f1=open('data.csv','r')
    signdata=list(csv.reader(f1))
    f1.close()
    if function=='signup':
        for i in signdata:
            if i!=[] and i[0]==username and c==True:
                tkinter.messagebox.showerror('ERROR','Username Already taken !')
                c=False
           
    for i in store2 :
        if (store2[i].isspace() or len(store2[i])==0 )and c==True :
            tkinter.messagebox.showerror('ERROR','Empty Entry')
            c=False
            break
    for i in range(len(l)):
        j=(l2[i])
        print(j)
        if store2[j].isspace() or len(store2[j])==0 or store2[j]=='' and c==True :
            tkinter.messagebox.showerror('ERROR','Empty Entry')
            c=False
    print(l1)
    id1=['.com','.edu','.gov.in','.org','.in','.us']
    cou=False
    for i in id1 :
            if i in l1[2]:
                cou=True
    if cou==False and c==True :
        tkinter.messagebox.showerror('ERROR','Enter Valid Email ID')
        c=False

    def write():
        if function!='update':  
            f1=open('data.csv','a')
            w=csv.writer(f1,delimiter=',')
            w.writerow(l1)
            f1.close()
            sign_in()    
           
    if '@' not in l1[2] and c==True :
        tkinter.messagebox.showerror('ERROR','Enter Valid Email ID')
        c=False
       
    elif len(ph_no)!=10 and c==True :
        tkinter.messagebox.showerror('ERROR','Enter Valid Phone Number')
        c=False
    elif not ph_no.isdigit() and c==True :
        tkinter.messagebox.showerror('ERROR','Enter Valid Phone Number')
        c=False
       
    elif str(paswd) != str(paswdcfm) and c==True :
        tkinter.messagebox.showerror('ERROR','Password and Password Confirm not matched')
        c=False
   
    elif True:
        namealpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
        for i in l1[1]:
            if i not in namealpha and c==True :
                tkinter.messagebox.showerror('ERROR','Invalid Name, Dont use special Characters')
                c=False

    if c==True:
        write()

#sign up clear data for re entry  
def clear():
    global l,l1,usnm,nm,emlid,pno,pswd,pswdcfm,f1,username,name,email,ph_no,paswd,paswdcfm
    username,name,email,ph_no,paswd,paswdcfm=usnm.get(),nm.get(),emlid.get(),pno.get(),pswd.get(),pswdcfm.get()
    usnm.delete(0,len(username))
    nm.delete(0,len(name))
    emlid.delete(0,len(email))
    pno.delete(0,len(ph_no))
    pswd.delete(0,len(paswd))
    pswdcfm.delete(0,len(paswdcfm))
    #empty.destroy()

#clear data for update profile
def clearup():
    #username,name,email,ph_no,paswd,paswdcfm=prodata['USERNAME'],nm.get(),emlid.get(),pno.get(),pswd.get(),pswdcfm.get()
    usnm.delete(0,len(username))
    nm.delete(0,len(name))
    emlid.delete(0,len(email))
    pno.delete(0,len(ph_no))
    pswd.delete(0,len(paswd))
    pswdcfm.delete(0,len(paswdcfm))

#opens first window
def a1(function="Signup"):   #opens first window
    global a,l1,usnm,nm,emlid,pno,pswd,pswdcfm,f1,bclr
    try:
        exit3()
    except:
        pass
    a=tkinter.Tk()
    a.title("Personal Finanace Assistance")
    if function=='update':
        a.geometry('500x500')
    else:
        a.geometry('1200x700')
        a.iconbitmap('favicon (1).ico')  
        pic=tkinter.PhotoImage(file=('inco tax_final.png'))
        lp=tkinter.Label(a,image = pic)
        lp.grid(row=3,column=0,rowspan=5)  
    a.configure(bg="#f5e180")
    #labels for sign up page
    if function=="update":
        label=tkinter.Label(a,text="UPDATE",font=("ALGERIAN",30),bg="#f5e180",)
    else:
         label=tkinter.Label(a,text="Sign Up",font=("ALGERIAN",40),bg="#f5e180",)
    label.grid(column=1,row=0)
    #username
    if function!='update':
        label1=tkinter.Label(a,text="Username",font=("Times New Roman",20),bg="#f5e180")
        label1.grid(column=1,row=2)
        usnm=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20))
        usnm.grid(column=2,row=2)
    #name
    label2=tkinter.Label(a,text="Name",font=("Times New Roman",20),bg="#f5e180")
    label2.grid(column=1,row=3)
    nm=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20))
    nm.grid(column=2,row=3)
    #email ID
    label3=tkinter.Label(a,text="Email ID ",font=("Times New Roman",20),bg="#f5e180")
    label3.grid(column=1,row=4)
    emlid=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20))
    emlid.grid(column=2,row=4)
    #phone number
    label4=tkinter.Label(a,text="Phone Number",font=("Times New Roman",20),bg="#f5e180")
    label4.grid(column=1,row=5)
    pno=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20))
    pno.grid(column=2,row=5)
    #password
    label5=tkinter.Label(a,text="Password",font=("Times New Roman",20),bg="#f5e180")
    label5.grid(column=1,row=6)
    pswd=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20),show='*')
    pswd.grid(column=2,row=6)
    #repeat password
    label6=tkinter.Label(a,text="Confirm",font=("Times New Roman",20),bg="#f5e180")
    label6.grid(column=1,row=7)
    pswdcfm=tkinter.Entry(a,width=20,borderwidth=2,font=("Times New Roman",20),show='*')
    pswdcfm.grid(column=2,row=7)
    #submit to open sign in page  
    if function!="update":
        b2=tkinter.Button(a,text="Submit",font=("Times New Roman",20),command=signupdel)
        b2.grid(column=2,row=9)
        #if already details are entered
        b3=tkinter.Button(a,text='Already a member ? Sign in',font=("Times New Roman",20),command=sign_in)
        b3.grid(row=8,column=1)
        #exiting signup page
        be=tkinter.Button(a,text='Exit',font=("Times New Roman",20),command=exit1)
        be.grid(row=9,column=1)
        bclr=tkinter.Button(a,text='Clear',font=("Times New Roman",20),command=clear)
        bclr.grid(row=8,column=2)
    else:
        '''bclr=tkinter.Button(a,text='Clear',font=("Times New Roman",20),command=clearup)
        bclr.grid(row=8,column=1)'''
        profileback=tkinter.Button(a,text='Profile',font=("Times New Roman",20),command=profile)
        profileback.grid(row=9,column=1)
        b2=tkinter.Button(a,text="Submit",font=("Times New Roman",20),command=updatedel)
        b2.grid(column=2,row=8)
        calcback=tkinter.Button(a,text='Calculator',font=("Times New Roman",20),command=details)
        calcback.grid(row=9,column=2)

a1()
l=[]
l1=[]
a.iconbitmap('favicon (1).ico')  
f2=open('details.csv','a+')                
b=None  
pic=tkinter.PhotoImage(file=('inco tax_final.png'))
lp=tkinter.Label(a,image = pic)
lp.grid(row=3,column=0,rowspan=5)  
a.mainloop()
f1.close()
