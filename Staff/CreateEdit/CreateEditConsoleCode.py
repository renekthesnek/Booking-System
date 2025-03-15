import sys
import os
import pyodbc
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox

if __name__ == "__main__":
    from CreateEditConsole import Ui_Dialog
else:
    from .CreateEditConsole import Ui_Dialog



class CreateEditConsoleForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(CreateEditConsoleForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_Staff_console)
        self.ui.AddPeformanceButton.clicked.connect(self.addPeformance)
        self.ui.loggedindisplay.setText("Logged in as: " + UserName)
        self.ui.AddPeformanceDateEdit.setDate(date.today())

    def switch_to_Staff_console(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
    
    def addPeformance(self):
        PeformanceID = self.ui.AddPeformanceIDInput.text()
        PeformanceDate = self.ui.AddPeformanceDateEdit.text()
        PeformanceTitle = self.ui.AddPeformanceTitleInput.text()
        PeformanceDate = PeformanceDate.replace("/","-")
        
        if PeformanceID != "" and PeformanceDate != "" and PeformanceTitle != "":
            if PeformanceID.isnumeric():
                cnxn = self.connect()
                cursor = cnxn.cursor()
                cursor.execute("INSERT INTO Performances VALUES (?, ?, ?)", (PeformanceID, PeformanceDate, PeformanceTitle))
                rows_affected = cursor.rowcount
                if rows_affected > 0:
                    for Row in ["A","B","C","D","E","F","G","H","I","J"]:
                        for number in range(1,21):
                            seatid = Row + str(number)
                            StatusID = PeformanceID + seatid        
                            cursor.execute("INSERT INTO SeatStatus VALUES (?,?,?,?)", (StatusID,PeformanceID,seatid,"empty"))   
                    rows_affected = cursor.rowcount
                    if rows_affected > 0:
                        cnxn.commit()
                        QMessageBox.information(self, "Success", "Peformance has been added")
                        self.ui.AddPeformanceIDInput.clear()
                        self.ui.AddPeformanceTitleInput.clear()
                    else:
                        QMessageBox.critical(self, "Error", "An error has occured while trying to add the peformance\nError Creating Seats")
                
                else:
                    QMessageBox.critical(self, "Error", "An error has occured while trying to add the peformance\nPeformance ID and Peformance Date must be unique")
            else:
                QMessageBox.critical(self, "Error", "Peformance ID must be a number")
        else:
            QMessageBox.critical(self, "Error", "Please fill in all fields")
        
    def connect(self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
def main():
    app = QApplication(sys.argv)
    window = CreateEditConsoleForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()