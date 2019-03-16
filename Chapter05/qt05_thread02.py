#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 9:24
# @Author : leoyo
# @Email : #
# @File : qt05_thread02.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0

class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(2000000000):
            pass
        self.trigger.emit()

def countTime():
    global sec
    sec += 1
    lcdNumber.display(sec)

def work():
    timer.start(1000)
    workThread.start()

    workThread.trigger.connect(timestop)

def timestop():
    timer.stop()
    print("运行结束用时",lcdNumber.value())
    global sec
    sec = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(600,400)

    layout = QVBoxLayout(top)
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    workThread =WorkThread()
    button.clicked.connect(work)

    timer.timeout.connect(countTime)

    top.show()
    sys.exit(app.exec_())