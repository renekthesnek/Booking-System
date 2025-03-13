import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == "__main__":
    from ConfirmBooking import Ui_Dialog
else:
    from .ConfirmBooking import Ui_Dialog

class ConfirmBookingForm(QDialog):
    def __init__(self):
        super(ConfirmBookingForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = ConfirmBookingForm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()