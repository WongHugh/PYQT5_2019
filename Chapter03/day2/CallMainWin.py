#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-13 13:47
# @Author : leoyo
# @Email : #
# @File : CallMainWin.py
# @Project : PYQT5_UI
# @IDE : PyCharm
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from Chapter03.day2.MainWin import Ui_Form
import sys

class MainWin(QMainWindow,Ui_Form):

    def __init__(self):
        super(MainWin,self).__init__()
        self.setupUi(self)
        self.status = self.statusBar()
        self.status.showMessage('hello world!',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MainWin()
    mywin.show()
    sys.exit(app.exec_())

