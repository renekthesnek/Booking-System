import sys
import os
import pyodbc
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QLabel,QComboBox
from PyQt5.QtGui import QFont, QPixmap


if __name__ == "__main__":
    from SeatEditor import Ui_Dialog
else:
    from .SeatEditor import Ui_Dialog
    
#fix widget cascading after delete
#add confirmation functionality to update seatstates in database
    
class SeatEditorForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(SeatEditorForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.Backtostaffconsolebutton.clicked.connect(self.switch_to_Staff_console)
        self.seats = []
        self.labels = {}
        self.comboboxes = {}
        self.populate_lists()
        self.offset = 10
        self.widgets = 0
        self.ui.scrollAreaWidgetContents.adjustSize()
        self.ui.scrollArea.setWidgetResizable(True)
        
        if UserName == "No Parsed Username":
            self.ui.loggedindisplay.setText("Not Logged In")
        else:
            self.ui.loggedindisplay.setText("logged in as " + UserName)
        
        self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "highlighted.png")
        self.emptyabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "empty.png")
        self.getpeformancedata()
        self.getseatstates()

        
    
    def mousePressEvent(self, event):
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatlabel.underMouse():
                #add highlighting of seats and bind to comboboxes to make seats red when blocked
                if seatdata["status"] == "empty":
                    self.addnewclone(seatdata)
                    self.widgets += 1
                    self.ui.scrollAreaWidgetContents.update()
                    seatdata["status"] = 'highlighted'
                    seatlabel.setPixmap(QPixmap(self.highlightedabspath))
                elif seatdata["status"] == "highlighted":
                    self.removeclone(seatdata)
                    self.widgets -= 1
                    self.ui.scrollAreaWidgetContents.update()
                    seatdata["status"] = 'empty'
                    seatlabel.setPixmap(QPixmap(self.emptyabspath))
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
        
        newcombobox = clonedcombo(newticketlabel,self.ui)
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
    
    def removeclone(self,seatdata):
        seatname = seatdata["seat_id"]
        self.labels[f"Seat{seatname}Label"].parent().setVisible(False)
        self.labels[f"Seat{seatname}Label"].setVisible(False)
        self.labels[f"Seat{seatname}Label"].deleteLater()
        del self.labels[f"Seat{seatname}Label"]
        self.comboboxes[f"Seat{seatname}ComboBox"].parent().setVisible(False)
        self.comboboxes[f"Seat{seatname}ComboBox"].setVisible(False)
        self.comboboxes[f"Seat{seatname}ComboBox"].deleteLater()
        del self.comboboxes[f"Seat{seatname}ComboBox"]
        self.offset -= 75
        

    def populate_lists(self):
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":i+str(j+1),"status":"empty"})
    
    def switch_to_Staff_console(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
    
    def connect(self):
        fileabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn
    
    def getpeformancedata(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT Performance_title FROM Performances")
        data = cursor.fetchall()
        self.ui.comboBox.addItems([i[0] for i in data])
    
    def getseatstates(self):
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM SeatStatus WHERE performance_id = (select performance_id from Performances where Performance_title = ?)", (self.ui.comboBox.currentText(),))
        data = cursor.fetchall()
        for seatstate in data:
            for seat in self.seats:
                if seat["seat_id"] == seatstate[2]:
                    seat["status"] = seatstate[3]
                    break
            
            
        
class clonedlabel(QLabel):
    def __init__(self):
        super().__init__()
        
class clonedcombo(QComboBox):
    def __init__(self,myticketlabel,ui):
        super().__init__()
        self.addItems(["Available","Unavailable"])
        self.currentTextChanged.connect(self.on_change)
        self.myticketlabel = myticketlabel
        self.ui = ui
    
    def on_change(self):
        seat = self.myticketlabel.text()
        seat = seat[0]+"_"+seat[1]+seat[2]
        if self.currentText() == "Available":
            self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "highlighted.png")
            self.ui.__getattribute__("seat"+seat).setPixmap(QPixmap(self.highlightedabspath))
        else:
            self.blockedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "blocked.png")
            self.ui.__getattribute__("seat"+seat).setPixmap(QPixmap(self.blockedabspath))
def main():
    app = QApplication(sys.argv)
    window = SeatEditorForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()