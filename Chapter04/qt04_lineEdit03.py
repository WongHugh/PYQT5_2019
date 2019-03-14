#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-13 16:57
# @Author : leoyo
# @Email : #
# @File : qt04_lineEdit02.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class lineEditDemo(QWidget):
    def __init__(self,parent = None):
        super(lineEditDemo,self).__init__(parent)
        self.setWindowTitle("QLineEdit 例子")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDateLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask("AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow("数字掩码",pIPLineEdit)
        flo.addRow("MAC掩码",pMACLineEdit)
        flo.addRow("日期掩码",pDateLineEdit)
        flo.addRow("许可证掩码",pLicenseLineEdit)

        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())


