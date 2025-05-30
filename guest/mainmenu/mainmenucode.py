import sys
import os 
import hashlib
import pyodbc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap

from seatselector import SeatSelectionForm


if __name__ == "__main__":
    from MainMenu import Ui_Dialog
else:
    from .MainMenu import Ui_Dialog


class MainMenuForm(QDialog):
    def __init__(self, username = "No Parsed Username"):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Menu")
        self.ui.guestloginbutton.clicked.connect(self.guest_login)
        self.ui.staffloginbutton.clicked.connect(self.staff_login)
        self.ui.nologinbutton.clicked.connect(self.no_login)
        self.ui.guestloginbutton.setFocus()
        self.username = username

    def guest_login(self):
        self.username = self.ui.GuestLoginUsernameInput.text()
        password = self.ui.GuestLoginPasswordInput.text()
        passwordhash = hashlib.sha224(password.encode()).hexdigest()

        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ? AND password_hash = ? or email = ? AND password_hash = ?", (self.username, passwordhash, self.username, passwordhash))
        data = cursor.fetchone()
        if data is not None:
            self.switch_to_seatselector()
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
            return

    def staff_login(self): 
        self.username = self.ui.StaffLoginUsername.text()
        password = self.ui.StaffLoginPassword.text()
        passwordhash = hashlib.sha224(password.encode()).hexdigest()

        try:
            cnxn = self.connect()
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = ? AND password_hash = ?", (self.username, passwordhash))
            data = cursor.fetchone()
            permission = data[7]
            cursor.close()
            cnxn.close()
        except:
            data = None
        
        if data is not None and permission == 'Staff':
            self.switch_to_staff_console()
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
            return

    def no_login(self):
        self.switch_to_seatselector()


    def switch_to_seatselector(self):
        self.close()
        newwindow = SeatSelectionForm(self.username)
        newwindow.show()
        newwindow.exec_()
        
    def switch_to_staff_console(self):
        self.close()
        from Staff import StaffConsoleForm
        newwindow = StaffConsoleForm(self.username)
        newwindow.show()
        newwindow.exec_()
    
    def connect (self):
        fileabspath = self.highlightedabspath = os.path.join(os.path.dirname(__file__), "..", "..", "databaselogin.txt")
        with open(fileabspath, 'r') as f:
            cs = f.read()
        cnxn = pyodbc.connect(cs)
        return cnxn

def main():
    app = QApplication(sys.argv)
    window = MainMenuForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()