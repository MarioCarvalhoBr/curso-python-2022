from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui_pyqt6/hello/tela.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.lbl_resultado.setText("Mario")


window.show()
app.exec()