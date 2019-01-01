# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PERFOMANCE.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 800)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pencil_choose = QtWidgets.QPushButton(self.centralwidget)
        self.pencil_choose.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.pencil_choose.setFont(font)
        self.pencil_choose.setObjectName("pencil_choose")
        self.set_color_pencil = QtWidgets.QPushButton(self.centralwidget)
        self.set_color_pencil.setGeometry(QtCore.QRect(50, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.set_color_pencil.setFont(font)
        self.set_color_pencil.setObjectName("set_color_pencil")
        self.set_size_pencil = QtWidgets.QPushButton(self.centralwidget)
        self.set_size_pencil.setGeometry(QtCore.QRect(40, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.set_size_pencil.setFont(font)
        self.set_size_pencil.setObjectName("set_size_pencil")
        self.pencil_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pencil_clear.setGeometry(QtCore.QRect(50, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pencil_clear.setFont(font)
        self.pencil_clear.setObjectName("pencil_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pencil_choose.setText(_translate("MainWindow", "Карандаш"))
        self.set_color_pencil.setText(_translate("MainWindow", "Цвет"))
        self.set_size_pencil.setText(_translate("MainWindow", "Толщина: 1"))
        self.pencil_clear.setText(_translate("MainWindow", "Очистить"))

