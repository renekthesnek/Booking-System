import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5.QtWidgets import QApplication, QDialog
if __name__ == "__main__":
    from DataViewer import Ui_Dialog
else:
    from .DataViewer import Ui_Dialog

#change from counting on button click to checking if the buttons text is in the label already, if it is then remove 
#simple right?

class DataViewerForm(QDialog):
    def __init__(self, UserName="No Parsed Username"):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Booking Confirmation")
        self.ui.BackToMenuButton.clicked.connect(self.switch_to_main_menu)
        
        self.usersbutton_click_count = 0
        self.seatsbutton_click_count = 0
        self.performancesbutton_click_count = 0
        self.bookingsbutton_click_count = 0
        self.bookingseatsbutton_click_count = 0
        self.seatstatesbutton_click_count = 0
        
        self.ui.usersbutton.clicked.connect(self.on_usersbutton_clicked)
        self.ui.SeatsButton.clicked.connect(self.on_seatsbutton_clicked)
        self.ui.performancesbutton.clicked.connect(self.on_performancesbutton_clicked)
        self.ui.bookingsbutton.clicked.connect(self.on_bookingsbutton_clicked)
        self.ui.bookingseatsbutton.clicked.connect(self.on_bookingseatsbutton_clicked)
        self.ui.seatstatesbutton.clicked.connect(self.on_seatstatesbutton_clicked)
                
    def on_usersbutton_clicked(self):
        print("on_usersbutton_clicked called")
        self.usersbutton_click_count += 1
        self.updatelabel("Users", self.usersbutton_click_count)
        print(f"Button 1 clicked {self.usersbutton_click_count} times")

    def on_seatsbutton_clicked(self):
        self.seatsbutton_click_count += 1
        self.updatelabel("Seats", self.seatsbutton_click_count)
        print(f"Button 2 clicked {self.seatsbutton_click_count} times")

    def on_performancesbutton_clicked(self):
        self.performancesbutton_click_count += 1
        self.updatelabel("Performances", self.performancesbutton_click_count)
        print(f"Button 3 clicked {self.performancesbutton_click_count} times")

    def on_bookingsbutton_clicked(self):
        self.bookingsbutton_click_count += 1
        self.updatelabel("Bookings", self.bookingsbutton_click_count)
        print(f"Button 4 clicked {self.bookingsbutton_click_count} times")

    def on_bookingseatsbutton_clicked(self):
        self.bookingseatsbutton_click_count += 1
        self.updatelabel("Booking Seats", self.bookingseatsbutton_click_count)
        print(f"Button 5 clicked {self.bookingseatsbutton_click_count} times")

    def on_seatstatesbutton_clicked(self):
        self.seatstatesbutton_click_count += 1
        self.updatelabel("Seat States", self.seatstatesbutton_click_count)
        print(f"Button 6 clicked {self.seatstatesbutton_click_count} times")

        
        
    def updatelabel(self, text, value=None):
        if value is not None:
            currenttext = self.ui.SelectedMultiDisplay.text()
            currenttext += "\n" + str(text) + ": " + str(value)
            self.ui.SelectedMultiDisplay.setText(currenttext)
        
    def switch_to_main_menu(self):
        self.close()
        from StaffMainMenu import StaffConsoleForm
        newwindow = StaffConsoleForm()
        newwindow.show()
        newwindow.exec_()
def main():
    app = QApplication(sys.argv)
    window = DataViewerForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()