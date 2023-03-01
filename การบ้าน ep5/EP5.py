from tkinter import *
from tkinter import ttk
from tkinter import messagebox

RW = Tk()
RW.title('Oxygen SCBA')
RW.geometry('500x300')

F1 = ttk.LabelFrame()
F1.place(x=120,y=130)

MH1 = Label(RW,text="คำนวณเวลาในการใช้อากาศ \n ในพื้นที่อับอากาศ",font=('Angsana New',20),fg='white',bg='green')
MH1.place(x=120,y=20)
CM1 = Label(RW,text='ใส่จำนวนอากาศในถัง',font=('Angsana New',18),fg='white',bg='green')
CM1.place(x=120,y=105)

o_oxcigen = IntVar()
V1 = ttk.Entry(F1,font=('Angsana New',22),textvariable=o_oxcigen)
V1.pack(padx=5,pady=5)

def oxsigen():
    oxcijen = o_oxcigen.get()
    if oxcijen >= 300:
        count = oxcijen*6
        total = count/40
    elif oxcijen >= 200:
        count = oxcijen*6
        total = count/40
    elif oxcijen >= 100:
        count = oxcijen*6
        total = count/40
    else:
        count = oxcijen
      
    text = ('อยู่ในพื้นที่อับอากาศได้:' ,total,"นาที", 'จากอากาศในถัง',oxcijen,'บาร์')
    o_oxcigen.set('')
    messagebox.showinfo('Oxygen',text)
AOXI = ttk.Button(F1,command=oxsigen,text='คำนวนอากาศ')
AOXI.pack(ipadx=15,ipady=15)

RW.mainloop()