#Modules Required
#1. datetime
#2. tkinter
#3. calender


import datetime
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font as tkFont
import calendar
from datetime import date
root=Tk()
widths=root.winfo_screenwidth()
heights=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (widths,heights))
root.config(bg="#081923")
helv36 = tkFont.Font(family='Helvetica',size=29)
now = datetime.datetime.now()
year=str(now.strftime("%Y"))
date=now.strftime("%d")
month=calendar.month_name[int(now.strftime("%m"))]
def clock():
    now = datetime.datetime.now()
    hour=now.strftime("%H")
    minute=now.strftime("%M")
    second=now.strftime("%S")
    if(int(hour)>12):
        hour=str(int(hour)-12)
    label1.config(text=hour)
    label2.config(text=minute)
    label3.config(text=second)
    label4.config(text=str(now.strftime("%p")))
    label3.after(200,clock)


#Current dates and times
lable=Label(root,text="Age and Time",font=("times new roman",20,"bold"),fg="white",bg="#081923").place(x=680,y=40)
label1=Label(root,font=("times new roman",30,"bold"),bg="#0047AB",fg="white")
label1.place(x=500,y=100,width=120,height=130)
label2=Label(root,font=("times new roman",30,"bold"),bg="#0096FF",fg="white")
label2.place(x=635,y=100,width=120,height=130)
label3=Label(root,font=("times new roman",30,"bold"),bg="#5F9EA0",fg="white")
label3.place(x=770,y=100,width=120,heigh=130)
label4=Label(root,font=("times new roman",30,"bold"),bg="#6F8FAF",fg="white")
label4.place(x=905,y=100,width=120,height=130)
label5=Label(root,text="HOUR",font=("times new roman",15,"bold"),bg="#0047AB",fg="white").place(x=500,y=240,width=120,height=30)
label6=Label(root,text="MINUTE",font=("times new roman",15,"bold"),bg="#0096FF",fg="white").place(x=635,y=240,width=120,height=30)
label7=Label(root,text="SECOND",font=("times new roman",15,"bold"),bg="#5F9EA0",fg="white").place(x=770,y=240,width=120,height=30)
label8=Label(root,text="NOON",font=("times new roman",15,"bold"),bg="#6F8FAF",fg="white").place(x=905,y=240,width=120,height=30)
label9=Label(root,text=date,font=("times new roman",14,"bold"),bg="#0047AB",fg="white").place(x=500,y=280,width=120,height=30)
label10=Label(root,text=month,font=("times new roman",14,"bold"),bg="#0096FF",fg="white").place(x=635,y=280,width=120,height=30)
label11=Label(root,text=year,font=("times new roman",14,"bold"),bg="#5F9EA0",fg="white").place(x=770,y=280,width=120,height=30)
label12=Label(root,text="Date",font=("times new roman",14,"bold"),bg="#6F8FAF",fg="white").place(x=905,y=280,width=120,height=30)
#frame
frame1=Frame(root,height=200,width=530,bg="#6F8FAF").place(x=500,y=350)
label_d=Label(root,text="Date",font=("times new roman",14,"bold"),bg="#0047AB",fg="white").place(x=635,y=380,width=120,height=30)
label_m=Label(root,text="Month",font=("times new roman",14,"bold"),bg="#0096FF",fg="white").place(x=635,y=420,width=120,height=30)
label_y=Label(root,text="Year",font=("times new roman",14,"bold"),bg="#5F9EA0",fg="white").place(x=635,y=460,width=120,height=30)
dates=StringVar()
months=StringVar()
years=StringVar()
input_d=Entry(frame1)
input_d.place(x=770,y=385)
input_m=Entry(frame1)
input_m.place(x=770,y=425)
input_y=Entry(frame1)
input_y.place(x=770,y=465)
from datetime import date
today=str(date.today())    #getting current date using datetime module
list_today=today.split("-")

def click():
    from datetime import date
    global today
    global new
    b_year=int(input_y.get())
    b_date=int(input_d.get())
    b_month=int(input_m.get())
    c_date=int(list_today[2])
    c_month=int(list_today[1])
    c_year=int(list_today[0])
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>c_date):
        c_month=c_month-1
        c_date=c_date+month[b_month-1]
    if (b_month>c_month):
        c_year=c_year-1
        c_month=c_month+12
    resultd=str(c_date-b_date)
    resultm=str(c_month-b_month)
    resulty=str(c_year-b_year)
    
    years.set("Years "+str(resulty))
    months.set("Months "+str(resultm))
    dates.set("Days "+str(resultd))
    label13=Label(root,textvariable=dates,font=("times new roman",14,"bold"),fg="white",bg="#0047AB").place(x=635,y=600,width=200,height=30)
    label14=Label(root,textvariable=months,font=("times new roman",14,"bold"),fg="white",bg="#0096FF").place(x=635,y=650,width=200,height=30)
    label15=Label(root,textvariable=years,font=("times new roman",14,"bold"),fg="white",bg="#5F9EA0").place(x=635,y=700,width=200,height=30)
submit=Button(root,text="submit",command=click,bg="white").place(x=730,y=510)

clock()
root.mainloop()
