# Carrega o layout .ui
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

def funcao():
   nome = form.txt_nome.text()
   form.lbl_resultado.setText(f"Seja bem-vind@ {nome}!")

Form, Window = uic.loadUiType("boas_vindas_gui/janela.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.btn_entrar.clicked.connect(funcao)
window.show()
app.exec()