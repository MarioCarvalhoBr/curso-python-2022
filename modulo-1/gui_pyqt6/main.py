import sys
from PyQt6.QtWidgets import QApplication,QSpacerItem, QWidget, QPushButton, QLabel, QLineEdit

def funcao():
    nome = txt_nome.text()
    idade = int(txt_idade.text())
    if idade >= 18:
        lbl_resultado.setText(f"Seja bem-vind@ {nome}.\nVocê tem idade pra acessar: {idade}")
        lbl_resultado.adjustSize()
    else:
        lbl_resultado.setText(f"Acesso negado para o usuário {nome}.\nVocê não tem idade pra acessar: {idade}")
        lbl_resultado.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,500)
janela.setWindowTitle("Programa 123")

lbl_texto = QLabel("Bem-vind@!", janela)
lbl_texto.setGeometry(20, 10, 100, 16)

lbl_nome = QLabel("Nome: ", janela)
lbl_nome.setGeometry(20, 40, 100, 16)

txt_nome = QLineEdit(janela)
txt_nome.setGeometry(60, 40, 201, 22)

lbl_idade = QLabel("Idade: ", janela)
lbl_idade.setGeometry(20, 70, 100, 16)

txt_idade = QLineEdit(janela)
txt_idade.setGeometry(60, 70, 201, 22)

tbn_idade = QPushButton("Entrar", janela)
tbn_idade.setGeometry(20, 100, 100, 40)

tbn_idade.clicked.connect(funcao)

lbl_resultado = QLabel("Resultado: ", janela)
lbl_resultado.setGeometry(20, 150, 100, 16)
lbl_resultado.setStyleSheet("font-size:20px")


janela.show()
app.exec()
