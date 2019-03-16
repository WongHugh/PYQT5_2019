#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 15:10
# @Author : leoyo
# @Email : #
# @File : qt08_winStyle02.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class mywindow(QMainWindow):

    def __init__(self,parent = None):
        super(mywindow,self).__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setStyleSheet("background-color:blue;")


    def showMaximized(self):

        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)
        self.show()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    my = mywindow()
    my.showMaximized()
    # my.show()
    sys.exit(app.exec_())