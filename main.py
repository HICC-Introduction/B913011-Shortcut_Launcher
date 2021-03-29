# B913011 Shortcut_Launcher
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

win = tk.Tk()   
win.title("KMS - Shortcut Launcher")   
win.geometry("800x200+100+100")
win.resizable(False, False)


status_label = ttk.Label(win, text = "Waiting...")
status_label.configure(foreground='blue')
status_label.pack()

def opn_note():
    btn1.configure(text="RUNNING..")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='OPEN NOTEPAD') # 레이블 텍스트 변경
def opn_calc():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="RUNNING..")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text= "OPEN CALCULATOR") # 레이블 텍스트 변경
def opn_c():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="RUNNING..")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='OPEN C:') # 레이블 텍스트 변경
def opn_google():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="RUNNING..")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='OPEN GOOGLE') # 레이블 텍스트 변경
def b5():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="RUNNING..")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='버5 실행 중') # 레이블 텍스트 변경
def b6():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="RUNNING..")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='버6 실행 중') # 레이블 텍스트 변경
def b7():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="RUNNING..")
    btn8.configure(text="BUTTON8")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='버7 실행 중') # 레이블 텍스트 변경 
def b8():
    btn1.configure(text="NOTEPAD")
    btn2.configure(text="CALCULATOR")
    btn3.configure(text="C:")
    btn4.configure(text="GOOGLE")
    btn5.configure(text="BUTTON5")
    btn6.configure(text="BUTTON6")
    btn7.configure(text="BUTTON7")
    btn8.configure(text="RUNNING..")
    status_label.configure(foreground='red') # 레이블 색상 변경
    status_label.configure(text='버8 실행 중') # 레이블 텍스트 변경

def b9():
    win.destroy
    exit()


btn1 = ttk.Button(win, text="NOTEPAD", command=opn_note, width=8, padding= 25)   
btn1.place(x=60, y=30)

btn2 = ttk.Button(win, text="CALCULATOR", command=opn_calc, width=8, padding=25)   
btn2.place(x=240, y=30)

btn3 = ttk.Button(win, text="C:", command=opn_c, width=8, padding=25)   
btn3.place(x=420, y=30)

btn4 = ttk.Button(win, text="GOOGLE", command=opn_google, width=8, padding=25)   
btn4.place(x=600, y=30)

btn5 = ttk.Button(win, text="BUTTON5", command=b5, width=8, padding=25)   
btn5.place(x=60, y=110)

btn6 = ttk.Button(win, text="BUTTON6", command=b6, width=8, padding=25)   
btn6.place(x=240, y=110)

btn7 = ttk.Button(win, text="BUTTON7", command=b7, width=8, padding=25 )   
btn7.place(x=420, y=110)

btn8 = ttk.Button(win, text="BUTTON8", command=b8, width=8, padding=25)   
btn8.place(x=600, y=110)

exitbtn = ttk.Button(win, text="Exit", command=b9)
exitbtn.pack()


win.mainloop()

