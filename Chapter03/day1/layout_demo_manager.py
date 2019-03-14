#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-12 15:16
# @Author : leoyo
# @Email : #
# @File : layout_demo_manager.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication
from Chapter03.day1.layout_demo import Ui_MainWindow

class LayoutDemo(QMainWindow,Ui_MainWindow):
    '''
    class documenation goes here
    '''
    def __init__(self,parent = None):
        '''
        Constructor
        @:param reference to the parent widget
        @:type Qwidget
        '''
        super(LayoutDemo,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        '''
        Slot documentation goes here

        '''

        print('收益_min:',self.doubleSpinBox_return_min.text())
        print('收益_max:',self.doubleSpinBox_return_max.text())
        print('最大回撤_min:',self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:',self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:',self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:',self.doubleSpinBox_sharp_max.text())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
