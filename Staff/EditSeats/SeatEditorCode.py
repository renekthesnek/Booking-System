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
    
Blocked_seats = []
    
class SeatEditorForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(SeatEditorForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.Backtostaffconsolebutton.clicked.connect(self.switch_to_Staff_console)
        self.ui.ConfirmButton.clicked.connect(self.updateseats)
        self.comboboxes = {}
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
        self.blockedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "blocked.png")
        self.getpeformancedata()
        self.populate_lists()
        self.getseatstates()
    
    def mousePressEvent(self, event):
        for seatdata in self.seats:
            seatlabel = seatdata["label_object"]
            if seatlabel.underMouse():
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
        
        if f"Seat{seatname}Label" in self.labels:
            self.labels[f"Seat{seatname}Label"].setVisible(True)
            self.comboboxes[f"Seat{seatname}ComboBox"].setVisible(True)
        else:
        
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
            
            newticketlabel.setVisible(True)
            newcombobox.setVisible(True)
        
            if self.widgets >= 4:
                self.ui.scrollAreaWidgetContents.setFixedSize(self.ui.scrollAreaWidgetContents.width(), self.ui.scrollAreaWidgetContents.height() + 75)
            
            self.offset += 75
    
    def removeclone(self,seatdata):
        global Blocked_seats
        seatname = seatdata["seat_id"]
        
        self.labels[f"Seat{seatname}Label"].setVisible(False)
        
        self.comboboxes[f"Seat{seatname}ComboBox"].setVisible(False)
        
        for widget in list(self.labels.values())[list(self.labels.values()).index(self.labels[f"Seat{seatname}Label"])+1:]:
            widget.move(widget.x(), widget.y()-75)
        for widget in list(self.comboboxes.values())[list(self.comboboxes.values()).index(self.comboboxes[f"Seat{seatname}ComboBox"])+1:]:
            widget.move(widget.x(), widget.y()-75)
            
        if self.widgets >= 4:
                self.ui.scrollAreaWidgetContents.setFixedSize(self.ui.scrollAreaWidgetContents.width(), self.ui.scrollAreaWidgetContents.height() - 75)
        
        
        dictseatname = seatname[0] + "_"+ seatname[1]  + seatname[2]
        Blocked_seats = [dict(t) for t in {tuple(d.items()) for d in Blocked_seats}]
        Blocked_seats = [item for item in Blocked_seats if item["seat_id"] != dictseatname]
            
        self.offset -= 75
        
        del self.labels[f"Seat{seatname}Label"]
        del self.comboboxes[f"Seat{seatname}ComboBox"]

    def populate_lists(self):
        self.seats = []
        self.labels = {}
        self.performance = self.ui.comboBox.currentText()
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT performance_id FROM Performances WHERE Performance_title = ?", (self.performance))
        performanceid = cursor.fetchone()
        if performanceid == None:
            QMessageBox.critical(self, "Error", "No Performances found")
            self.switch_to_Staff_console()
        else:
            performanceid = performanceid[0]
        index = 0
        for i in (["A","B","C","D","E","F","G","H","I","J"]):
            for j in range(20):
                if j <= 10:
                    seatRow = f"Row{i}_A"
                else:
                    seatRow = f"Row{i}_B"
                seatid = i+str(j+1)
                cursor.execute("SELECT seat_state FROM seatstatus WHERE seat_id = ? AND performance_id = ?", (seatid,performanceid))
                data = cursor.fetchone()
                status = data[0]
                index += 1
                self.seats.append({"label_object":self.ui.__getattribute__("seat"+i+"_"+str(j+1)),"seat_id":seatid,"status":status,"seat_row":seatRow})
                if self.seats[-1]["status"] == "booked":
                    self.seats[-1]["label_object"].setPixmap(QPixmap(self.blockedabspath))
        
    def updateseats(self):
        global Blocked_seats
        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT Performance_id FROM Performances WHERE performance_title = ?", (self.ui.comboBox.currentText(),))
        self.performanceid = cursor.fetchone()[0]
        for seat in Blocked_seats:
            seat["seat_id"] = seat["seat_id"][0]+seat["seat_id"][2]+seat["seat_id"][3]
            cursor.execute("UPDATE seatstatus SET seat_state = ? WHERE seat_id = ? AND performance_id = ?", (seat["status"],seat["seat_id"],self.performanceid))
        rows_affected = cursor.rowcount
        if rows_affected > 0:
            cnxn.commit()
            QMessageBox.information(self, "Success", "Seats updated")
            self.populate_lists()
            for seat in self.seats:
                if seat["status"] == "booked":
                    seat["label_object"].setEnabled(False)
        else:
            QMessageBox.critical(self, "Error", "An error has occured while trying to update the seats")
    
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
        self.addItems(["available","booked"])
        self.currentTextChanged.connect(self.on_change)
        self.myticketlabel = myticketlabel
        self.ui = ui
    
    def on_change(self):
        global Blocked_seats
        seat = self.myticketlabel.text()
        seat = seat[0]+"_"+seat[1]+seat[2]
        if self.currentText() == "Available":
            self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "highlighted.png")
            self.ui.__getattribute__("seat"+seat).setPixmap(QPixmap(self.highlightedabspath))
            Blocked_seats = [dict(t) for t in {tuple(d.items()) for d in Blocked_seats}]
        else:
            self.blockedabspath = os.path.join(os.path.dirname(__file__), "..",'..','guest', "images", "blocked.png")
            self.ui.__getattribute__("seat"+seat).setPixmap(QPixmap(self.blockedabspath))
            Blocked_seats.append({"seat_id":seat,"status":self.currentText()})
def main():
    app = QApplication(sys.argv)
    window = SeatEditorForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()