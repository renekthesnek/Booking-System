import sys
import os
import pyodbc
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QLabel,QComboBox
from PyQt5.QtGui import QFont


if __name__ == "__main__":
    from SeatEditor import Ui_Dialog
else:
    from .SeatEditor import Ui_Dialog
    
class SeatEditorForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(SeatEditorForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.seats = []
        self.labels = {}
        self.comboboxes = {}
        self.populate_lists()
        self.offset = 10
        self.widgets = 0
        self.ui.scrollAreaWidgetContents.adjustSize()
        self.ui.scrollArea.setWidgetResizable(True)
        
    
    def mousePressEvent(self, event):
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatlabel.underMouse():
                if seatdata["status"] == "empty":
                    self.addnewclone(seatdata)
                    self.widgets += 1
                    self.ui.scrollAreaWidgetContents.update()
                    seatdata["status"] == 'highlighted'
                elif seatdata["status"] == "highlighted":
                    #self.removeclone(seatdata)
                    self.widgets -= 1
                    self.ui.scrollAreaWidgetContents.update()
                    seatdata["status"] == 'empty'
        else:
            super().mousePressEvent(event)
            
    def addnewclone(self,seatdata):
        seatname = seatdata["seat_id"]
        
        newticketlabel = clonedlabel()
        newticketlabel.setParent(self.ui.scrollAreaWidgetContents)
        newticketlabel.setGeometry(10,self.offset,91,41)
        newticketlabel.setFont(QFont('Open Sans Extrabold',16))
        newticketlabel.setText(seatname)
        newticketlabel.setObjectName(f"Seat{seatname}Label")
        newticketlabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.labels[f"Seat{seatname}Label"] = newticketlabel
        
        newcombobox = clonedcombo()
        newcombobox.setParent(self.ui.scrollAreaWidgetContents)
        newcombobox.setGeometry(100,self.offset,121,41)
        newcombobox.setFont(QFont('Open Sans Extrabold',10))
        newcombobox.setObjectName(f"Seat{seatname}ComboBox")
        newcombobox.setStyleSheet("color: rgb(238, 238, 238);")
        self.comboboxes[f"Seat{seatname}ComboBox"] = newcombobox
        
        newticketlabel.parent().setVisible(True)
        newticketlabel.setVisible(True)
        newcombobox.parent().setVisible(True)
        newcombobox.setVisible(True)
        
        if self.widgets >= 4:
            self.ui.scrollAreaWidgetContents.setFixedSize(self.ui.scrollAreaWidgetContents.width(), self.ui.scrollAreaWidgetContents.height() + 75)
        
        self.offset += 75
        

    def populate_lists(self):
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":i+str(j+1),"status":"empty"})
                
class clonedlabel(QLabel):
    def __init__(self):
        super().__init__()
        
class clonedcombo(QComboBox):
    def __init__(self):
        super().__init__()
        
def main():
    app = QApplication(sys.argv)
    window = SeatEditorForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()