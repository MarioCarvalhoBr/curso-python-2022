# Importa as bibliotecas
import os
import pandas as pd
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.abspath(".")
    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute

def btn_excluir():
    dlg = QMessageBox()
    dlg.setWindowTitle("AVISO")
    dlg.setText("Deseja excluír?")
    button = dlg.exec()

    if button == QMessageBox.StandardButton.Ok:
        print("SIM!")
    if button == QMessageBox.StandardButton.No:
        print("NAO!")

def limpar():
    pass

def btn_cancelar_add():
    janela_add.close()

def btn_salvar_add():
    cpf = janela_add.txt_cpf.text()
    nome = janela_add.txt_nome.text()
    idade = janela_add.txt_idade.text()

    sexo = ''
    if janela_add.btnr_f.isChecked():
        print("Selecionou F")
        sexo = 'F'
    if janela_add.btnr_m.isChecked():
        print("Selecionou M")
        sexo = 'M'

    obs = janela_add.txt_obs.toPlainText()
    date = str(janela_add.date_data_nasc.date().toString())
    cor = janela_add.cb_cor.currentText()
    # Monto a linha
    linha = {'CPF': cpf,
               'Nome': nome,
               'Idade': idade,
               'Sexo': sexo,
               'Data_Nasc': date,
               'Cor': cor,
               'OBS': obs
               }
    # Adiciono no banco
    global banco
    banco = banco.append(linha, ignore_index=True)
    # Listar o banco
    listar()
    btn_cancelar_add()
    banco.to_csv(PATH_BANCO_CSV, sep=";", index=False)

def listar():
    if banco.empty:
        janela_principal.list_dados.addItem("Não existem clientes cadastradas!")
        #janela_principal.txt_tabela.setPlainText("Não existem clientes cadastradas!")
    else:
        # janela_principal.txt_tabela.setPlainText(banco.to_string())
        for i in range(len(banco)):
            linha = banco.loc[i]
            linha_dic = linha.to_list()
            janela_principal.list_dados.addItem(str(linha_dic))

def btn_add():
    janela_add.show()

def btn_editar():
    janela_editar.show()

# Criação dos caminhos absolutos dos arquivos
PATH_TELA_PRINCIPAL =  resource_path("principal.ui")
PATH_TELA_ADD =  resource_path("add.ui")
PATH_TELA_EDITAR =  resource_path("editar.ui")
PATH_BANCO_CSV =  resource_path("banco.csv")

# Criando a aplicação princial
app = QtWidgets.QApplication([])
global banco
banco = pd.read_csv(PATH_BANCO_CSV, sep=";")

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
janela_principal = uic.loadUi(PATH_TELA_PRINCIPAL)
janela_add = uic.loadUi(PATH_TELA_ADD)
janela_editar = uic.loadUi(PATH_TELA_EDITAR)

janela_principal.btn_add.clicked.connect(btn_add)
janela_principal.btn_editar.clicked.connect(btn_editar)
janela_principal.btn_excluir.clicked.connect(btn_excluir)

janela_add.btn_salvar.clicked.connect(btn_salvar_add)
janela_add.btn_cancelar.clicked.connect(btn_cancelar_add)

listar()
# Mostra a tela
janela_principal.show()
app.exec()