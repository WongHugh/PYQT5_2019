#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 14:03
# @Author : leoyo
# @Email : #
# @File : datedialog.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateDialog(QDialog):

    def __init__(self,parent = None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle(self.__class__.__name__)


        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent =None):
        diglog = DateDialog(parent)
        result = diglog.exec_()
        date = diglog.dateTime()
        return (date.date(),date.time(),result == QDialog.Accepted)
