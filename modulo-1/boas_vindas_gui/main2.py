# Carrega o layout .ui
from PyQt6 import uic, QtWidgets

def funcao():
   nome = formulario.txt_nome.text()
   formulario.lbl_resultado.setText(f"Seja bem-vind@ {nome}!")

app = QtWidgets.QApplication([])
Form, Window  = uic.loadUiType("boas_vindas_gui/janela.ui")
window = Window()
formulario = Form()
formulario.setupUi(window)

formulario.btn_entrar.clicked.connect(funcao)
window.show()
app.exec()