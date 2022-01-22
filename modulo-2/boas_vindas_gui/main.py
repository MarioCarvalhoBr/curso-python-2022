# Importa as bibliotecas
from PyQt6 import uic, QtWidgets

def boas_vindas():
    nome = formulario.txt_nome.text()
    formulario.lbl_resultado.setText(f"Bem-vind@ {nome}")

def limpar():
    formulario.lbl_resultado.setText(f"Clicou em limpar")
    formulario.txt_nome.setText("")

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window  = uic.loadUiType("modulo-2/boas_vindas_gui/tela.ui")

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

formulario.btn_enviar.clicked.connect(boas_vindas)
formulario.btn_limpar.clicked.connect(limpar)

janela.show()
app.exec()