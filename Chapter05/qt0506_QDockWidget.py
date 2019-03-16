#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 15:16
# @Author : leoyo
# @Email : #
# @File : qt0506_QDockWidget.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo( QMainWindow ):
    def __init__(self, parent=None):
        super( DockDemo, self ).__init__( parent )
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu( "File" )
        file.addAction( "New" )
        file.addAction( "save" )
        file.addAction( "quit" )
        self.items = QDockWidget( "Dockable", self )
        self.listWidget = QListWidget()
        self.listWidget.addItem( "item1" )
        self.listWidget.addItem( "item2" )
        self.listWidget.addItem( "item3" )
        self.items.setWidget( self.listWidget )
        self.items.setFloating( True )
        self.setCentralWidget( QTextEdit() )
        self.addDockWidget( Qt.RightDockWidgetArea, self.items )
        self.items.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.setLayout( layout )
        self.setWindowTitle( "Dock 例子" )


if __name__ == '__main__':
    app = QApplication( sys.argv )
    demo = DockDemo()
    demo.show()
    sys.exit( app.exec_() )