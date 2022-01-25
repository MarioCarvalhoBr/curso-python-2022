import os
import sys

PATH_ROOT =  os.path.dirname(__file__)
PATH_BANCO = os.path.join(PATH_ROOT, "banco.csv")
PATH_UI = os.path.join(PATH_ROOT, "tela.ui")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

PATH_BANCO = resource_path("banco.csv")
PATH_UI = resource_path("tela.ui")


# Importa as bibliotecas
from PyQt6 import uic, QtWidgets

from PyQt6.QtWidgets import QDialog, QMessageBox

import pandas as pd
import numpy as np

# Criando a aplicação princial
app = QtWidgets.QApplication([])
global banco
banco = pd.read_csv(PATH_BANCO, sep=";")
# print(banco.to_string())

def enviar():
    titulo = formulario.txt_titulo.text()
    email = formulario.txt_email.text()
    reclamacao = formulario.txt_reclamacao.toPlainText()
    # Monto a linha
    linha = {'Titulo': titulo,
               'Email': email,
               'Reclamacao': reclamacao}
    # Adiciono no banco
    global banco
    banco = banco.append(linha, ignore_index=True)
    # Listar o banco
    listar()

    limpar()
    formulario.lbl_resultado.setText("Reclamaçaão enviada com sucesso!")
def sobre():
    dlg = QMessageBox()
    dlg.setWindowTitle("Sistema de Reclamações")
    dlg.setText("Versão 1.0\nSistema para fazer registro de reclamações.\nPython 3.9.8\nPyQt 6\nAutores: Mário Carvalho")
    button = dlg.exec()

    if button == QMessageBox.StandardButton.Ok:
        print("OK!")

def salvar():
    banco.to_csv(PATH_BANCO, sep=";", index=False)
    formulario.lbl_resultado.setText("Banco de dados salvo com sucesso!")

def limpar():
    formulario.txt_titulo.setText("")
    formulario.txt_email.setText("")
    formulario.txt_reclamacao.setPlainText("")
    formulario.lbl_resultado.setText("Formulário limpo com sucesso!")

def listar():
    if banco.empty:
        formulario.lbl_reclamacoes.setPlainText("Não existem reclamações cadastradas!")
    else:
        formulario.lbl_reclamacoes.setPlainText(banco.to_string())

def sair():
    app.quit()

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window  = uic.loadUiType(PATH_UI)

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

formulario.btn_enviar.clicked.connect(enviar)
# Get click de botão
formulario.btn_limpar.clicked.connect(limpar)

# Get click de item de menu
formulario.menu_add.triggered.connect(salvar)
formulario.menu_sair.triggered.connect(sair)
formulario.menu_sobre.triggered.connect(sobre)

listar()

janela.show()
app.exec()