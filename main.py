import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import *  
import webbrowser
import os

def opn_note(): # 메모장 실행 함수
        os.system("notepad.exe")

def opn_calc(): # 계산기 실행 함수
        os.system("calc.exe")

def opn_cfold(): # c: 폴더 여는 함수
        os.startfile("c:")

def opn_google(): # 웹브라우져로 google을 여는 함수
        webbrowser.open("http://www.google.co.kr/")

btn_name = [["NOTEPAD", "CALCULATOR", "C:", "GOOGLE"], ["5", "6", "7", "8"]] # 버튼 이름 저장
btn_icon = ["note.png", "calc.png", "cfold.png", "google.png"] # 버튼 아이콘 이름 저장
btn_func = [opn_note, opn_calc, opn_cfold, opn_google] # 버튼 함수 이름 저장

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 200)   # 창의 크기를 800x200 로 고정
        self.setWindowTitle("KMS - Shortcut Launcher") # 생성한 창의 이름 설정
        grid_layout = QGridLayout()
        self.setLayout(grid_layout) # 버튼을 그리드로 구현하기 위해 적용
        
        for row in range(2): # 2행
            for col in range(4): # 4열
                x = row # for문 인자가 배열의 인덱스로 들어가면 작동하지않아서 대체
                y = col
                btn = QPushButton(btn_name[x][y]) # 버튼의 이름을 2x4의 배열에 저장해둠
                btn.setMaximumHeight(100)   # 창의 크기에 맞게 최대 100의 높이를 가지게 설정
                grid_layout.addWidget(btn, row, col)    # 버튼은 그리드를 따라 2x4의 형태를 가짐
                if x == 0:  # 1행에 있는 버튼들만 해당
                    btn.setIcon(QIcon(btn_icon[y])) # 열에 따라 아이콘을 넣도록 배열에 .png파일 이름 저장
                    btn.clicked.connect(btn_func[y]) # 열에 따라 각각 클릭되었을때 이벤트를 배열에 이름 저장
                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    app.exec_()