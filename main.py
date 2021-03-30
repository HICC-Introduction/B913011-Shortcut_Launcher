import sys
import webbrowser
import os
from PyQt5.QtWidgets import *

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 200)
        self.setWindowTitle("KMS - Shortcut Launcher")

        self.btn_note = QPushButton("NOTEPAD", self)
        self.btn_note.move(20, 20)
        self.btn_note.resize(100, 50)
        self.btn_note.clicked.connect(self.opn_note)

        self.btn_calc = QPushButton("CALC", self)
        self.btn_calc.move(150, 20)
        self.btn_calc.resize(100, 50)
        self.btn_calc.clicked.connect(self.opn_calc)

        self.btn_cfold = QPushButton("C:", self)
        self.btn_cfold.move(280, 20)
        self.btn_cfold.resize(100, 50)
        self.btn_cfold.clicked.connect(self.opn_cfold)

        self.btn_google = QPushButton("GOOGLE", self)
        self.btn_google.move(410, 20)
        self.btn_google.resize(100, 50)
        self.btn_google.clicked.connect(self.opn_google)

        self.btn_5 = QPushButton("Button 5", self)
        self.btn_5.move(20, 80)
        self.btn_5.resize(100, 50)
        #self.btn_5.clicked.connect(self.opn_note)

        self.btn_6 = QPushButton("Button 6", self)
        self.btn_6.move(150, 80)
        self.btn_6.resize(100, 50)
        #self.btn_6.clicked.connect(self.opn_note)

        self.btn_7 = QPushButton("Button 7", self)
        self.btn_7.move(280, 80)
        self.btn_7.resize(100, 50)
        #self.btn_7.clicked.connect(self.opn_note)

        self.btn_8 = QPushButton("Button 8", self)
        self.btn_8.move(410, 80)
        self.btn_8.resize(100, 50)
        #self.btn_8.clicked.connect(self.opn_note)

    def opn_note():
        os.system("notepad.exe")

    def opn_calc():
        os.system("calc.exe")

    def opn_cfold():
        os.startfile("c:")

    def opn_google(self):
        webbrowser.open("http://www.google.co.kr/")


app = QApplication(sys.argv)
win = Win()
win.show()
app.exec_()