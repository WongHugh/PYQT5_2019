#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 8:34
# @Author : leoyo
# @Email : #
# @File : qt0414_Qbutton.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        layout = QVBoxLayout()
        self.btn1 = QPushButton('Button1')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnstate)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton("Button2")
        self.btn2.clicked.connect(lambda :self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)

        self.btn3 = QPushButton("Dissabled")
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda :self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)





        self.setLayout(layout)
        self.setWindowTitle("button demo")
        self.resize(300,300)


    def btnstate(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self,btn):
        print("clicked button is "+btn.text())

if __name__ == '__main__':
    app =QApplication(sys.argv)
    myform  = Form()
    myform.show()
    sys.exit(app.exec_())

