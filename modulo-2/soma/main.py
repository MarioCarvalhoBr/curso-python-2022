# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
import funcoes
def click_btn_somar():
    funcoes.somar(formulario)

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window  = uic.loadUiType("modulo-2/soma/tela.ui")

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

formulario.btn_somar.clicked.connect(lambda: funcoes.somar(formulario))
# formulario.btn_somar.clicked.connect(click_btn_somar)

janela.show()
app.exec()