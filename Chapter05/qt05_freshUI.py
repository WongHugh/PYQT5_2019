#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-15 9:41
# @Author : leoyo
# @Email : #
# @File : qt05_freshUI.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout
import sys
import time


class WinForm( QWidget ):

    def __init__(self, parent=None):
        super( WinForm, self ).__init__( parent )
        self.setWindowTitle( "实时刷新界面例子" )
        self.listFile = QListWidget()
        self.btnStart = QPushButton( '开始' )
        layout = QGridLayout( self )
        layout.addWidget( self.listFile, 0, 0, 1, 2 )
        layout.addWidget( self.btnStart, 1, 1 )
        self.btnStart.clicked.connect( self.slotAdd )
        self.setLayout( layout )

    def slotAdd(self):
        for n in range( 100 ):
            str_n = 'File index {0}'.format( n )
            self.listFile.addItem( str_n )
            QApplication.processEvents()
            time.sleep( 2 )


if __name__ == "__main__":
    app = QApplication( sys.argv )
    form = WinForm()
    form.show()
    sys.exit( app.exec_() )