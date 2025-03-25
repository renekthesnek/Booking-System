import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from BookingConfirmed import Ui_Dialog
else:
    from .BookingConfirmed import Ui_Dialog
    

#add functionality to show sidepanel images and show booking information
class BookingConfirmedForm(QDialog):
    def __init__(self):
        super(BookingConfirmedForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)
    
    def switch_to_main_menu(self):
        self.close()
        from mainmenu import MainMenuForm
        newwindow = MainMenuForm()
        newwindow.show()
        newwindow.exec_()

def main():
    app = QApplication(sys.argv)
    window = BookingConfirmedForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()