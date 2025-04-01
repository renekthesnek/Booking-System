# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Booking-System\Staff\CreateEdit\CreateEditConsole.ui'
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
        self.Title.setGeometry(QtCore.QRect(260, 10, 461, 71))
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
        self.AddPeformanceFrame = QtWidgets.QFrame(Dialog)
        self.AddPeformanceFrame.setGeometry(QtCore.QRect(70, 120, 381, 271))
        self.AddPeformanceFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.AddPeformanceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AddPeformanceFrame.setLineWidth(3)
        self.AddPeformanceFrame.setObjectName("AddPeformanceFrame")
        self.AddPeformanceIDLabel = QtWidgets.QLabel(self.AddPeformanceFrame)
        self.AddPeformanceIDLabel.setGeometry(QtCore.QRect(30, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPeformanceIDLabel.setFont(font)
        self.AddPeformanceIDLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.AddPeformanceIDLabel.setObjectName("AddPeformanceIDLabel")
        self.AddPeformanceDateLabel = QtWidgets.QLabel(self.AddPeformanceFrame)
        self.AddPeformanceDateLabel.setGeometry(QtCore.QRect(30, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPeformanceDateLabel.setFont(font)
        self.AddPeformanceDateLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.AddPeformanceDateLabel.setObjectName("AddPeformanceDateLabel")
        self.AddPeformanceDateEdit = QtWidgets.QDateEdit(self.AddPeformanceFrame)
        self.AddPeformanceDateEdit.setGeometry(QtCore.QRect(210, 100, 161, 31))
        self.AddPeformanceDateEdit.setCalendarPopup(True)
        self.AddPeformanceDateEdit.setObjectName("AddPeformanceDateEdit")
        self.AddPeformanceTitleLabel = QtWidgets.QLabel(self.AddPeformanceFrame)
        self.AddPeformanceTitleLabel.setGeometry(QtCore.QRect(30, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPeformanceTitleLabel.setFont(font)
        self.AddPeformanceTitleLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.AddPeformanceTitleLabel.setObjectName("AddPeformanceTitleLabel")
        self.AddPeformanceTitleInput = QtWidgets.QLineEdit(self.AddPeformanceFrame)
        self.AddPeformanceTitleInput.setGeometry(QtCore.QRect(190, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPeformanceTitleInput.setFont(font)
        self.AddPeformanceTitleInput.setObjectName("AddPeformanceTitleInput")
        self.AddPeformanceButton = QtWidgets.QPushButton(self.AddPeformanceFrame)
        self.AddPeformanceButton.setGeometry(QtCore.QRect(80, 220, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.AddPeformanceButton.setFont(font)
        self.AddPeformanceButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.AddPeformanceButton.setObjectName("AddPeformanceButton")
        self.AddPeformanceIDDisplay = QtWidgets.QLabel(self.AddPeformanceFrame)
        self.AddPeformanceIDDisplay.setGeometry(QtCore.QRect(170, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddPeformanceIDDisplay.setFont(font)
        self.AddPeformanceIDDisplay.setStyleSheet("color: rgb(238, 238, 238);")
        self.AddPeformanceIDDisplay.setFrameShape(QtWidgets.QFrame.Box)
        self.AddPeformanceIDDisplay.setLineWidth(2)
        self.AddPeformanceIDDisplay.setText("")
        self.AddPeformanceIDDisplay.setObjectName("AddPeformanceIDDisplay")
        self.BackToMenuButton = QtWidgets.QPushButton(Dialog)
        self.BackToMenuButton.setGeometry(QtCore.QRect(340, 490, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(18)
        self.BackToMenuButton.setFont(font)
        self.BackToMenuButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.BackToMenuButton.setObjectName("BackToMenuButton")
        self.EditPeformanceFrame = QtWidgets.QFrame(Dialog)
        self.EditPeformanceFrame.setGeometry(QtCore.QRect(520, 100, 431, 351))
        self.EditPeformanceFrame.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditPeformanceFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.EditPeformanceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditPeformanceFrame.setLineWidth(3)
        self.EditPeformanceFrame.setObjectName("EditPeformanceFrame")
        self.EditPeformanceIDLabel = QtWidgets.QLabel(self.EditPeformanceFrame)
        self.EditPeformanceIDLabel.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EditPeformanceIDLabel.setFont(font)
        self.EditPeformanceIDLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditPeformanceIDLabel.setObjectName("EditPeformanceIDLabel")
        self.EditPeformanceIDInput = QtWidgets.QLineEdit(self.EditPeformanceFrame)
        self.EditPeformanceIDInput.setEnabled(False)
        self.EditPeformanceIDInput.setGeometry(QtCore.QRect(170, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EditPeformanceIDInput.setFont(font)
        self.EditPeformanceIDInput.setObjectName("EditPeformanceIDInput")
        self.EditPeformanceDateLabe = QtWidgets.QLabel(self.EditPeformanceFrame)
        self.EditPeformanceDateLabe.setGeometry(QtCore.QRect(30, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EditPeformanceDateLabe.setFont(font)
        self.EditPeformanceDateLabe.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditPeformanceDateLabe.setObjectName("EditPeformanceDateLabe")
        self.EditPerformanceDateEdit = QtWidgets.QDateEdit(self.EditPeformanceFrame)
        self.EditPerformanceDateEdit.setGeometry(QtCore.QRect(210, 170, 161, 31))
        self.EditPerformanceDateEdit.setCalendarPopup(True)
        self.EditPerformanceDateEdit.setObjectName("EditPerformanceDateEdit")
        self.EditPeformanceTitleLabel = QtWidgets.QLabel(self.EditPeformanceFrame)
        self.EditPeformanceTitleLabel.setGeometry(QtCore.QRect(30, 230, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EditPeformanceTitleLabel.setFont(font)
        self.EditPeformanceTitleLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditPeformanceTitleLabel.setObjectName("EditPeformanceTitleLabel")
        self.EditPeformanceTitleInput = QtWidgets.QLineEdit(self.EditPeformanceFrame)
        self.EditPeformanceTitleInput.setGeometry(QtCore.QRect(190, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EditPeformanceTitleInput.setFont(font)
        self.EditPeformanceTitleInput.setObjectName("EditPeformanceTitleInput")
        self.DeletePeformanceButton = QtWidgets.QPushButton(self.EditPeformanceFrame)
        self.DeletePeformanceButton.setGeometry(QtCore.QRect(220, 300, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.DeletePeformanceButton.setFont(font)
        self.DeletePeformanceButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.DeletePeformanceButton.setObjectName("DeletePeformanceButton")
        self.EditPeformanceButton = QtWidgets.QPushButton(self.EditPeformanceFrame)
        self.EditPeformanceButton.setGeometry(QtCore.QRect(10, 300, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Extrabold")
        font.setPointSize(14)
        self.EditPeformanceButton.setFont(font)
        self.EditPeformanceButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.EditPeformanceButton.setObjectName("EditPeformanceButton")
        self.comboBox = QtWidgets.QComboBox(self.EditPeformanceFrame)
        self.comboBox.setGeometry(QtCore.QRect(40, 40, 331, 31))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Title.setText(_translate("Dialog", "Create/Edit Peformances"))
        self.loggedindisplay.setText(_translate("Dialog", "logged in as:"))
        self.AddPeformanceIDLabel.setText(_translate("Dialog", "PeformanceID:"))
        self.AddPeformanceDateLabel.setText(_translate("Dialog", "Peformance Date:"))
        self.AddPeformanceDateEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd"))
        self.AddPeformanceTitleLabel.setText(_translate("Dialog", "Peformance Title:"))
        self.AddPeformanceButton.setText(_translate("Dialog", "Add Peformance"))
        self.BackToMenuButton.setText(_translate("Dialog", "Return To Menu"))
        self.EditPeformanceIDLabel.setText(_translate("Dialog", "PeformanceID:"))
        self.EditPeformanceDateLabe.setText(_translate("Dialog", "Peformance Date:"))
        self.EditPerformanceDateEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd"))
        self.EditPeformanceTitleLabel.setText(_translate("Dialog", "Peformance Title:"))
        self.DeletePeformanceButton.setText(_translate("Dialog", "Delete Peformance"))
        self.EditPeformanceButton.setText(_translate("Dialog", "Edit Peformance"))
