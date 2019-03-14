#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 13:41
# @Author : leoyo
# @Email : #
# @File : qt0434_Qmenu.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MenuDemo(QMainWindow):

    def __init__(self,parent= None):
        super(MenuDemo,self).__init__(parent)

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")

        file.addAction("New")

        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("paste")
        edit.addAction("copy")
        quit = QAction("Quit",self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)
        self.setLayout(layout)
        self.setWindowTitle(self.__class__.__name__)

    def processtrigger(self,q):
        print(q.text()+"is triggered")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menudemo = MenuDemo()
    menudemo.show()
    sys.exit(app.exec_())


