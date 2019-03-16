#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 11:30
# @Author : leoyo
# @Email : #
# @File : qt07_signall.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtCore import QObject,pyqtSignal


class signalcalss(QObject):
    signal_1 = pyqtSignal()
    signal_2 = pyqtSignal(int)

    def __init__(self,parent = None):
        super(signalcalss,self).__init__(parent)

        self.signal_1.connect(self.sin1call)
        self.signal_1.connect(self.sin2call)
        self.signal_2.connect(self.signal_1)

        self.signal_1.emit()
        self.signal_2.emit(1)

        self.signal_1.disconnect(self.sin1call)
        self.signal_1.disconnect(self.sin2call)
        self.signal_2.disconnect(self.signal_1)

        self.signal_1.connect(self.sin1call)
        self.signal_2.connect(self.sin1call)

        self.signal_1.emit()
        self.signal_2.emit(2)


    def sin1call(self):
        print("signal_111111 emit")

    def sin2call(self):
        print("signal_222222 emit")

if __name__ == '__main__':
    signal = signalcalss()
