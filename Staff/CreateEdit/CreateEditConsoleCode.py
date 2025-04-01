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


#add edit and delete functionality

class CreateEditConsoleForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(CreateEditConsoleForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Performance")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_Staff_console)
        self.ui.AddPeformanceButton.clicked.connect(self.addPerformance)
        self.ui.EditPeformanceButton.clicked.connect(self.editPerformance)
        self.ui.DeletePeformanceButton.clicked.connect(self.deletePerformance)
        if UserName == "No Parsed Username":
            self.ui.loggedindisplay.setText("Not Logged In")
        else:
            self.ui.loggedindisplay.setText("logged in as " + UserName)
        self.ui.AddPeformanceDateEdit.setDate(date.today())
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.updatedisplays(self.ui.comboBox.currentText()))
        try:
            self.updatedisplays()
        except:
            print("Performance Data Not Found")
            self.ui.AddPeformanceIDDisplay.setText("1")

    def switch_to_Staff_console(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
    
    def addPerformance(self):
        PerformanceID = self.ui.AddPeformanceIDDisplay.text()
        PerformanceDate = self.ui.AddPeformanceDateEdit.text()
        PerformanceTitle = self.ui.AddPeformanceTitleInput.text()
        PerformanceDate = PerformanceDate.replace("/","-")
        
        if PerformanceID != "" and PerformanceDate != "" and PerformanceTitle != "":
            if PerformanceID.isnumeric():
                cnxn = self.connect()
                cursor = cnxn.cursor()
                cursor.execute("INSERT INTO Performances VALUES (?, ?, ?)", (PerformanceID, PerformanceDate, PerformanceTitle))
                rows_affected = cursor.rowcount
                if rows_affected > 0:
                    for Row in ["A","B","C","D","E","F","G","H","I","J"]:
                        for number in range(1,21):
                            seatid = Row + str(number)
                            StatusID = PerformanceID + seatid        
                            cursor.execute("INSERT INTO SeatStatus VALUES (?,?,?,?)", (StatusID,PerformanceID,seatid,"empty"))   
                    rows_affected = cursor.rowcount
                    if rows_affected > 0:
                        cnxn.commit()
                        QMessageBox.information(self, "Success", "Performance has been added")
                        self.ui.AddPeformanceTitleInput.clear()
                        self.updatedisplays()
                    else:
                        QMessageBox.critical(self, "Error", "An error has occured while trying to add the peformance\nError Creating Seats")
                
                else:
                    QMessageBox.critical(self, "Error", "An error has occured while trying to add the peformance\nPerformance ID and Performance Date must be unique")
            else:
                QMessageBox.critical(self, "Error", "Performance ID must be a number")
        else:
            QMessageBox.critical(self, "Error", "Please fill in all fields")
    
    def editPerformance(self):
        PerformanceID = self.ui.EditPeformanceIDInput.text()
        PerformanceDate = self.ui.EditPerformanceDateEdit.text()
        PerformanceTitle = self.ui.EditPeformanceTitleInput.text()
        PerformanceDate = PerformanceDate.replace("/","-")
        
        if PerformanceID != "" and PerformanceDate != "" and PerformanceTitle != "":
            if PerformanceID.isnumeric():
                cnxn = self.connect()
                cursor = cnxn.cursor()
                cursor.execute("UPDATE Performances SET Performance_Date = ?, Performance_Title = ? WHERE Performance_ID = ?", (PerformanceDate, PerformanceTitle, PerformanceID))
                rows_affected = cursor.rowcount
                if rows_affected > 0:
                    cnxn.commit()
                    QMessageBox.information(self, "Success", "Performance has been updated")
                    self.ui.EditPeformanceTitleInput.clear()
                    self.updatedisplays()
                else:
                    QMessageBox.critical(self, "Error", "An error has occured while trying to edit the peformance")
            else:
                QMessageBox.critical(self, "Error", "Performance ID must be a number")
        else:
            QMessageBox.critical(self, "Error", "Please fill in all fields")
    
    def deletePerformance(self):
        PerformanceID = self.ui.EditPeformanceIDInput.text()
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("DELETE FROM Performances WHERE Performance_ID = ?", (PerformanceID,))
        rows_affected = cursor.rowcount
        if rows_affected > 0:
            cnxn.commit()
            QMessageBox.information(self, "Success", "Performance has been deleted")
            self.ui.EditPeformanceTitleInput.clear()
            self.updatedisplays()
        else:
            QMessageBox.critical(self, "Error", "An error has occured while trying to delete the peformance")
        
    def connect(self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
    
    def updatedisplays(self,title="ALL"):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT Max(performance_id) FROM Performances")
        MaxID = cursor.fetchone()
        if MaxID[0] == None:
            MaxID = 1
            self.ui.AddPeformanceIDDisplay.setText(str(MaxID))
        else:
            self.ui.AddPeformanceIDDisplay.setText(str(MaxID[0]+1))
        
        self.ui.comboBox.blockSignals(True)
        if title != "ALL":
            pass
        else:
            self.ui.comboBox.clear()
            cursor.execute("Select Performance_title from Performances")
            data = cursor.fetchall()
            self.ui.comboBox.addItems([i[0] for i in data])
        self.ui.comboBox.blockSignals(False)

        if title != "ALL":
            cursor.execute("select * from Performances where Performance_title = ?", (title,))
        else:
            cursor.execute("select * from Performances where Performance_title = ?", (self.ui.comboBox.currentText(),))
        data = cursor.fetchone()
        if data != None:
            self.ui.EditPeformanceIDInput.setText(str(data[0]))
            self.ui.EditPerformanceDateEdit.setDate(date.fromisoformat(data[1]))
            self.ui.EditPeformanceTitleInput.setText(str(data[2]))
def main():
    app = QApplication(sys.argv)
    window = CreateEditConsoleForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()