# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 166)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 371, 101))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.doubleSpinBox_return_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_return_min.setObjectName("doubleSpinBox_return_min")
        self.gridLayout.addWidget(self.doubleSpinBox_return_min, 1, 0, 1, 1)
        self.doubleSpinBox_return_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_return_max.setObjectName("doubleSpinBox_return_max")
        self.gridLayout.addWidget(self.doubleSpinBox_return_max, 1, 1, 1, 1)
        self.doubleSpinBox_maxdrawdown_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_maxdrawdown_min.setObjectName("doubleSpinBox_maxdrawdown_min")
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 0, 1, 1)
        self.doubleSpinBox_maxdrawdown_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_maxdrawdown_max.setObjectName("doubleSpinBox_maxdrawdown_max")
        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_max, 2, 1, 1, 1)
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_min, 3, 0, 1, 1)
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        self.gridLayout.addWidget(self.doubleSpinBox_sharp_max, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.doubleSpinBox_sharp_min)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.doubleSpinBox_return_min, self.doubleSpinBox_return_max)
        MainWindow.setTabOrder(self.doubleSpinBox_return_max, self.doubleSpinBox_maxdrawdown_min)
        MainWindow.setTabOrder(self.doubleSpinBox_maxdrawdown_min, self.doubleSpinBox_maxdrawdown_max)
        MainWindow.setTabOrder(self.doubleSpinBox_maxdrawdown_max, self.doubleSpinBox_sharp_min)
        MainWindow.setTabOrder(self.doubleSpinBox_sharp_min, self.doubleSpinBox_sharp_max)
        MainWindow.setTabOrder(self.doubleSpinBox_sharp_max, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "收益"))
        self.label_2.setText(_translate("MainWindow", "最大回撤"))
        self.label_3.setText(_translate("MainWindow", "&sharp比"))
        self.label_4.setText(_translate("MainWindow", "最小值"))
        self.label_5.setText(_translate("MainWindow", "最大值"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
