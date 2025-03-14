import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from CreateEditConsole import Ui_Dialog
else:
    from .CreateEditConsole import Ui_Dialog



class CreateEditConsoleForm(QDialog):
    def __init__(self):
        super(CreateEditConsoleForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_Staff_console)

    def switch_to_Staff_console(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
def main():
    app = QApplication(sys.argv)
    window = CreateEditConsoleForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()