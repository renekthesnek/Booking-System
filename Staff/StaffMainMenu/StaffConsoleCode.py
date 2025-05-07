import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from StaffConsole import Ui_Dialog
else:
    from .StaffConsole import Ui_Dialog

#add the two remaining panels

class StaffConsoleForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        super(StaffConsoleForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Staff console")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)
        self.ui.ToPeformanceMenuButton.clicked.connect(self.switch_to_CreateEditConsole)
        self.ui.EditSeatsForPeformanceButton.clicked.connect(self.switch_to_seat_editor)
        self.ui.ProcessBookingsButton.clicked.connect(self.switch_to_approve_bookings)
        if UserName == "No Parsed Username":
            self.ui.loggedindisplay.setText("Not Logged In")
        else:
            self.ui.loggedindisplay.setText("logged in as " + UserName)
            
    

    def switch_to_main_menu(self):
        self.close()
        from guest import MainMenuForm
        newwindow = MainMenuForm()
        newwindow.show()
        newwindow.exec_()
    
    def switch_to_CreateEditConsole(self):
        self.close()
        from CreateEdit import CreateEditConsoleForm
        newwindow = CreateEditConsoleForm()
        newwindow.show()
        newwindow.exec_()
    
    def switch_to_seat_editor(self):
        self.close()
        from EditSeats import SeatEditorForm
        newwindow = SeatEditorForm()
        newwindow.show()
        newwindow.exec_()
        
    def switch_to_approve_bookings(self):
        self.close()
        from BookingApprove import ApproveBookingsForm
        newwindow = ApproveBookingsForm()
        newwindow.show()
        newwindow.exec_()
def main():
    app = QApplication(sys.argv)
    window = StaffConsoleForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()