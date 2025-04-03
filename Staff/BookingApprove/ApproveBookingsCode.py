import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem

if __name__ == "__main__":
    from ApproveBookings import Ui_Dialog
else:
    from .ApproveBookings import Ui_Dialog
    

class ApproveBookingsForm(QDialog):
    def __init__(self):
        super(ApproveBookingsForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_Staff_console)
        self.ui.FirstRecordButton.clicked.connect(self.firstrecord)
        
        self.setuptable("SELECT * FROM Bookings",["BookingID", "PerformanceID", "UserID", "Booking Date", "Booking Price"])
        
        
    def setuptable(self,sqlquery,headers):
        #use tablewidget ig
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute(sqlquery)
        data = cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        for header in headers:
            self.ui.tableWidget.setHorizontalHeaderItem(headers.index(header), QTableWidgetItem(header))
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                self.ui.tableWidget.setItem(i, j, item)
                
    def firstrecord(self):
        data = []
        for column in range(self.ui.tableWidget.columnCount()):
            data.append(self.ui.tableWidget.item(0, column).text())
            
        bookingID = data[0]
        bookingprice = data[4]
        userID = data[2]
        performanceID = data[1]
        
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("select count(*) from BookingSeats where Booking_ID = ?", (bookingID,))
        data = cursor.fetchone()
        
        numseats = data[0]
        
        cursor.execute("select first_name, last_name from Users where userID = ?", (userID,))
        data = cursor.fetchone()
        username = data[0] + " " + data[1]
        
        cursor.execute("select Performance_title from Performances where Performance_ID = ?", (performanceID,))
        data = cursor.fetchone()
        performance = data[0]
        
        cursor.close()
        cnxn.close()
        
        self.ui.BookingIDDisplay.setText(str(bookingID))
        self.ui.BookingPriceDisplay.setText(str(bookingprice))
        self.ui.BookedSeatsDisplay.setText(str(numseats))
        self.ui.FullNameDisplay.setText(str(username))
        self.ui.PerformanceDisplay.setText(str(performance))
        

    def connect(self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
        
    def switch_to_Staff_console(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
        
def main():
    app = QApplication(sys.argv)
    window = ApproveBookingsForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()