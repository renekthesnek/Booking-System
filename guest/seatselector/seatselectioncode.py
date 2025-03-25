import sys
import os

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
        self.populate_lists()
        self.emptyabspath = os.path.join(os.path.dirname(__file__), "..", "images", "empty.png")
        self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "images", "highlighted.png")
        self.booked_seats = []
        self.username = username
    
    def confirm_booking(self):
        if self.ui.listWidget.count() > 0:
            self.switch_to_confirm_booking()
        else:
            QMessageBox.warning(self, "Warning", "No Seats Selected!")
        
    def mousePressEvent(self, event):
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatlabel.underMouse():
                self.toggle_seat_status(seatdata)
        else:
            super().mousePressEvent(event)
            
    def toggle_seat_status(self, seatdata):
        seatlabel = seatdata["label_object"]
        if seatdata["status"] == "empty":
            seatlabel.setPixmap(QPixmap(self.highlightedabspath))
            seatdata["status"] = "highlighted"
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
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":i+str(j+1),"status":"empty"})
        for i in(["A","B","C","D","E","F","G","H","I","J"]):
            for j in ("A","B"):
                self.rows.append(self.ui.__getattribute__("Row"+i+"_"+j))

    def switch_to_confirm_booking(self):
        self.close()
        from bookingConformation import ConfirmBookingForm
        newwindow = ConfirmBookingForm(self.booked_seats,self.username)
        newwindow.show()
        newwindow.exec_()

def main():
    app = QApplication(sys.argv)
    window = SeatSelectionForm()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__": 
    main()
