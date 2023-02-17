from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()  # คือหน้าจอ หลัก
GUI.title('การฝึกพนักงานดับเพลิง')  # ชื่อ โปรแกรม
GUI.geometry("500x400")

L1 = Label (GUI, text='โปรแกรมบันทึกการฝึก',font=('Angsana New',20),fg='Green')
L1.place(x=150, y=10)



###########################################
def Button1():
    Text = 'ทบทวนการใช้เครื่องระบายควัน'
    messagebox.showinfo('เครื่องระบายควัน',Text)
    
FB1 = Frame(GUI)
FB1.place(x=40, y=40)
B1 = ttk.Button(FB1, text='นัดหมาย วันที่ 10 ม.ค. 66',command = Button1)
B1.pack(ipadx=10, ipady=10)

####################################
def Button2():
    Text = 'การเข้าผจญเพลิงในอาคาร'
    messagebox.showinfo('ผจญเพลิงในอาคาร',Text)
    
FB2 = Frame(GUI)
FB2.place(x=40, y=40)
B2 = ttk.Button(FB1, text='นัดหมาย วันที่ 11 ม.ค. 66',command = Button2)
B2.pack(ipadx=20, ipady=20)


def Button3():
    Text = 'การบรรจุอากาศ'
    messagebox.showinfo('ใช้เครื่องยนต์',Text)
    
FB3 = Frame(GUI)
FB3.place(x=40, y=40)
B3 = ttk.Button(FB1, text='นัดหมาย วันที่ 12 ม.ค. 66',command = Button3)
B3.pack(ipadx=20, ipady=20)


def Button4():
    Text = 'การดับเพลิงเกิดจากน้ำมัน'
    messagebox.showinfo('ผจญเพลิง',Text)
    
FB4 = Frame(GUI)
FB4.place(x=40, y=40)
B4 = ttk.Button(FB1, text='นัดหมาย วันที่ 13 ม.ค. 66',command = Button4)
B4.pack(ipadx=20, ipady=20)


GUI.mainloop()

