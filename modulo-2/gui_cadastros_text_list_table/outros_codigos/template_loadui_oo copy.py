from PyQt6 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('principal.ui', self)
        self.show()

app = QtWidgets.QApplication([])
window = Ui()
app.exec()