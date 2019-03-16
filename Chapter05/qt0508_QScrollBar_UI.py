# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt0508_QScrollBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Example(object):
    def setupUi(self, Example):
        Example.setObjectName("Example")
        Example.resize(400, 300)
        self.widget = QtWidgets.QWidget(Example)
        self.widget.setGeometry(QtCore.QRect(60, 50, 275, 181))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setMaximum(255)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar_2.setMaximum(255)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalLayout.addWidget(self.verticalScrollBar_2)
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar_3.setMaximum(255)
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.horizontalLayout.addWidget(self.verticalScrollBar_3)

        self.retranslateUi(Example)

        QtCore.QMetaObject.connectSlotsByName(Example)

    def retranslateUi(self, Example):
        _translate = QtCore.QCoreApplication.translate
        Example.setWindowTitle(_translate("Example", "QScrollBar例子"))
        self.label.setText(_translate("Example", " 拖动滑块改变颜色     "))

