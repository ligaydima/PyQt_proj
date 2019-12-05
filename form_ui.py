# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(40, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label.setObjectName("label")
        self.enter_title = QtWidgets.QLineEdit(Form)
        self.enter_title.setGeometry(QtCore.QRect(170, 20, 221, 21))
        self.enter_title.setObjectName("enter_title")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 291, 20))
        self.label_2.setObjectName("label_2")
        self.enter_prior = QtWidgets.QSpinBox(Form)
        self.enter_prior.setGeometry(QtCore.QRect(310, 60, 48, 24))
        self.enter_prior.setObjectName("enter_prior")
        self.enter_time = QtWidgets.QDateTimeEdit(Form)
        self.enter_time.setGeometry(QtCore.QRect(170, 100, 194, 24))
        self.enter_time.setObjectName("enter_time")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.label_3.setObjectName("label_3")
        self.choose_img_btn = QtWidgets.QPushButton(Form)
        self.choose_img_btn.setGeometry(QtCore.QRect(0, 140, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.choose_img_btn.setFont(font)
        self.choose_img_btn.setAutoDefault(True)
        self.choose_img_btn.setDefault(False)
        self.choose_img_btn.setFlat(False)
        self.choose_img_btn.setObjectName("choose_img_btn")
        self.img_name_lbl = QtWidgets.QLabel(Form)
        self.img_name_lbl.setGeometry(QtCore.QRect(20, 200, 321, 31))
        self.img_name_lbl.setText("")
        self.img_name_lbl.setObjectName("img_name_lbl")

        self.retranslateUi(Form)
        self.buttonBox.accepted.connect(Form.accept)
        self.buttonBox.rejected.connect(Form.reject)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dialog"))
        self.label.setText(_translate("Form", "Название напоминания"))
        self.label_2.setText(_translate("Form", "Приоритет(чем больше число, тем меньше)"))
        self.label_3.setText(_translate("Form", "Время напоминания"))
        self.choose_img_btn.setText(_translate("Form", "выбрать картинку(опционально)"))
