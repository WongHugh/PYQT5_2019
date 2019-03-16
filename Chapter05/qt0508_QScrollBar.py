# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt0508_QScrollBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from Chapter05.qt0508_QScrollBar_UI import Ui_Example

class Example(QWidget,Ui_Example):
    def __init__(self,parent = None):
        super(Example,self).__init__(parent)
        self.setupUi(self)
        self.verticalScrollBar_3.sliderMoved['int'].connect(self.sliderval)
        self.verticalScrollBar_2.sliderMoved['int'].connect(self.sliderval)
        self.verticalScrollBar.sliderMoved['int'].connect(self.sliderval)

    def sliderval(self):
        print(self.verticalScrollBar.value(),self.verticalScrollBar_2.value(),self.verticalScrollBar_3.value())
        palette = QPalette()
        c =QColor(self.verticalScrollBar.value(),self.verticalScrollBar_2.value(),self.verticalScrollBar_3.value(),255)
        palette.setColor(QPalette.Foreground,c)
        self.label.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())