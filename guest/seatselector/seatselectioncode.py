import sys
import os
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    from Seatselection import Ui_Dialog
else:
    from .Seatselection import Ui_Dialog

#add combobox functionality to allow for the preloading of performance data like booked seats

class SeatSelectionForm(QDialog):
    def __init__(self,username="No Parsed Username"):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Seat Selector")
        self.ui.pushButton.clicked.connect(self.confirm_booking)
        self.seats = []
        self.rows = []
        self.emptyabspath = os.path.join(os.path.dirname(__file__), "..", "images", "empty.png")
        self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "images", "highlighted.png")
        self.blockedabspath = os.path.join(os.path.dirname(__file__), "..", "images", "blocked.png")
        self.booked_seats = []
        self.username = username

        self.setupcombobox()
        self.performance = self.ui.comboBox.currentText()
        self.populate_lists()
        
        self.ui.comboBox.currentIndexChanged.connect(self.updatedisplays)
        
    def updatedisplays(self):
        self.seats = []
        self.rows = []
        self.performance = self.ui.comboBox.currentText()
        while self.ui.listWidget.count() > 0:
            self.ui.listWidget.takeItem(0)
        self.booked_seats = []
        self.populate_lists()
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatdata["status"] == "booked":
                seatlabel.setPixmap(QPixmap(self.blockedabspath))
            elif seatdata["status"] == "empty":
                seatlabel.setPixmap(QPixmap(self.emptyabspath))
    
    def setupcombobox(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("Select Performance_title from Performances")
        data = cursor.fetchall()
        self.ui.comboBox.addItems([i[0] for i in data])
    
    def confirm_booking(self):
        if self.ui.listWidget.count() > 0:
            self.switch_to_confirm_booking()
        else:
            QMessageBox.warning(self, "Warning", "No Seats Selected!")
        
    def mousePressEvent(self, event):
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatlabel.underMouse():
                if seatdata["status"] == "booked":
                    return
                self.toggle_seat_status(seatdata)
        else:
            super().mousePressEvent(event)
            
    def toggle_seat_status(self, seatdata):
        seatlabel = seatdata["label_object"]
        if seatdata["status"] == "empty":
            seatlabel.setPixmap(QPixmap(self.highlightedabspath))
            seatdata["status"] = "highlighted"
            if self.ui.listWidget.findItems(seatdata["seat_id"], Qt.MatchExactly):
                pass
            else:
                self.ui.listWidget.addItem(seatdata["seat_id"])
                self.booked_seats.append(seatdata["seat_id"])
        elif seatdata["status"] == "highlighted":
            seatlabel.setPixmap(QPixmap(self.emptyabspath))
            seatdata["status"] = "empty"
            for index in range(self.ui.listWidget.count()):
                item = self.ui.listWidget.item(index)
                if item.text() == seatdata["seat_id"]:
                    self.ui.listWidget.takeItem(index)
                    break
            self.booked_seats.remove(seatdata["seat_id"])
        
        
    def populate_lists(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT performance_id FROM Performances WHERE Performance_title = ?", (self.performance))
        performanceid = cursor.fetchone()[0]
        cursor.execute("SELECT seat_state FROM seatstatus WHERE performance_id = ?", (performanceid))
        data = cursor.fetchall()
        index = 0
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                status = data[index][0]
                index += 1
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":i+str(j+1),"status":status})
                if self.seats[-1]["status"] == "booked":
                    self.seats[-1]["label_object"].setPixmap(QPixmap(self.blockedabspath))
        for i in(["A","B","C","D","E","F","G","H","I","J"]):
            for j in ("A","B"):
                self.rows.append(self.ui.__getattribute__("Row"+i+"_"+j))

    def switch_to_confirm_booking(self):
        performance = self.ui.comboBox.currentText()
        self.close()
        from bookingConformation import ConfirmBookingForm
        newwindow = ConfirmBookingForm(self.booked_seats,performance,self.username)
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
    window = SeatSelectionForm()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__": 
    main()
