import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox

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
        self.ui.NextRecordButton.clicked.connect(self.nextrecord)
        self.ui.PreviousRecordButton.clicked.connect(self.previousrecord)
        self.ui.ApproveBookingButton.clicked.connect(self.approvebooking)
        self.ui.DenyBookingButton.clicked.connect(self.denybooking)
        self.ui.tableWidget.setStyleSheet("background-color: rgb(126, 126, 126);")
        self.setuptable("SELECT Booking_ID, userID, performance_id, booking_date, total_price FROM Bookings where booking_status = 'Pending'",["BookingID", "PerformanceID", "UserID", "Booking Date", "Booking Price"])
        
        self.firstrecord()
        
    
    def approvebooking(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("update Bookings set booking_status = 'Approved' where Booking_ID = ?", (self.ui.BookingIDDisplay.text(),))
        cnxn.commit()
        self.setuptable("SELECT Booking_ID, userID, performance_id, booking_date, total_price FROM Bookings where booking_status = 'Pending'",["BookingID", "PerformanceID", "UserID", "Booking Date", "Booking Price"])
        self.firstrecord()
    
    def denybooking(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("delete from Bookings where Booking_ID = ?", (self.ui.BookingIDDisplay.text(),))
        cnxn.commit()
        self.setuptable("SELECT Booking_ID, userID, performance_id, booking_date, total_price FROM Bookings where booking_status = 'Pending'",["BookingID", "PerformanceID", "UserID", "Booking Date", "Booking Price"])
        self.firstrecord()
        
    def setuptable(self,sqlquery,headers):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute(sqlquery)
        data = cursor.fetchall()
        try:
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(len(data[0]))
            for header in headers:
                self.ui.tableWidget.setHorizontalHeaderItem(headers.index(header), QTableWidgetItem(header))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    item = QTableWidgetItem(str(data[i][j]))
                    self.ui.tableWidget.setItem(i, j, item)
        except:
            QMessageBox.critical(self, "Error", "No Bookings found")
            self.switch_to_Staff_console()
            
    def updatewidgets(self,data):
        bookingID = data[0]
        bookingprice = data[4]
        userID = data[1]
        performanceID = data[2]
        
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
                
    def firstrecord(self):
        data = []
        for column in range(self.ui.tableWidget.columnCount()):
            data.append(self.ui.tableWidget.item(0, column).text())
        
        self.currentrow = 0
        self.updatewidgets(data)
        
    def nextrecord(self):
        if self.currentrow >= self.ui.tableWidget.rowCount()-1:
            return
        self.currentrow += 1
        data = []
        for column in range(self.ui.tableWidget.columnCount()):
            data.append(self.ui.tableWidget.item(self.currentrow, column).text())
        
        self.updatewidgets(data)
    
    def previousrecord(self):
        if self.currentrow <= 0:
            return
        self.currentrow -= 1
        data = []
        for column in range(self.ui.tableWidget.columnCount()):
            data.append(self.ui.tableWidget.item(self.currentrow, column).text())
        
        self.updatewidgets(data)

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