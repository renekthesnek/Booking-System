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
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Menu")
        self.ui.guestloginbutton.clicked.connect(self.guest_login)
        self.ui.staffloginbutton.clicked.connect(self.staff_login)
        self.ui.nologinbutton.clicked.connect(self.no_login)

    def guest_login(self):
        return

    def staff_login(self):
        username = self.ui.StaffLoginUsername.text()
        password = self.ui.StaffLoginPassword.text()
        passwordhash = hashlib.sha224(password.encode()).hexdigest()

        cnxn = self.connect()
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ? AND password_hash = ?", (username, passwordhash))
        data = cursor.fetchone()
        cursor.close()
        cnxn.close()
        
        if data is not None:
            self.switch_to_staff_console(username)
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
            return

    def no_login(self):
        self.switch_to_seatselector()

    def switch_to_seatselector(self):
        self.close()
        newwindow = SeatSelectionForm()
        newwindow.show()
        newwindow.exec_()
        
    def switch_to_staff_console(self,UserName):
        self.close()
        from Staff import StaffConsoleForm
        newwindow = StaffConsoleForm(UserName)
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