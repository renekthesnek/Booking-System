# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\StaffMainMenu\StaffConsole.ui'
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
        Dialog.setStyleSheet("background-color: rgb(93, 93, 93);")
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
        self.loggedindisplay = QtWidgets.QLabel(Dialog)
        self.loggedindisplay.setGeometry(QtCore.QRect(820, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loggedindisplay.setFont(font)
        self.loggedindisplay.setStyleSheet("color: rgb(238, 238, 238);")
        self.loggedindisplay.setObjectName("loggedindisplay")
        self.ToPeformanceMenuButton = QtWidgets.QPushButton(Dialog)
        self.ToPeformanceMenuButton.setGeometry(QtCore.QRect(150, 220, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.ToPeformanceMenuButton.setFont(font)
        self.ToPeformanceMenuButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.ToPeformanceMenuButton.setObjectName("ToPeformanceMenuButton")
        self.EditSeatsForPeformanceButton = QtWidgets.QPushButton(Dialog)
        self.EditSeatsForPeformanceButton.setGeometry(QtCore.QRect(530, 220, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.EditSeatsForPeformanceButton.setFont(font)
        self.EditSeatsForPeformanceButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditSeatsForPeformanceButton.setObjectName("EditSeatsForPeformanceButton")
        self.DataViewerButton = QtWidgets.QPushButton(Dialog)
        self.DataViewerButton.setGeometry(QtCore.QRect(530, 350, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.DataViewerButton.setFont(font)
        self.DataViewerButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.DataViewerButton.setObjectName("DataViewerButton")
        self.ProcessBookingsButton = QtWidgets.QPushButton(Dialog)
        self.ProcessBookingsButton.setGeometry(QtCore.QRect(150, 350, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.ProcessBookingsButton.setFont(font)
        self.ProcessBookingsButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.ProcessBookingsButton.setObjectName("ProcessBookingsButton")
        self.BackToMenuButton = QtWidgets.QPushButton(Dialog)
        self.BackToMenuButton.setGeometry(QtCore.QRect(340, 490, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.BackToMenuButton.setFont(font)
        self.BackToMenuButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.BackToMenuButton.setObjectName("BackToMenuButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Title.setText(_translate("Dialog", "Staff Console "))
        self.loggedindisplay.setText(_translate("Dialog", "logged in as:"))
        self.ToPeformanceMenuButton.setText(_translate("Dialog", "Create/Edit Peformances"))
        self.EditSeatsForPeformanceButton.setText(_translate("Dialog", "Edit Seats for Peformance"))
        self.DataViewerButton.setText(_translate("Dialog", "Data Viewer"))
        self.ProcessBookingsButton.setText(_translate("Dialog", "Process Bookings"))
        self.BackToMenuButton.setText(_translate("Dialog", "Return To Menu"))
