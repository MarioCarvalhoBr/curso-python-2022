from PyQt6 import uic, QtWidgets

def chamar_tela2():
    tela2.show()
app = QtWidgets.QApplication([])

tela1 = uic.loadUi("tela1.ui")
tela2 = uic.loadUi("tela2.ui")

tela1.btn_chamar.clicked.connect(chamar_tela2)

tela1.show()

app.exec()