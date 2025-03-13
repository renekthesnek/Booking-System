import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog
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
        return

    def no_login(self):
        self.switch_to_seatselector()

    def switch_to_seatselector(self):
        self.close()
        newwindow = SeatSelectionForm()
        newwindow.show()
        newwindow.exec_()

def main():
    app = QApplication(sys.argv)
    window = MainMenuForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()