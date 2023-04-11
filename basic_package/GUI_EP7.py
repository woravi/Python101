import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
########### CSV ############
import csv
from tkinter.ttk import Labelframe
from datetime import datetime
import csv

def writecsv(datalist):
    with open('EngineFire.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('EngineFire.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(file)
    return data
data = readcsv()
print(data)

########### CSV ############

GUI = tkinter.Tk()# คือหน้าจอ หลัก
GUI.title('ประวัติเครื่องยนต์งานดับเพลิง')
GUI.geometry('800x800')

frame = ttk.Frame(GUI)
frame.pack()

f1 = font=('tahoma', 18)
f2 = font=('tahoma', 25)
Label = tkinter.Label(frame, text='FIRE MAN STATION', font = f1)
Label.grid(row=0, column=0)

engine_info = tkinter.LabelFrame(frame, text='ชนิดเครื่องยนต์', font = f1)
engine_info.grid(row=1,column=0)

###########################################


f1 = font=('tahoma', 18)
f2 = font=('tahoma', 25)
Label = tkinter.Label(frame, text='FIRE MAN STATION', font = f1)
Label.grid(row=0, column=0)
engine_info = tkinter.LabelFrame(frame, text='ชนิดเครื่องยนต์', font = f1)
engine_info.grid(row=1,column=0)

engine_type = tkinter.Label(engine_info, text="ชนิด",font=f1)
engine_type.grid(row=1, column=0)
engle_type_en = ttk.Combobox(engine_info, values=["รถดับเพลิง", "เครื่องสูบน้ำ", "เครื่องกำเนิดไฟฟ้า", "เครื่องกำเนิดไฟฟ้า-8259", "เครื่องระบายควัน", "เครื่องอัดอากาศ", "ถังดบเพลิง เคมีแห้ง", "ถังดับเพลิง ฮาโลตรอน"])
engle_type_en.grid(row=2, column=0,ipadx=40)

en_no = tkinter.Label(engine_info, text="หมายเลข S/No",font=f1)
en_no.grid(row=1, column=1)
info = ttk.Combobox(engine_info, values=["ตส - 8225", "ตส - 8215", "ฒษ - 3755", "ฒบ - 8259", "I-853 ระบายควัน", "P-28 อัดอากาศ", "EP-2500", "ช - 1325"])
info.grid(row=2, column=1,ipadx=35)

check = tkinter.Label(engine_info, text="สถานะปัจจุบัน",font=f1)
check.grid(row=3,column=0)
check_info = ttk.Combobox(engine_info, values=["ปกติ", "ชำรุด"])
check_info.grid(row=4,column=0,ipadx=40)

broken1 = tkinter.Label(engine_info, text="อาการที่ชำรุด",font=f1)
broken1.grid(row=3, column= 1)
broken_en = tkinter.Entry(engine_info)
broken_en.grid(row=4,column=1,ipadx=35)

make_corrections = tkinter.LabelFrame(frame, text='make corrections', font = f1)
make_corrections.grid(row=2,column=0)

make1 = tkinter.Label(make_corrections, text="หมายเลข สั่งซ่อม",font=f1)
make1.grid(row=1, column= 1)
make1_en = tkinter.Entry(make_corrections)
make1_en.grid(row=2,column=1,ipadx=40)

date_label1 = tkinter.Label(make_corrections, text="วัน/เวลาที่ส่งรายงาน",font=f1)
date_label1.grid(row=1, column=2)
date_make = tkinter.Entry(make_corrections)
date_make.grid(row=2, column=2,ipadx=40)

for widget in make_corrections.winfo_children():
    widget.grid_configure(padx=8, pady=5)


from datetime import datetime
time = datetime.now().strftime('%d%m%Y %H%M%S')
def data():

    engine_type = engle_type_en.get()
    en_no = info.get()
    check = check_info.get()
    broken1 = broken_en.get()
    make1 = make1_en.get()
    date_label1 = date_make.get()

    information = [time,
            ("ชนิดเครื่องยนต์ : ", engine_type),
            ("หมายเลข S/No : ", en_no),
            ("สถานะปัจจุบัน : ", check),
            ("อาการที่ชำรุด : ", broken1),
            ("หมายเลข สั่งซ่อม : ", make1),
            ("วัน/เวลาที่ส่งรายงาน : ", date_make),
            ] 

    writecsv(information)

    text = 'บันทึกข้อมูลเรียบร้อยแล้ว'
    messagebox.showinfo('SAVE',text)



button = tkinter.Button(frame, text="บันทึกข้อมูล",bg='white',
    fg='red', font=('tahoma',18), width=30, command= data)
button.grid(row=25, column=0, padx=30, pady=20)



GUI.mainloop()
