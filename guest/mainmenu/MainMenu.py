# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Guest\mainmenu\MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(93, 93, 93);")
        self.sidepanel_L = QtWidgets.QLabel(Dialog)
        self.sidepanel_L.setGeometry(QtCore.QRect(10, 10, 241, 581))
        self.sidepanel_L.setText("")
        self.sidepanel_L.setObjectName("sidepanel_L")
        self.sidepanel_R = QtWidgets.QLabel(Dialog)
        self.sidepanel_R.setGeometry(QtCore.QRect(760, 10, 241, 581))
        self.sidepanel_R.setText("")
        self.sidepanel_R.setObjectName("sidepanel_R")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(270, 10, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(26)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(238, 238, 238);")
        self.Title.setFrameShape(QtWidgets.QFrame.Box)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.GuestLoginFrame = QtWidgets.QFrame(Dialog)
        self.GuestLoginFrame.setGeometry(QtCore.QRect(530, 260, 191, 201))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        self.GuestLoginFrame.setFont(font)
        self.GuestLoginFrame.setStyleSheet("color: rgb(238, 238, 238);")
        self.GuestLoginFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.GuestLoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GuestLoginFrame.setObjectName("GuestLoginFrame")
        self.GuestLoginUsernameInput = QtWidgets.QLineEdit(self.GuestLoginFrame)
        self.GuestLoginUsernameInput.setGeometry(QtCore.QRect(20, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(8)
        self.GuestLoginUsernameInput.setFont(font)
        self.GuestLoginUsernameInput.setObjectName("GuestLoginUsernameInput")
        self.GuestloginUsernameLabel = QtWidgets.QLabel(self.GuestLoginFrame)
        self.GuestloginUsernameLabel.setGeometry(QtCore.QRect(20, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(12)
        self.GuestloginUsernameLabel.setFont(font)
        self.GuestloginUsernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuestloginUsernameLabel.setObjectName("GuestloginUsernameLabel")
        self.GuestloginPasswordLabel = QtWidgets.QLabel(self.GuestLoginFrame)
        self.GuestloginPasswordLabel.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(12)
        self.GuestloginPasswordLabel.setFont(font)
        self.GuestloginPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuestloginPasswordLabel.setObjectName("GuestloginPasswordLabel")
        self.GuestLoginPasswordInput = QtWidgets.QLineEdit(self.GuestLoginFrame)
        self.GuestLoginPasswordInput.setGeometry(QtCore.QRect(20, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        self.GuestLoginPasswordInput.setFont(font)
        self.GuestLoginPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.GuestLoginPasswordInput.setObjectName("GuestLoginPasswordInput")
        self.StaffLoginFrame = QtWidgets.QFrame(Dialog)
        self.StaffLoginFrame.setGeometry(QtCore.QRect(280, 260, 191, 201))
        self.StaffLoginFrame.setStyleSheet("color: rgb(238, 238, 238);")
        self.StaffLoginFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.StaffLoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StaffLoginFrame.setObjectName("StaffLoginFrame")
        self.StaffloginUsernameLabel = QtWidgets.QLabel(self.StaffLoginFrame)
        self.StaffloginUsernameLabel.setGeometry(QtCore.QRect(20, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(12)
        self.StaffloginUsernameLabel.setFont(font)
        self.StaffloginUsernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StaffloginUsernameLabel.setObjectName("StaffloginUsernameLabel")
        self.StaffLoginUsername = QtWidgets.QLineEdit(self.StaffLoginFrame)
        self.StaffLoginUsername.setGeometry(QtCore.QRect(20, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        self.StaffLoginUsername.setFont(font)
        self.StaffLoginUsername.setObjectName("StaffLoginUsername")
        self.StaffloginPasswordLabel = QtWidgets.QLabel(self.StaffLoginFrame)
        self.StaffloginPasswordLabel.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(12)
        self.StaffloginPasswordLabel.setFont(font)
        self.StaffloginPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StaffloginPasswordLabel.setObjectName("StaffloginPasswordLabel")
        self.StaffLoginPassword = QtWidgets.QLineEdit(self.StaffLoginFrame)
        self.StaffLoginPassword.setGeometry(QtCore.QRect(20, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        self.StaffLoginPassword.setFont(font)
        self.StaffLoginPassword.setInputMask("")
        self.StaffLoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.StaffLoginPassword.setObjectName("StaffLoginPassword")
        self.nologinbutton = QtWidgets.QPushButton(Dialog)
        self.nologinbutton.setGeometry(QtCore.QRect(530, 200, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.nologinbutton.setFont(font)
        self.nologinbutton.setStyleSheet("color: rgb(238, 238, 238);")
        self.nologinbutton.setObjectName("nologinbutton")
        self.guestloginbutton = QtWidgets.QPushButton(Dialog)
        self.guestloginbutton.setGeometry(QtCore.QRect(530, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.guestloginbutton.setFont(font)
        self.guestloginbutton.setStyleSheet("color: rgb(238, 238, 238);")
        self.guestloginbutton.setObjectName("guestloginbutton")
        self.staffloginbutton = QtWidgets.QPushButton(Dialog)
        self.staffloginbutton.setGeometry(QtCore.QRect(280, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.staffloginbutton.setFont(font)
        self.staffloginbutton.setStyleSheet("color: rgb(238, 238, 238);")
        self.staffloginbutton.setObjectName("staffloginbutton")
        self.StaffloginUsernameLabel_2 = QtWidgets.QLabel(Dialog)
        self.StaffloginUsernameLabel_2.setGeometry(QtCore.QRect(280, 200, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.StaffloginUsernameLabel_2.setFont(font)
        self.StaffloginUsernameLabel_2.setStyleSheet("color: rgb(238, 238, 238);")
        self.StaffloginUsernameLabel_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.StaffloginUsernameLabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.StaffloginUsernameLabel_2.setLineWidth(2)
        self.StaffloginUsernameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.StaffloginUsernameLabel_2.setObjectName("StaffloginUsernameLabel_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Title.setText(_translate("Dialog", "Collyers Booking System"))
        self.GuestloginUsernameLabel.setText(_translate("Dialog", "Username/email"))
        self.GuestloginPasswordLabel.setText(_translate("Dialog", "Password"))
        self.StaffloginUsernameLabel.setText(_translate("Dialog", "Username"))
        self.StaffloginPasswordLabel.setText(_translate("Dialog", "Password"))
        self.nologinbutton.setText(_translate("Dialog", "Continue as guest "))
        self.guestloginbutton.setText(_translate("Dialog", "Confirm login"))
        self.staffloginbutton.setText(_translate("Dialog", "Confirm login"))
        self.StaffloginUsernameLabel_2.setText(_translate("Dialog", "Staff login"))
