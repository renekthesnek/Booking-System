import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from StaffConsole import Ui_Dialog
else:
    from .StaffConsole import Ui_Dialog

from mainmenu import MainMenuForm

class StaffConsoleForm(QDialog):
    def __init__(self):
        super(StaffConsoleForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)

    def switch_to_main_menu(self):
        self.close()
        newwindow = MainMenuForm()
        newwindow.show()
        newwindow.exec_()
def main():
    app = QApplication(sys.argv)
    window = StaffConsoleForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()