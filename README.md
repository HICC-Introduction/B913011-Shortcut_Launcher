# Python GUI - Shortcut Launcher

## 목표 및 목적
* Turbo laucher의 기능을 간략하게 구현할 수 있도록 한다.
* 버튼은 총 2x4 그리드 형식의 8가지 버튼을 가지고있고 
* 각 버튼은 메모장, 계산기, c: 폴더, google.com을 실행시킬 수 있고 나머지 4개의 버튼은 임의 지정한다.
* 실행 창의 크기는 800x200 이며 크기조정은 불가능 하다.
* 본 프로그램은 윈도우 운영체제에서 실행을 기반으로 개발한다.
### 문제 분석
  
* 최종 목적 : 단축키 실행 프로그램인 Shortcut Launcher를 완성한다.
    * 상위 목적 : GUI에 버튼을 구현한다.
        * 버튼 구현
        * 버튼의 가독성
    * 상위 목적 : GUI에 버튼을 눌렀을 때, 응용프로그램을 실행시킨다.
        * 누르기 전부터 예상한 실행이 되도록 한다.

## 개발 사양

### 하드웨어
* CPU : Apple M1칩 8코어 CPU(성능 코어 4개 및 효율 코어 4개) 7코어 GPU 16코어 Neural Engine
* RAM : 8GB
* HDD/SSD : APPLE SSD AP0256Q
* GPU : Apple M1

### 소프트웨어
* OS : Mac OS BigSur
* 개발 스택 : Tkinter (블로그, 유투브에 정보가 많음)
* 개발 프로그램 : PyCharm 
* 개발 언어 : [Python v3.8.2]

### 코드룰
* 예시 프로그램

```
    # 변수명
    tst_var = 13

    # 클래스명
    class tst_class:
        def __init__(self):
            # 프로퍼티명
            self.tstProperty = 41

        # 메소드명
        def tst_method(self):
            print(self.tstProperty)
    
    if __name__ == "__main__":
        tst_var = tst_class(43)
        tst_var.tst_method()
```

  
