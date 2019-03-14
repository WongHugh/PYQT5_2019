#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-13 10:46
# @Author : leoyo
# @Email : #
# @File : CallMainForm.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
import sys
from Chapter03.day2.MainForm import Ui_MainWindow
from Chapter03.day2.ChildrenForm import Ui_Form

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)
        self.child = ChildrenFrom()
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childshow)

    def childshow(self):
        self.gridLayout.addWidget(self.child)
        self.child.show()


    def openMsg(self):
        file,ok = QFileDialog.getOpenFileNames(self,'打开','C:\\','ALL Files (*);;Text Files(*.txt)')
        self.statusbar.showMessage(file)

class ChildrenFrom(QWidget,Ui_Form):
    def __init__(self):
        super(ChildrenFrom,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

