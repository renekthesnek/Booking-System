import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog

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
        
        self.setuptable("SELECT * FROM Bookings")
        
        
    def setuptable(self,sqlquery):
        #use tablewidget ig
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute(sqlquery)
        data = cursor.fetchall()
        self.ui.tableView.rows(len(data))
        self.ui.tableView.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                item = QTableWidgetItem(str(data[i][j]))
                self.ui.tableView.setItem(i, j, item)

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