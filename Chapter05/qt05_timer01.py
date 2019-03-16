#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 8:37
# @Author : leoyo
# @Email : #
# @File : qt05_timer01.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
import sys

class WinForm(QWidget):

    def __init__(self,parent =None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        self.listFile = QListWidget()
        self.label = QLabel("显示当前时间")
        self.startBtn = QPushButton("开始")
        self.endBtn = QPushButton("结束")
        layout = QGridLayout(self)


        self.timer = QTimer(self)

        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,2)

        self.startBtn.clicked.connect(self.StartTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def StartTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WinForm()
    example.show()
    sys.exit(app.exec_())


