#required modules tkinter
from tkinter import *
from tkinter import font as tkFont
from tkinter import *
import tkinter.messagebox

root=Tk()

widths=root.winfo_screenwidth()
heights=root.winfo_screenheight()


root.geometry("%dx%d+0+0" % (widths,heights))
root.config(bg="#081923")
helv36 = tkFont.Font(family='Helvetica',size=29)


Label_Head=Label(root,text="Tic Tac Toe Game",font=("Times",30,"bold"),bg="#081923",fg="White",underline=10).place(x=620,y=50,width=350,height=50)

label_Name=Label(root,text="Enter Name",font=("times new roman",18,"bold"),bg="#5F9EA0",fg="white")
label_player1=Label(root,text="Player 1",font=("times new roman",14,"bold"),bg="#0047AB",fg="white")
label_player2=Label(root,text="Player 2",font=("times new roman",14,"bold"),bg="#0096FF",fg="white")


p1=StringVar()
p2=StringVar()


input_d=Entry(root)
input_m=Entry(root)

def disbtn():
    global button7,button7,button6,button5,button4,button3,button2,button1,button8,button9
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)





bclick=True
c=0




def winner():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" ):
        disbtn()
        tkinter.messagebox.showinfo("game",pw1)
    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" ):
        disbtn()
        tkinter.messagebox.showinfo("game",pw2)
    elif(c==8):
        tkinter.messagebox.showinfo("Match tied")


def btnclick(x):
    global c,bclick,pl1,pl2,pw1,pw2
    if x["text"]=="" and bclick==True:

        x["text"]="X"
        bclick=False
        pw1=p1.get() + " wins"
        winner()

        c+=1

    elif x["text"] =="" and bclick==False:
        x["text"]="O"
        bclick=True
        pw2=p2.get() + " wins"
        winner()

        c=+1
    else:
        tkinter.messagebox.showinfo("Button already clicked")



def afterClick():
    p1.set("Player1: "+input_d.get())
    p2.set("Player2: "+input_m.get())
    label_p1=Label(root,textvariable=p1,font=("times new roman",18,"bold"),bg="#5F9EA0",fg="white").place(x=690,y=150,width=180,height=30)
    label_p1=Label(root,textvariable=p2,font=("times new roman",18,"bold"),bg="#5F9EA0",fg="white").place(x=690,y=200,width=180,height=30)
    gameFrame()
    


def onClick():
    label_Name.place_forget()
    label_player1.place_forget()
    label_player2.place_forget()
    input_d.place_forget()
    input_m.place_forget()
    button_Submit.place_forget()
    afterClick()


def gameFrame():
    Frame_main=Frame(root,bg="white").place(x=580,y=300,width=400,height=400)

    global button7,button7,button6,button5,button4,button3,button2,button1,button8,button9
    button7=Button(root,bg="#081923",borderwidth=0,text="",fg="white",command=lambda: btnclick(button7),font=("Times",30,"bold"))
    button7.place(x=580,y=300,width=130,height=130)
    button8=Button(Frame_main,text="",fg="white",font=("Times",30,"bold"),bg="#081923",borderwidth=0,command=lambda: btnclick(button8))
    button8.place(x=715,y=300,width=130,height=130)
    button9=Button(Frame_main,bg="#081923",borderwidth=0,text="",fg="white",command=lambda: btnclick(button9),font=("Times",30,"bold"))
    button9.place(x=850,y=300,width=130,height=130)

    button4=Button(Frame_main,bg="#081923",text="",fg="white",borderwidth=0,font=("Times",30,"bold"),command=lambda: btnclick(button4))
    button4.place(x=580,y=435,width=130,height=130)
    button5=Button(Frame_main,bg="#081923",text="",fg="white",borderwidth=0,font=("Times",30,"bold"),command=lambda: btnclick(button5))
    button5.place(x=715,y=435,width=130,height=130)
    button6=Button(Frame_main,bg="#081923",borderwidth=0,text="",fg="white",font=("Times",30,"bold"),command=lambda: btnclick(button6))
    button6.place(x=850,y=435,width=130,height=130)

    button1=Button(Frame_main,bg="#081923",text="",fg="white",borderwidth=0,font=("Times",30,"bold"),command=lambda: btnclick(button1))
    button1.place(x=580,y=570,width=130,height=130)
    button2=Button(Frame_main,bg="#081923",text="",fg="white",borderwidth=0,font=("Times",30,"bold"),command=lambda: btnclick(button2))
    button2.place(x=715,y=570,width=130,height=130)
    button3=Button(Frame_main,bg="#081923",text="",fg="white",borderwidth=0,font=("Times",30,"bold"),command=lambda: btnclick(button3))
    button3.place(x=850,y=570,width=130,height=130)

button_Submit=Button(root,text="Submit",command=onClick)

label_Name.place(x=690,y=300,width=180,height=30)
label_player1.place(x=635,y=380,width=120,height=30)
label_player2.place(x=635,y=420,width=120,height=30)
input_d.place(x=770,y=385)
input_m.place(x=770,y=425)
button_Submit.place(x=720,y=470,width=80,height=30)


root.mainloop()
