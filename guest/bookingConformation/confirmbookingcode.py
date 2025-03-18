import sys
import os
import pyodbc
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QComboBox,QLabel,QMessageBox
from PyQt5.QtGui import QFont

if __name__ == "__main__":
    from ConfirmBooking import Ui_Dialog
else:
    from .ConfirmBooking import Ui_Dialog
    
comboboxes = {}

class ConfirmBookingForm(QDialog):
    def __init__(self, booked_seats,username="No Parsed Username"):
        super(ConfirmBookingForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.ConfirmBookingButton.clicked.connect(self.confirm_booking)
        if username == "No Parsed Username":
            self.ui.LoginDisplay.setText("Not Logged In")
        else:
            self.ui.LoginDisplay.setText("logged in as " + username)
        self.booked_seats = booked_seats
        self.offset = 10
        self.labels = {}
        
        if len (self.booked_seats) == 1:
            self.CloneTemplate(0)
            labelname = f"Seat{self.booked_seats[0]}PriceLabel"
            comboname = f"Seat{self.booked_seats[0]}ComboBox"
            labelobject = self.labels[labelname]
            comboboxobject = comboboxes[comboname]
            labelobject.setText("£" + str(self.calculate_seat_price(comboboxobject)))
            
        elif len (self.booked_seats) > 1:
            for row in range(len(self.booked_seats)):
                self.CloneTemplate(row)
                labelname = f"Seat{self.booked_seats[row]}PriceLabel"
                comboname = f"Seat{self.booked_seats[row]}ComboBox"
                labelobject = self.labels[labelname]
                comboboxobject = comboboxes[comboname]
                labelobject.setText("£" + str(self.calculate_seat_price(comboboxobject)))
                if row > 5:
                    self.ui.scrollAreaWidgetContents.resize(self.ui.scrollAreaWidgetContents.width(), self.ui.scrollAreaWidgetContents.height() + 75)
            self.ui.scrollAreaWidgetContents.setMinimumSize(self.ui.scrollAreaWidgetContents.width(), self.ui.scrollAreaWidgetContents.height())
            
        self.calculate_total_price()
    
    def confirm_booking(self):
        #make if for whether user logged in or not
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("Select Max(UserID) from Users")
        MaxID = cursor.fetchone()
        if self.ui.UsernameInput.text == "" or self.ui.FullNameInput.text == "":
            QMessageBox.critical(self, "Error", "Please enter a username and full name")
        elif self.ui.EmailInput.text() == "" and self.ui.PhoneNumberlInput.text == "":
            QMessageBox.critical(self, "Error", "Please enter Email or phone number")
        elif self.ui.PasswordInput.text() == "":
            QMessageBox.critical(self, "Error", "Please enter a password")
        elif self.ui.ConfirmPasswordInput.text() == "":
            QMessageBox.critical(self, "Error", "Please confirm your password")
        elif self.ui.PasswordInput.text() != self.ui.ConfirmPasswordInput.text():
            QMessageBox.critical(self, "Error", "Passwords do not match")
        else:
            currentID = MaxID[0] + 1
            firstname,lastname = self.ui.FullNameInput.text().split(" ")
            username = self.ui.UsernameInput.text()
            #add validation for phone number or email here
            if self.ui.PhoneNumberlInput.text != "":
                phonenumber = self.ui.PhoneNumberlInput.text()
                try:
                    phonenumber = int(phonenumber)
                except ValueError:
                    #flags anyway when empty, fix this
                    QMessageBox.critical(self, "Error", "Please enter a valid phone number")
            else:
                phonenumber = None
            if self.ui.EmailInput.text != "":
                email = self.ui.EmailInput.text()
                try:
                    email = str(email)
                except ValueError:
                    QMessageBox.critical(self, "Error", "Please enter a valid email")
            else:
                email = None
            passwordhash = hashlib.sha224(self.ui.PasswordInput.text().encode()).hexdigest()
            permission = "Guest"
            cursor.execute("INSERT INTO Users VALUES (?,?,?,?,?,?,?,?)", (currentID,username,passwordhash,email,phonenumber,firstname,lastname,permission))
            rows_affected = cursor.rowcount
            if rows_affected > 0:
                QMessageBox.information(self, "Success", "Booking Confirmed")
                cnxn.commit()
                cnxn.close()
            else:
                QMessageBox.critical(self, "Error", "An error has occured during insertion")
                cnxn.close
            self.switch_to_Booking_Confirmed()
            
    def switch_to_Booking_Confirmed(self):
        self.close()
        from ConfirmedBooking import BookingConfirmedForm
        newwindow = BookingConfirmedForm()
        newwindow.show()
        newwindow.exec_()
    
    def calculate_total_price(self):
        self.total_price = 0
        for combobox in comboboxes.values():
            self.total_price += self.calculate_seat_price(combobox)
        self.ui.TotalPriceDisplay.setText("£" + str(self.total_price))
    
    def CloneTemplate(self, currentindex):
        seatname = self.booked_seats[currentindex]

        newticketlabel = clonedlabel()
        newticketlabel.setParent(self.ui.scrollAreaWidgetContents)
        newticketlabel.setGeometry(10,self.offset,141,41)
        newticketlabel.setFont(QFont('Open Sans Extrabold',24))
        newticketlabel.setText(self.booked_seats[currentindex])
        newticketlabel.setObjectName(f"Seat{seatname}Label")
        self.labels[f"Seat{seatname}Label"] = newticketlabel

        newpricelabel = clonedlabel()
        newpricelabel.setParent(self.ui.scrollAreaWidgetContents)  # Fix: set parent to self.ui.scrollAreaWidgetContents
        newpricelabel.setGeometry(340,self.offset,121,41)
        newpricelabel.setFont(QFont('Open Sans Extrabold',24))
        newpricelabel.setObjectName(f"Seat{seatname}PriceLabel")
        self.labels[f"Seat{seatname}PriceLabel"] = newpricelabel

        newcombobox = clonedcombo(newpricelabel,self.ui)
        newcombobox.setParent(self.ui.scrollAreaWidgetContents)  # Fix: set parent to self.ui.scrollAreaWidgetContents
        newcombobox.setGeometry(160,self.offset,171,41)
        newcombobox.setFont(QFont('Open Sans Extrabold',10))
        newcombobox.setObjectName(f"Seat{seatname}ComboBox")
        comboboxes[f"Seat{seatname}ComboBox"] = newcombobox

        self.offset += 75
    def calculate_seat_price(self,comboboxobject):
        tickettype = comboboxobject.currentText()
        if tickettype == "Normal Ticket":
            ticketprice = 10
        elif tickettype == "Reduced Price Ticket":
            ticketprice = 5
        elif tickettype == "Special Ticket":
            ticketprice = 0
        return ticketprice#
    
    def connect (self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
    

class clonedcombo(QComboBox):
    def __init__(self, mypricewidget,ui):
        super().__init__()
        self.ui = ui
        self.currentTextChanged.connect(self.on_change)
        self.mypricewidget = mypricewidget
        self.addItems(["Normal Ticket","Reduced Price Ticket","Special Ticket"])
        
    def on_change(self):
        self.mypricewidget.setText("£" + str(self.calculate_seat_price()))
        self.calculate_total_price()

    def calculate_seat_price(self):
        tickettype = self.currentText()
        if tickettype == "Normal Ticket":
            ticketprice = 10
        elif tickettype == "Reduced Price Ticket":
            ticketprice = 5
        elif tickettype == "Special Ticket":
            ticketprice = 0
        return ticketprice
    
    def calculate_total_price(self):
        self.total_price = 0
        for combobox in comboboxes.values():
            tickettype = combobox.currentText()
            if tickettype == "Normal Ticket":
                ticketprice = 10
            elif tickettype == "Reduced Price Ticket":
                ticketprice = 5
            elif tickettype == "Special Ticket":
                ticketprice = 0
            self.total_price += ticketprice
        self.ui.TotalPriceDisplay.setText("£" + str(self.total_price))
    
class clonedlabel(QLabel):
    def __init__(self):
        super().__init__()
        
        
def main():
    app = QApplication(sys.argv)
    window = ConfirmBookingForm(["A1"])
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()