import sys
import os
import pandas as pd

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate

def get_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _TEMP
        base_path = sys._TEMP
    except Exception:
        base_path = os.path.abspath(".")

    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute

# Criação dos caminhos absolutos dos arquivos
PATH_TELA_PRINCIPAL =  get_path("principal_list.ui")
PATH_TELA_ADD =  get_path("add.ui")
PATH_TELA_EDITAR =  get_path("editar.ui")
PATH_BANCO_CSV =  get_path("banco.csv")

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        # Janelas da aplicacao
        self.j_main = uic.loadUi(PATH_TELA_PRINCIPAL)
        self.j_add = None
        self.j_editar = None

        # Conectando os eventos dos botoes
        self.j_main.btn_add.clicked.connect(self.main_btn_add)
        self.j_main.btn_editar.clicked.connect(self.main_btn_editar)
        self.j_main.btn_excluir.clicked.connect(self.main_btn_excluir)

        # Criando o banco de dados
        self.banco = pd.read_csv(PATH_BANCO_CSV, sep=";")
        # Listar o banco de dados
        self.main_listar()
        # Mostra a janela na tela
        self.j_main.show()

    def main_btn_add(self):
        # Carrega a janela
        self.j_add = uic.loadUi(PATH_TELA_ADD)
        # Conectando os eventos dos botoes
        self.j_add.btn_salvar.clicked.connect(self.add_btn_salvar)
        self.j_add.btn_cancelar.clicked.connect(self.add_btn_cancelar)
        # Mostra a janela na tela
        self.j_add.show()
    
    def main_btn_editar(self):
        # Pega o índice do click na lista
        index = self.j_main.list_dados.currentRow()

        # Verifica se o click foi acionado
        if index != -1:
            dados = self.banco.loc[index]
            # Cria a janela de editar
            self.j_editar = uic.loadUi(PATH_TELA_ADD)
            self.j_editar.btn_salvar.clicked.connect(lambda: self.editar_btn_salvar(index))
            self.j_editar.btn_cancelar.clicked.connect(self.editar_btn_cancelar)

            # Seta os dados da seleção
            self.j_editar.txt_cpf.setText(str(dados[0]))
            self.j_editar.txt_nome.setText(dados[1])
            self.j_editar.txt_idade.setText(str(dados[2]))
            sexo = str(dados[3])

            if sexo == 'F':
                self.j_editar.btnr_f.setChecked(True)
            if sexo == 'M':
                self.j_editar.btnr_m.setChecked(True)

            # Trabalhando com datas
            lista_data = dados[4].split("/") #Transforma a data em uma lista [dia, mes, ano]
            
            # Pega os dados do dia, mes e ano
            dia = int(lista_data[0]) 
            mes = int(lista_data[1])
            ano = int(lista_data[2])
            # Seta a os dados da data
            self.j_editar.date_data_nasc.setDate(QDate(ano, mes, dia))

            cor = str(dados[5])
            self.j_editar.cb_cor.setCurrentText(cor)

            obs = dados[6]
            self.j_editar.txt_obs.setPlainText(obs)
            # Mostra a janela
            self.j_editar.show()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("AVISO")
            dlg.setText("Você precisa selecionar uma linha na lista!")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")
    
    def main_btn_excluir(self):
        index = self.j_main.list_dados.currentRow()
        if index != -1:
            dados = self.banco.loc[index]

            opcao = QMessageBox.question(self.j_main,'AVISO', f"Deseja excluír os dados de {dados[1]}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            
            if opcao == QMessageBox.StandardButton.Yes:
                # delete a single row by index value 0
                self.banco = self.banco.drop(labels=index, axis=0)
                self.salvar_banco()
                # Resetando os indices
                self.banco.reset_index(drop=True, inplace=True)

            if opcao == QMessageBox.StandardButton.No:
                print('No clicked.')
            self.main_listar()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("AVISO")
            dlg.setText("Você precisa selecionar uma linha na lista!")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

    def editar_btn_salvar(self, index):
        cpf = self.j_editar.txt_cpf.text()
        nome = self.j_editar.txt_nome.text()
        idade = self.j_editar.txt_idade.text()

        sexo = ''
        if self.j_editar.btnr_f.isChecked():
            print("Selecionou F")
            sexo = 'F'
        if self.j_editar.btnr_m.isChecked():
            print("Selecionou M")
            sexo = 'M'

        obs = self.j_editar.txt_obs.toPlainText()
        date = str(self.j_editar.date_data_nasc.date().toString("dd/MM/yyyy"))
        cor = self.j_editar.cb_cor.currentText()
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
        self.banco.loc[index] = linha
        # Listar o banco
        self.main_listar()
        # Fechar a janela
        self.editar_btn_cancelar()
        # Salvar o banco de dados
        self.salvar_banco()
    
    def editar_btn_cancelar(self):
        self.j_editar.close()
        del self.j_editar

    def add_btn_salvar(self):
        cpf = self.j_add.txt_cpf.text()
        nome = self.j_add.txt_nome.text()
        idade = self.j_add.txt_idade.text()

        sexo = ''
        if self.j_add.btnr_f.isChecked():
            print("Selecionou F")
            sexo = 'F'
        if self.j_add.btnr_m.isChecked():
            print("Selecionou M")
            sexo = 'M'

        obs = self.j_add.txt_obs.toPlainText()
        date = str(self.j_add.date_data_nasc.date().toString("dd/MM/yyyy"))
        cor = self.j_add.cb_cor.currentText()
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
        self.banco = self.banco.append(linha, ignore_index=True)
        # Listar o banco
        self.main_listar()
        self.add_btn_cancelar()
        self.salvar_banco()

    def add_btn_cancelar(self):
        self.j_add.close()
        del self.j_add

    def salvar_banco(self):
        self.banco.to_csv(PATH_BANCO_CSV, sep=";", index=False)
    
    def main_listar(self):
        # limpa a lista atual
        self.j_main.list_dados.clear()

        # Atualiza a lista limpa com novos dados
        if self.banco.empty:
            self.j_main.list_dados.addItem("Não existem clientes cadastradas!")
        else:
            for i in self.banco.index:
                linha = self.banco.loc[i]
                linha_dic = linha.to_list()
                self.j_main.list_dados.addItem(str(linha_dic))

app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec()