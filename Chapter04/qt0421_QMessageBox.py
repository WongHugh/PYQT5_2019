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

class Qmessageboxdemo(QMainWindow):

    def __init__(self,parent = None):
        super(Qmessageboxdemo,self).__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        self.resize(800,600)

        self.mybutton = QPushButton( self )
        self.mybutton.setText( "点击弹出消息对话框" )
        self.mybutton.move( 50, 50 )
        self.mybutton.clicked.connect( self.msg )

    def msg(self):
        reply = QMessageBox.information(self,"标题","消息正文",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Qmessagebox = Qmessageboxdemo()
    Qmessagebox.show()
    sys.exit(app.exec_())
