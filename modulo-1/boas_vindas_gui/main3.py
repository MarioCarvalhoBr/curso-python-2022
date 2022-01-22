# Importa as bibliotecas
from PyQt6 import uic, QtWidgets

# Criando a aplicação princial
app = QtWidgets.QApplication([])

Form, Window  = uic.loadUiType("boas_vindas_gui/janela.ui")
window = Window()
formulario = Form()
formulario.setupUi(window)

window.show()
app.exec()