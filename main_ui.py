# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(580, 20, 193, 32))
        self.addButton.setObjectName("addButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 20, 193, 32))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 20, 287, 26))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 80, 591, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.notifications_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.notifications_layout.setContentsMargins(0, 0, 0, 0)
        self.notifications_layout.setObjectName("notifications_layout")
        self.delete_missed_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_missed_btn.setGeometry(QtCore.QRect(360, 50, 331, 31))
        self.delete_missed_btn.setObjectName("delete_missed_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
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
        self.addButton.setText(_translate("MainWindow", "добавить напоминание"))
        self.pushButton.setText(_translate("MainWindow", "показать"))
        self.delete_missed_btn.setText(_translate("MainWindow", "удалить все пропущенные напоминания"))
