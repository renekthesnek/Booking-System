import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QComboBox

if __name__ == "__main__":
    from ConfirmBooking import Ui_Dialog
else:
    from .ConfirmBooking import Ui_Dialog
    

class ConfirmBookingForm(QDialog):
    def __init__(self, booked_seats):
        super(ConfirmBookingForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.ConfirmBookingButton.clicked.connect(self.confirm_booking)
        self.booked_seats = booked_seats
        if len (self.booked_seats) == 1:
            self.ui.SeatBookedLabelTemplate.setText(self.booked_seats[0])
            self.calculate_seat_price()
            self.ui.PriceLabelTemplate.setText("£" + str(self.calculate_seat_price()))
            self.ui.DropDownTemplate.currentTextChanged.connect(lambda: self.ui.PriceLabelTemplate.setText("£" + str(self.calculate_seat_price())))
        elif len (self.booked_seats) > 1:
            self.ui.SeatBookedLabelTemplate.setText(self.booked_seats[0])
            self.CloneTemplate()
        
        #Add updating of price label on new selection from dropdown box
    
    def confirm_booking(self):
        self.switch_to_Booking_Confirmed()
        
    def switch_to_Booking_Confirmed(self):
        self.close()
        from ConfirmedBooking import BookingConfirmedForm
        newwindow = BookingConfirmedForm()
        newwindow.show()
        newwindow.exec_()
    
    def CloneTemplate(self):
        return

    def calculate_seat_price(self):
        tickettype = self.ui.DropDownTemplate.currentText()
        if tickettype == "Normal Ticket":
            ticketprice = 10
        elif tickettype == "Reduced Price Ticket":
            ticketprice = 5
        elif tickettype == "Special Ticket":
            ticketprice = 0
        return ticketprice

class clonedcombo(QComboBox):
    def __init__(self, mypricewidget,parent = ...):
        super().__init__(parent)
        self.currentTextChanged.connect(self.on_change)
        self.mypricewidget = mypricewidget
        
    def on_change(self):
        self.mypricewidget.setText("£" + str(self.calculate_seat_price()))

    def calculate_seat_price(self):
        tickettype = self.ui.DropDownTemplate.currentText()
        if tickettype == "Normal Ticket":
            ticketprice = 10
        elif tickettype == "Reduced Price Ticket":
            ticketprice = 5
        elif tickettype == "Special Ticket":
            ticketprice = 0
        return ticketprice
def main():
    app = QApplication(sys.argv)
    window = ConfirmBookingForm(["A1"])
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()