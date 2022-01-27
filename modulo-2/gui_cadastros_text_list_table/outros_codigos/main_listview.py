# Importa as bibliotecas
import os
import pandas as pd
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QDate

global janela_add
janela_add = None

global janela_editar
janela_editar = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = os.path.abspath(".")
    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute

# Criação dos caminhos absolutos dos arquivos
PATH_TELA_PRINCIPAL =  resource_path("principal.ui")
PATH_TELA_ADD =  resource_path("add.ui")
PATH_TELA_EDITAR =  resource_path("editar.ui")
PATH_BANCO_CSV =  resource_path("banco.csv")

def btn_excluir():
    global banco
    global janela_principal
    index = janela_principal.list_dados.currentRow()
    if index != -1:
        dados = banco.loc[index]

        opcao = QMessageBox.question(janela_principal,'AVISO', f"Deseja excluír os dados de {dados[1]}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        
        if opcao == QMessageBox.StandardButton.Yes:
            # delete a single row by index value 0
            banco = banco.drop(labels=index, axis=0)
            banco.to_csv(PATH_BANCO_CSV, sep=";", index=False)
            # Resetando os indices
            banco.reset_index(drop=True, inplace=True)

        if opcao == QMessageBox.StandardButton.No:
            print('No clicked.')
        listar()
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("AVISO")
        dlg.setText("Você precisa selecionar uma linha na lista!")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")
def limpar():
    pass

def btn_cancelar_editar():
    global janela_editar
    janela_editar.close()
    del janela_editar

def btn_cancelar_add():
    global janela_add
    janela_add.close()
    del janela_add

def btn_editar_add(index):
    global janela_editar
    cpf = janela_editar.txt_cpf.text()
    nome = janela_editar.txt_nome.text()
    idade = janela_editar.txt_idade.text()

    sexo = ''
    if janela_editar.btnr_f.isChecked():
        print("Selecionou F")
        sexo = 'F'
    if janela_editar.btnr_m.isChecked():
        print("Selecionou M")
        sexo = 'M'

    obs = janela_editar.txt_obs.toPlainText()
    date = str(janela_editar.date_data_nasc.date().toString("dd/MM/yyyy"))
    cor = janela_editar.cb_cor.currentText()
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
    banco.loc[index] = linha
    # Listar o banco
    listar()
    btn_cancelar_editar()
    banco.to_csv(PATH_BANCO_CSV, sep=";", index=False)

def btn_salvar_add():
    global janela_add
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
    date = str(janela_add.date_data_nasc.date().toString("dd/MM/yyyy"))
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
    global janela_principal
    global banco
    print("banco: ", banco)
    # limpa a lista atual
    janela_principal.list_dados.clear()

    # Atualiza a lista limpa com novos dados
    if banco.empty:
        janela_principal.list_dados.addItem("Não existem clientes cadastradas!")
        #janela_principal.txt_tabela.setPlainText("Não existem clientes cadastradas!")
    else:
        # janela_principal.txt_tabela.setPlainText(banco.to_string())
        for i in banco.index:
            print("IMARIO: ", i)
            linha = banco.loc[i]
            linha_dic = linha.to_list()
            janela_principal.list_dados.addItem(str(linha_dic))

def btn_add():
    global janela_add
    janela_add = uic.loadUi(PATH_TELA_ADD)
    janela_add.btn_salvar.clicked.connect(btn_salvar_add)
    janela_add.btn_cancelar.clicked.connect(btn_cancelar_add)

    janela_add.show()

def btn_editar():
    global janela_editar
    # Pega os dados do click
    index = janela_principal.list_dados.currentRow()
    
    if index != -1:
        dados = banco.loc[index]
        # print("Dados: ", dados)

        # Cria a janela de editar
        janela_editar = uic.loadUi(PATH_TELA_EDITAR)
        janela_editar.btn_salvar.clicked.connect(lambda: btn_editar_add(index))
        janela_editar.btn_cancelar.clicked.connect(btn_cancelar_add)

        # Seta os dados da seleção
        janela_editar.txt_cpf.setText(str(dados[0]))
        janela_editar.txt_nome.setText(dados[1])
        janela_editar.txt_idade.setText(str(dados[2]))
        sexo = str(dados[3])

        if sexo == 'F':
            janela_editar.btnr_f.setChecked(True)
        if sexo == 'M':
            janela_editar.btnr_m.setChecked(True)

        # Trabalhando com datas
        lista_data = dados[4].split("/") #Transforma a data em uma lista [dia, mes, ano]
        # Pega os dados do dia, mes e ano
        dia = int(lista_data[0]) 
        mes = int(lista_data[1])
        ano = int(lista_data[2])
        # Seta a os dados da data
        janela_editar.date_data_nasc.setDate(QDate(ano, mes, dia))

        cor = str(dados[5])
        janela_editar.cb_cor.setCurrentText(cor)

        obs = dados[6]
        janela_editar.txt_obs.setPlainText(obs)

        janela_editar.show()
    else:
        dlg = QMessageBox()
        dlg.setWindowTitle("AVISO")
        dlg.setText("Você precisa selecionar uma linha na lista!")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

# Criando a aplicação princial
app = QtWidgets.QApplication([])
global banco
banco = pd.read_csv(PATH_BANCO_CSV, sep=";")

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
janela_principal = uic.loadUi(PATH_TELA_PRINCIPAL)

janela_editar = uic.loadUi(PATH_TELA_EDITAR)

janela_principal.btn_add.clicked.connect(btn_add)
janela_principal.btn_editar.clicked.connect(btn_editar)
janela_principal.btn_excluir.clicked.connect(btn_excluir)

listar()
# Mostra a tela
janela_principal.show()
app.exec()