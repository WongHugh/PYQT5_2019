#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 9:57
# @Author : leoyo
# @Email : #
# @File : qt0419_Qsilder.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Sliderdemo(QWidget):

    def __init__(self,parent=None):
        super(Sliderdemo,self).__init__(parent)
        self.setWindowTitle("Sliderdemo")
        self.resize(600,500)
        layout = QVBoxLayout()

        self.ll =QLabel("Hell PyQT5")
        self.ll.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.ll)

        self.s1 = QSlider(Qt.Horizontal)

        self.s1.setMinimum(10)
        self.s1.setMaximum(100)
        self.s1.setSingleStep(2)
        self.s1.setValue(100)
        self.s1.setTickPosition(QSlider.TicksBothSides)

        self.s1.setTickInterval(10)
        layout.addWidget(self.s1)

        self.s1.valueChanged.connect(self.valuechange)
        self.setLayout(layout)


    def valuechange(self):
        print("current slider value  = %s"%self.s1.value())
        size = self.s1.value()
        self.ll.setFont(QFont("Arial",size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sliderdemo = Sliderdemo()
    sliderdemo.show()
    sys.exit(app.exec_())

