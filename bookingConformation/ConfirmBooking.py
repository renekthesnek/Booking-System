# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\bookingConformation\ConfirmBooking.ui'
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
        self.Ticketconfirmationarea = QtWidgets.QScrollArea(Dialog)
        self.Ticketconfirmationarea.setGeometry(QtCore.QRect(20, 150, 501, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ticketconfirmationarea.setFont(font)
        self.Ticketconfirmationarea.setStyleSheet("color: rgb(238, 238, 238);\n"
"background-color: rgb(111, 111, 111);")
        self.Ticketconfirmationarea.setFrameShape(QtWidgets.QFrame.Box)
        self.Ticketconfirmationarea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Ticketconfirmationarea.setLineWidth(2)
        self.Ticketconfirmationarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Ticketconfirmationarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Ticketconfirmationarea.setWidgetResizable(True)
        self.Ticketconfirmationarea.setObjectName("Ticketconfirmationarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 423))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SeatBookedLabelTemplate = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SeatBookedLabelTemplate.setGeometry(QtCore.QRect(10, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.SeatBookedLabelTemplate.setFont(font)
        self.SeatBookedLabelTemplate.setObjectName("SeatBookedLabelTemplate")
        self.DropDownTemplate = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.DropDownTemplate.setGeometry(QtCore.QRect(160, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.DropDownTemplate.setFont(font)
        self.DropDownTemplate.setObjectName("DropDownTemplate")
        self.DropDownTemplate.addItem("")
        self.DropDownTemplate.addItem("")
        self.DropDownTemplate.addItem("")
        self.PriceLabelTemplate = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.PriceLabelTemplate.setGeometry(QtCore.QRect(340, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(9)
        self.PriceLabelTemplate.setFont(font)
        self.PriceLabelTemplate.setObjectName("PriceLabelTemplate")
        self.Ticketconfirmationarea.setWidget(self.scrollAreaWidgetContents)
        self.ConfirmBookingButton = QtWidgets.QPushButton(Dialog)
        self.ConfirmBookingButton.setGeometry(QtCore.QRect(630, 530, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.ConfirmBookingButton.setFont(font)
        self.ConfirmBookingButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.ConfirmBookingButton.setObjectName("ConfirmBookingButton")
        self.CustomerDetailsFrame = QtWidgets.QFrame(Dialog)
        self.CustomerDetailsFrame.setGeometry(QtCore.QRect(550, 149, 411, 361))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CustomerDetailsFrame.setFont(font)
        self.CustomerDetailsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.CustomerDetailsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CustomerDetailsFrame.setLineWidth(2)
        self.CustomerDetailsFrame.setObjectName("CustomerDetailsFrame")
        self.UsernameLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.UsernameLabel.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.UsernameLabel.setFont(font)
        self.UsernameLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.UsernameInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.UsernameInput.setGeometry(QtCore.QRect(110, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.UsernameInput.setFont(font)
        self.UsernameInput.setObjectName("UsernameInput")
        self.FullNameLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.FullNameLabel.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.FullNameLabel.setFont(font)
        self.FullNameLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.FullNameLabel.setObjectName("FullNameLabel")
        self.FullNameInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.FullNameInput.setGeometry(QtCore.QRect(110, 80, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.FullNameInput.setFont(font)
        self.FullNameInput.setObjectName("FullNameInput")
        self.PasswordLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.PasswordLabel.setGeometry(QtCore.QRect(10, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.PasswordInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.PasswordInput.setGeometry(QtCore.QRect(140, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setObjectName("PasswordInput")
        self.ConfirmPasswordLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.ConfirmPasswordLabel.setGeometry(QtCore.QRect(10, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.ConfirmPasswordLabel.setFont(font)
        self.ConfirmPasswordLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.ConfirmPasswordLabel.setObjectName("ConfirmPasswordLabel")
        self.ConfirmPasswordInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.ConfirmPasswordInput.setGeometry(QtCore.QRect(140, 310, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.ConfirmPasswordInput.setFont(font)
        self.ConfirmPasswordInput.setObjectName("ConfirmPasswordInput")
        self.EmailLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.EmailLabel.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.EmailLabel.setFont(font)
        self.EmailLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.EmailLabel.setObjectName("EmailLabel")
        self.EmailInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.EmailInput.setGeometry(QtCore.QRect(110, 130, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.EmailInput.setFont(font)
        self.EmailInput.setObjectName("EmailInput")
        self.PhoneNumberLabel = QtWidgets.QLabel(self.CustomerDetailsFrame)
        self.PhoneNumberLabel.setGeometry(QtCore.QRect(10, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.PhoneNumberLabel.setFont(font)
        self.PhoneNumberLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.PhoneNumberLabel.setObjectName("PhoneNumberLabel")
        self.PhoneNumberlInput = QtWidgets.QLineEdit(self.CustomerDetailsFrame)
        self.PhoneNumberlInput.setGeometry(QtCore.QRect(140, 180, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.PhoneNumberlInput.setFont(font)
        self.PhoneNumberlInput.setObjectName("PhoneNumberlInput")
        self.LoginDisplay = QtWidgets.QLabel(Dialog)
        self.LoginDisplay.setGeometry(QtCore.QRect(830, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(10)
        self.LoginDisplay.setFont(font)
        self.LoginDisplay.setStyleSheet("color: rgb(238, 238, 238);")
        self.LoginDisplay.setObjectName("LoginDisplay")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 601, 81))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 238);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SeatBookedLabelTemplate.setText(_translate("Dialog", "Seat Placeholder"))
        self.DropDownTemplate.setItemText(0, _translate("Dialog", "Normal Ticket"))
        self.DropDownTemplate.setItemText(1, _translate("Dialog", "Reduced Price Ticket"))
        self.DropDownTemplate.setItemText(2, _translate("Dialog", "Special Ticket"))
        self.PriceLabelTemplate.setText(_translate("Dialog", "price Placeholder"))
        self.ConfirmBookingButton.setText(_translate("Dialog", "Confirm booking"))
        self.UsernameLabel.setText(_translate("Dialog", "Username:"))
        self.FullNameLabel.setText(_translate("Dialog", "Full Name:"))
        self.PasswordLabel.setText(_translate("Dialog", "Password:"))
        self.ConfirmPasswordLabel.setText(_translate("Dialog", "Confirm Password:"))
        self.EmailLabel.setText(_translate("Dialog", "Email:"))
        self.PhoneNumberLabel.setText(_translate("Dialog", "Phone Number:"))
        self.LoginDisplay.setText(_translate("Dialog", "You Are Not Logged In"))
        self.label.setText(_translate("Dialog", "Confirm Booking"))
