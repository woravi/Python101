from tkinter import *

# color

bg = '#1c1c1c'

GUI = Tk()
GUI.geometry('500x400+500+50')
GUI.configure(background='#1c1c1c')
GUI.state('zoomed')

WW = GUI.winfo_screenwidth()
WH = GUI.winfo_screenheight()

canvas = Canvas(GUI, width=WW, height=WH, background=bg)
canvas.configure(bd=0, relief='ridge', highlightthickness=0)
canvas.place(x=0, y=0)

GUI.mainloop()
