import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import *  
import webbrowser
import os

btn_name = [["NOTEPAD", "CALCULATOR", "TERMINAL", "GOOGLE"], ["5", "6", "7", "8"]]
btn_icon = ["note.png", "calc.png", "terminal.png", "google.png"]

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
                if x == 0:  # 1행에 있는 버튼들만 열에따라 아이콘을 넣도록 배열에 .png파일 이름 저장
                    btn.setIcon(QIcon(btn_icon[y]))
                    if y == 0:  # 1행에 있는 버튼들 열에 따라 각각 클릭되었을때 이벤트를 연결해둠
                        btn.clicked.connect(self.opn_note)
                    elif y == 1:
                        btn.clicked.connect(self.opn_calc)
                    elif y == 2:
                        btn.clicked.connect(self.opn_terminal)
                    else:
                        btn.clicked.connect(self.opn_google)
        
    def opn_note(self): # Mac os에서 메모를 여는 경로
        os.system("/System/Applications/Notes.app/Contents/MacOS/Notes")

    def opn_calc(self): # Mac os에서 계산기를 여는 경로
        os.system("/System/Applications/Calculator.app/Contents/MacOS/Calculator")

    def opn_terminal(self): # Mac os에서 폴더역할인 디렉토리는 열수 없음 터미널로 대체
        os.system("/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal")

    def opn_google(self): # 웹브라우져로 google을 여는 함수
        webbrowser.open("http://www.google.co.kr/")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    app.exec_()