import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import QCoreApplication
import webbrowser
import subprocess
import os

btn_name = [["NOTEPAD", "CALCULATOR", "TERMINAL", "GOOGLE"], ["5", "6", "7", "8"]]

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 200)   # fix size window 800x200
        self.setWindowTitle("KMS - Shortcut Launcher") # change name of window
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        
        for x in range(2):
            for y in range(4):
                a = x
                b = y
                btn = QPushButton(btn_name[a][b]) 
                grid_layout.addWidget(btn, x, y)
                if a == 0:
                    if b == 0:
                        btn.clicked.connect(self.opn_note)
                    elif b == 1:
                        btn.clicked.connect(self.opn_calc)
                    elif b == 2:
                        btn.clicked.connect(self.opn_terminal)
                    else:
                        btn.clicked.connect(self.opn_google)
        
    def opn_note(self):
        os.system("/System/Applications/Notes.app/Contents/MacOS/Notes") # execution fuction for mac os

    def opn_calc(self):
        os.system("/System/Applications/Calculator.app/Contents/MacOS/Calculator") # execution fuction for mac os

    def opn_terminal(self):
        os.system("/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal") # in Mac os Terminal roll c: 

    def opn_google(self):
        webbrowser.open("http://www.google.co.kr/")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    app.exec_()