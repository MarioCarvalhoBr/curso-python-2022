import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,400)
janela.setWindowTitle("Programa 123")

lbl_texto = QLabel("Bem-vind@!", janela)
lbl_texto.setGeometry(50, 50, 100, 16)

btn_entrar = QPushButton("Entrar ", janela)
btn_entrar.setGeometry(50, 70, 400, 40)

janela.show()
app.exec()
