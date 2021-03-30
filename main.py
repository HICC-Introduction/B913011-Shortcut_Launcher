# B913011 Shortcut_Launcher
import tkinter as tk
import os
import webbrowser

win = tk.Tk()   
win.title("KMS - Shortcut Launcher")   
win.geometry("800x200+100+100")
win.resizable(False, False)

def opn_note():
    os.system("notepad.exe")

def opn_calc():
    os.system("calc.exe")

def opn_c():
    os.startfile("c:")

def opn_google():
    webbrowser.open("https://www.google.co.kr/")
"""    
def btn_5():
    
def btn_6():
    
def btn_7():
    
def btn_8():
    
"""
def btn_exit():
    win.destroy
    exit()


btn1 = tk.Button(win, text="NOTEPAD", command=opn_note, width=15, height=4)   
btn1.place(x=70, y=30)

btn2 = tk.Button(win, text="CALCULATOR", command=opn_calc, width=15, height=4)   
btn2.place(x=250, y=30)

btn3 = tk.Button(win, text="C:", command=opn_c, width=15, height=4)   
btn3.place(x=430, y=30)

btn4 = tk.Button(win, text="GOOGLE", command=opn_google, width=15, height=4)   
btn4.place(x=610, y=30)

btn5 = tk.Button(win, text="BUTTON5", width=15, height=4)   
btn5.place(x=70, y=110)

btn6 = tk.Button(win, text="BUTTON6", width=15, height=4)   
btn6.place(x=250, y=110)

btn7 = tk.Button(win, text="BUTTON7", width=15, height=4)   
btn7.place(x=430, y=110)

btn8 = tk.Button(win, text="BUTTON8", width=15, height=4)   
btn8.place(x=610, y=110)

exitbtn = tk.Button(win, text="Exit", command=btn_exit, width=10)
exitbtn.pack()


win.mainloop()