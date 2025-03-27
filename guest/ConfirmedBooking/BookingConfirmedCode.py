import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from BookingConfirmed import Ui_Dialog
else:
    from .BookingConfirmed import Ui_Dialog
    

#add functionality to show sidepanel images 
class BookingConfirmedForm(QDialog):
    def __init__(self,bookingid):
        super(BookingConfirmedForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("Select userID, performance_id from Bookings where Booking_id = ?", (bookingid,))
        data = cursor.fetchone()
        cursor.close()
        cnxn.close()
        self.userid = data[0]
        self.performance = data[1]
        self.ui.LabelBookingID.setText("booking reference number: " + str(bookingid))
        self.ui.LabelPeformanceID.setText("performance id: " + str(self.performance))
        self.ui.LabelUserID.setText(str("user id: " + str(self.userid)))
    
    def switch_to_main_menu(self):
        self.close()
        from mainmenu import MainMenuForm
        newwindow = MainMenuForm()
        newwindow.show()
        newwindow.exec_()
    
    def connect (self):
        fileabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn

def main():
    app = QApplication(sys.argv)
    window = BookingConfirmedForm(2)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()