#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 10:14
# @Author : leoyo
# @Email : #
# @File : qt0420_Qdialog01.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QDialogdemo01(QMainWindow):

    def __init__(self,parent = None):
        super(QDialogdemo01,self).__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        self.resize(800,600)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50,50)
        self.btn.clicked.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton("ok",dialog)
        btn.move(50,50)
        dialog.setWindowTitle(sys._getframe().f_code.co_name)
        self.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qdiaglgdemo = QDialogdemo01()
    qdiaglgdemo.show()
    sys.exit(app.exec_())
