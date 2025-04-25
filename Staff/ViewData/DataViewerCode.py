import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
if __name__ == "__main__":
    from DataViewer import Ui_Dialog
else:
    from .DataViewer import Ui_Dialog

#change from counting on button click to checking if the buttons text is in the label already, if it is then remove 
#simple right?

class DataViewerForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(DataViewerForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)
        
        self.ui.usersbutton.clicked.connect(lambda: self.updatelabel("Users"))
        self.ui.SeatsButton.clicked.connect(lambda: self.updatelabel("Seats"))
        self.ui.performancesbutton.clicked.connect(lambda: self.updatelabel("Performances"))
        self.ui.bookingsbutton.clicked.connect(lambda: self.updatelabel("Bookings"))
        self.ui.bookingseatsbutton.clicked.connect(lambda: self.updatelabel("Booking Seats"))
        self.ui.seatstatesbutton.clicked.connect(lambda: self.updatelabel("Seat States"))
        
        self.ui.NextRecordButton.clicked.connect(self.nextrecord)
        
        self.cursor = None
        self.currentrow = 0
        
        self.ui.SelectedMultiDisplay.setText("")

    
    def nextrecord(self):
        if self.cursor is None:
            table = self.ui.SelectedMultiDisplay.text().split("\n")
            if table != "":
                cnxn = self.connect()
                self.cursor = cnxn.cursor()
                table_names = ', '.join(['Bookings' if t == 'Booking' else 'BookingSeats' if t == 'Booking Seats' else 'SeatStatus' if t == 'Seat States' else t for t in table])
                self.cursor.execute(f"SELECT * FROM {table_names}")
        data = self.cursor.fetchone()
        if data is None:
            QMessageBox.critical(self, "Error", "No more data available in the table.")
            return
        else:
            self.currentrow += 1
            self.ui.tableWidget.setRowCount(1)
            for i, item in enumerate(data):
                self.ui.tableWidget.setItem(0, i, QTableWidgetItem(str(item)))
        

    def updatetable(self):
        self.cursor = None
        self.currentrow = 0
        cnxn = self.connect()
        cursor = cnxn.cursor()
        tables = self.ui.SelectedMultiDisplay.text().split("\n")
        
        updated_tables = []
        for table in tables:
            if table == "Users": updated_tables.append("Users")
            elif table == "Seats": updated_tables.append("Seats")
            elif table == "Performances": updated_tables.append("Performances")
            elif table == "Bookings": updated_tables.append("Bookings")
            elif table == "Booking Seats": updated_tables.append("BookingSeats")
            elif table == "Seat States": updated_tables.append("SeatStatus")
            else: continue

        sqlquery = "SELECT * FROM " + ", ".join(updated_tables)
        if updated_tables != []:
            cursor.execute(sqlquery)
        
        if cursor.description is not None:
            data = cursor.fetchall()
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(len(data))
            self.ui.tableWidget.setColumnCount(len(cursor.description))
            self.ui.tableWidget.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))#
        else:
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)
            
    def updatelabel(self, text):
        if text in self.ui.SelectedMultiDisplay.text():
            if len(self.ui.SelectedMultiDisplay.text().split("\n")) > 1:
                self.ui.SelectedMultiDisplay.setText(self.ui.SelectedMultiDisplay.text().replace("\n"+text, "")) 
            else:
                self.ui.SelectedMultiDisplay.setText(self.ui.SelectedMultiDisplay.text().replace(text, ""))
        else:
            if len(self.ui.SelectedMultiDisplay.text()) > 1:
                self.ui.SelectedMultiDisplay.setText(self.ui.SelectedMultiDisplay.text() + "\n" + text)
            else:
                self.ui.SelectedMultiDisplay.setText(self.ui.SelectedMultiDisplay.text() + text)
        
        self.updatetable()
        
    def connect (self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
    
    def switch_to_main_menu(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
def main():
    app = QApplication(sys.argv)
    window = DataViewerForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()