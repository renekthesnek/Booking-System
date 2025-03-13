import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap

from MainMenu import *

class MainMenuForm(QWidget):
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
        return

    def no_login(self):
        return
    
def main():
    app = QApplication(sys.argv)
    window = MainMenuForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()