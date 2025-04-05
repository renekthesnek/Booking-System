import sys
import os
import pyodbc
import hashlib
import datetime
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QComboBox,QLabel,QMessageBox
from PyQt5.QtGui import QFont

if __name__ == "__main__":
    from ConfirmBooking import Ui_Dialog
else:
    from .ConfirmBooking import Ui_Dialog
    
comboboxes = {}



class ConfirmBookingForm(QDialog):
    def __init__(self, booked_seats,performance,username="No Parsed Username"):
        super(ConfirmBookingForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.ConfirmBookingButton.clicked.connect(self.confirm_booking)
        if username == "No Parsed Username":
            self.ui.LoginDisplay.setText("Not Logged In")
        else:
            self.ui.LoginDisplay.setText("logged in as " + username)
            self.username = username  
            cnxn = self.connect()
            cursor = cnxn.cursor()
            cursor.execute("select * from Users where Username = ?", (self.username))
            data = cursor.fetchone()
            
            self.ui.UsernameInput.setText(data[1])
            self.ui.UsernameInput.setEnabled(False)
            
            self.ui.FullNameInput.setText(data[5] + " " + data[6])
            self.ui.FullNameInput.setEnabled(False)
            
            try:
                self.ui.EmailInput.setText(data[3])
                self.ui.EmailInput.setEnabled(False)
            except:
                pass
            try:
                self.ui.PhoneNumberlInput.setText(str(data[4]))
                self.ui.PhoneNumberlInput.setEnabled(False)
            except:
                pass
            self.ui.PasswordInput.setEnabled(False)
            self.ui.ConfirmPasswordInput.setEnabled(False)
        self.booked_seats = booked_seats
        self.offset = 10
        self.labels = {}
        self.performance = performance
        self.username = username
        
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
        if self.username == "No Parsed Username":
            cnxn = self.connect()
            cursor = cnxn.cursor()
            cursor.execute("Select Max(UserID) from Users")
            MaxID = cursor.fetchone()
            if self.ui.UsernameInput.text() == "" or self.ui.FullNameInput.text() == "":
                QMessageBox.critical(self, "Error", "Please enter a username and full name")
            elif self.ui.EmailInput.text() == "" and self.ui.PhoneNumberlInput.text() == "":
                QMessageBox.critical(self, "Error", "Please enter Email or phone number")
            elif self.ui.PasswordInput.text() == "":
                QMessageBox.critical(self, "Error", "Please enter a password")
            elif self.ui.ConfirmPasswordInput.text() == "":
                QMessageBox.critical(self, "Error", "Please confirm your password")
            elif self.ui.PasswordInput.text() != self.ui.ConfirmPasswordInput.text():
                QMessageBox.critical(self, "Error", "Passwords do not match")
            elif len(self.ui.FullNameInput.text().strip().split(" ")) != 2:
                QMessageBox.critical(self, "Error", "Please enter a first and last name")
            else:
                userID = MaxID[0] + 1
                firstname,lastname = self.ui.FullNameInput.text().split(" ")
                username = self.ui.UsernameInput.text()
                if self.ui.PhoneNumberlInput.text != "":
                    phonenumber = self.ui.PhoneNumberlInput.text()
                    try:
                        phonenumber = int(phonenumber)
                    except ValueError:
                        phonenumber = None
                else:
                    phonenumber = None
                if self.ui.EmailInput.text != "":
                    email = self.ui.EmailInput.text()
                    validationpattern =  r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if re.match(validationpattern, email):
                        email = email
                    else:
                        QMessageBox.critical(self, "Error", "Please enter a valid email address")
                        return
                    try:
                        email = str(email)
                    except ValueError:
                        phonenumber = None
                else:
                    email = None
                
                if phonenumber == None and email == None or phonenumber == None and email == "" or phonenumber == "" and email == None:
                    QMessageBox.critical(self, "Error", "Please enter a phone number or email")
                    return
                passwordhash = hashlib.sha224(self.ui.PasswordInput.text().encode()).hexdigest()
                permission = "Guest"
                cursor.execute("INSERT INTO Users VALUES (?,?,?,?,?,?,?,?)", (userID,username,passwordhash,email,phonenumber,firstname,lastname,permission))
                rows_affected = cursor.rowcount
        else:
            cnxn = self.connect()
            cursor = cnxn.cursor()
            username = self.ui.UsernameInput.text()
            cursor.execute("select UserID from Users where Username = ?", (self.username,))
            userID = cursor.fetchone()[0]
            loggedin = True
            rows_affected = 0
        
        if rows_affected > 0 or loggedin:
            try:
                self.bookingid = cursor.execute("Select Max(booking_id) from Bookings").fetchone()[0] + 1
            except:
                self.bookingid = 1
            performanceid = cursor.execute("Select Performance_ID from Performances where Performance_title = ?", (self.performance,)).fetchone()[0]
            self.calculate_total_price()
            totalprice = str(self.total_price) + ".00"
            bookingdate = datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO Bookings VALUES (?,?,?,?,?)", (self.bookingid,userID,performanceid,bookingdate,totalprice))
            rows_affected = cursor.rowcount
            if rows_affected > 0:
                for seat in self.booked_seats:
                    seat = seat["seat_id"]
                    bookingseatsID = str(self.bookingid) + str(seat)
                    cursor.execute("INSERT INTO BookingSeats VALUES (?,?,?)", (bookingseatsID,self.bookingid,seat))
                    rows_affected = cursor.rowcount
                    if rows_affected > 0:
                        cursor.execute("UPDATE SeatStatus SET seat_state = ? WHERE Performance_ID = ? AND Seat_ID = ?", ("booked",performanceid,seat))
                        rows_affected = cursor.rowcount
                        if rows_affected > 0:
                            cnxn.commit()
                        else:
                            QMessageBox.critical(self, "Error", "An error has occured during insertion of seat status")
                            cnxn.close
                    else:
                        QMessageBox.critical(self, "Error", "An error has occured during insertion of booking seat")
                        cnxn.close
                self.switch_to_Booking_Confirmed()
            else:
                QMessageBox.critical(self, "Error", "An error has occured during insertion of booking")
                cnxn.close
        else:
            QMessageBox.critical(self, "Error", "An error has occured during insertion of user")
            cnxn.close
            
    def switch_to_Booking_Confirmed(self):
        self.close()
        from ConfirmedBooking import BookingConfirmedForm
        newwindow = BookingConfirmedForm(self.bookingid)
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
        newticketlabel.setText(self.booked_seats[currentindex]["seat_id"])
        newticketlabel.setObjectName(f"Seat{seatname}Label")
        newticketlabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.labels[f"Seat{seatname}Label"] = newticketlabel

        newpricelabel = clonedlabel()
        newpricelabel.setParent(self.ui.scrollAreaWidgetContents)  
        newpricelabel.setGeometry(340,self.offset,121,41)
        newpricelabel.setFont(QFont('Open Sans Extrabold',24))
        newpricelabel.setObjectName(f"Seat{seatname}PriceLabel")
        newpricelabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.labels[f"Seat{seatname}PriceLabel"] = newpricelabel

        newcombobox = clonedcombo(newpricelabel,self.ui)
        newcombobox.setParent(self.ui.scrollAreaWidgetContents) 
        newcombobox.setGeometry(160,self.offset,171,41)
        newcombobox.setFont(QFont('Open Sans Extrabold',10))
        newcombobox.setObjectName(f"Seat{seatname}ComboBox")
        newcombobox.setStyleSheet("color: rgb(238, 238, 238);")
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
        return ticketprice
    
    def connect (self):
        fileabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
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
    window = ConfirmBookingForm(["A1"],"macbeth")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()