import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap

from Seatselection import *

class SeatSelectionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Seat Selector")
        self.seats = []
        self.rows = []
        self.populate_lists()
        
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
            seatlabel.setPixmap(QPixmap(".\\seatselector\\../images/highlighted.png"))
            seatdata["status"] = "highlighted"
        elif seatdata["status"] == "highlighted":
            seatlabel.setPixmap(QPixmap(".\\seatselector\\../images/empty.png"))
            seatdata["status"] = "empty"
        
        
    def populate_lists(self):
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":i+str(j+1),"status":"empty"})
        for i in(["A","B","C","D"]):
            for j in ("A","B"):
                self.rows.append(self.ui.__getattribute__("Row"+i+"_"+j))

def main():
    app = QApplication(sys.argv)
    window = SeatSelectionForm()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__": 
    main()
#move images into their own folder and use filepaths cause image management innit