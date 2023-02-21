import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
########### CSV ############
import csv
from tkinter.ttk import Labelframe


def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerow(datalist)  # datalist


def readcsv():
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)  # fr = file reader
        data = list(fr)
    return data
#####    csv 2 ######
def writecsv2(datalist):
    with open('data2.csv', 'a', encoding='utf-8', newline='') as file:
        fw2 = csv.writer(file)  # fw = file writer
        fw2.writerow(datalist)  # datalist


def readcsv2():
    with open('data2.csv', 'a', encoding='utf-8', newline='') as file:
        fr2 = csv.reader(file)  # fr = file reader
        data = list(fr2)
    return data
########### CSV ############

GUI = Tk()  # คือหน้าจอ หลัก
GUI.title('การฝึกพนักงานดับเพลิง')  # ชื่อ โปรแกรม
GUI.geometry("900x500")

L1 = Label(GUI, text='โปรแกรมบันทึกการฝึก', font=('Angsana New', 20), fg='Green')
L1.place(x=150, y=10)


###########################################
def Button1():
    Text = 'ทบทวนการใช้เครื่องระบายควัน'
    messagebox.showinfo('เครื่องระบายควัน', Text)


FB1 = Frame(GUI)
FB1.place(x=40, y=40)
B1 = ttk.Button(FB1, text='นัดหมาย วันที่ 10 ม.ค. 66', command=Button1)
B1.pack(ipadx=10, ipady=10)


####################################
def Button2():
    Text = 'การเข้าผจญเพลิงในอาคาร'
    messagebox.showinfo('ผจญเพลิงในอาคาร', Text)


FB2 = Frame(GUI)
FB2.place(x=40, y=40)
B2 = ttk.Button(FB1, text='นัดหมาย วันที่ 11 ม.ค. 66', command=Button2)
B2.pack(ipadx=20, ipady=20)


def Button3():
    Text = 'การบรรจุอากาศ'
    messagebox.showinfo('ใช้เครื่องยนต์', Text)


FB3 = Frame(GUI)
FB3.place(x=40, y=40)
B3 = ttk.Button(FB1, text='นัดหมาย วันที่ 12 ม.ค. 66', command=Button3)
B3.pack(ipadx=20, ipady=20)


def Button4():
    Text = 'การดับเพลิงเกิดจากน้ำมัน'
    messagebox.showinfo('ผจญเพลิง', Text)


FB4 = Frame(GUI)
FB4.place(x=40, y=40)
B4 = ttk.Button(FB1, text='นัดหมาย วันที่ 13 ม.ค. 66', command=Button4)
B4.pack(ipadx=20, ipady=20)

##############   ส่วนด้านขวา ################

LF1 = ttk.LabelFrame(GUI, text='ข้อมูลการฝึก')
LF1.place(x=350, y=50)

v_data = StringVar()  # ตัวแปลพิเศษใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1, textvariable=v_data, font=('Angsana New', 20))
E1.pack(pady=5, padx=5)

from datetime import datetime # ใส่เวลา

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get()  # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t, data]  # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text)  # บันทึกลง csv
    v_data.set('')  # เคลียร์ข้อมูลที่อยู่ในช่องกรอก


B4 = ttk.Button(LF1, text='บันทึกข้อมูล', command=SaveData)
B4.pack(ipadx=10, ipady=10)
#########---- ด้านขวาส่วนที่ 2 #########

LF2 = ttk.LabelFrame(GUI, text='ปัญหาที่พบจากการฝึก')
LF2.place(x=350, y=180)

v_data2 = StringVar()  # ตัวแปลพิเศษใช้กับข้อความใน GUI
E2 = ttk.Entry(LF2, textvariable=v_data2, font=('Angsana New', 20))
E2.pack(pady=5, padx=5)

from datetime import datetime # ใส่เวลา

def SaveData2():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data2.get()  # ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t, data]  # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv2(text)  # บันทึกลง csv
    v_data2.set('')  # เคลียร์ข้อมูลที่อยู่ในช่องกรอก


B5 = ttk.Button(LF2, text='บันทึกปัญหา', command=SaveData2)
B5.pack(ipadx=10, ipady=10)








GUI.mainloop()
