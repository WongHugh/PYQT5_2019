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
        pIntlineEdit = QLineEdit()
        pDoublelineEdit = QLineEdit()
        pVailidatorLineEdit = QLineEdit()

        flo.addRow("整型",pIntlineEdit)
        flo.addRow("浮点型",pDoublelineEdit)
        flo.addRow("字母和数字",pVailidatorLineEdit)

        pIntlineEdit.setPlaceholderText("整型")
        pDoublelineEdit.setPlaceholderText("浮点型")
        pVailidatorLineEdit.setPlaceholderText("字母和数字")

        # 整型，范围【1,99】
        pIntValidator =QIntValidator(self)
        pIntValidator.setRange(1,99)

        #浮点型,范围 【-360,360】， 精度小数点后两位
        pDoubleValidtor = QDoubleValidator(self)
        pDoubleValidtor.setRange(-360,360)
        pDoubleValidtor.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidtor.setDecimals(2)

        #字母和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        pValidtor = QRegExpValidator(self)
        pValidtor.setRegExp(reg)

        # 设置验证器

        pIntlineEdit.setValidator(pIntValidator)
        pDoublelineEdit.setValidator(pDoubleValidtor)
        pVailidatorLineEdit.setValidator(pValidtor)


        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())


