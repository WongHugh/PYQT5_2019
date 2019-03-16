#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-14 15:34
# @Author : leoyo
# @Email : #
# @File : qt0507_QMultiDoc.py
# @Project : PYQT5_UI
# @IDE : PyCharm

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    count = 0
    def __init__(self,parent =None):
        super(MainWindow,self).__init__(parent)
        self.mdi =QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.addAction("close all")
        file.addAction("quit")

        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle(self.__class__.__name__)

    def windowaction(self,q):
        print("triggered")

        if q.text() =="New":
            MainWindow.count = MainWindow.count+1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "close all":
            MainWindow.count = 0
            self.mdi.closeAllSubWindows()

        if q.text() == "quit":
            print("closed")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())