import sys
import os
import pandas as pd

from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate,  Qt

# Arquivos que não são alterados durante a execução do programa
# .ico, .ui
def get_path_static(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute

# Arquivos que SÃO alterados durante a execução do programa
# bancos de dados, banco.csv, arquivo.txt
def get_path_dynamic(relative_path):
    base_path = os.path.abspath(".")
    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute


# Criação dos caminhos absolutos dos arquivos dos arquivos estáticos
PATH_TELA_PRINCIPAL = get_path_static("principal_table.ui")
PATH_TELA_ADD = get_path_static("add.ui")
PATH_TELA_EDITAR = get_path_static("editar.ui")

# Criação dos caminhos absolutos dos arquivos dos arquivos dinâmicos
PATH_BANCO_CSV = get_path_dynamic("banco.csv")

# Caso o banco de dados não exista: CRIA UM NOVO BANCO VAZIO
if not os.path.exists(PATH_BANCO_CSV):
    linha = {'CPF': [],
             'Nome':[],
             'Idade':[],
             'Sexo':[],
             'Data_Nasc':[],
             'Cor':[],
             'OBS': []}
    df_banco = pd.DataFrame(linha)
    df_banco.to_csv(PATH_BANCO_CSV, sep=";", index=False)


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])


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
        self.model = None
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
        obj_click = self.j_main.table_dados.currentIndex()
        index = obj_click.row()
        coluna = obj_click.column()

        # Verifica se o click foi acionado
        if index != -1:
            dados = self.banco.loc[index]
            # Cria a janela de editar
            self.j_editar = uic.loadUi(PATH_TELA_ADD)
            self.j_editar.btn_salvar.clicked.connect(
                lambda: self.editar_btn_salvar(index))
            self.j_editar.btn_cancelar.clicked.connect(
                self.editar_btn_cancelar)

            # Seta os dados da seleção
            self.j_editar.txt_cpf.setText(str(dados[0]))
            self.j_editar.txt_nome.setText(dados[1])
            self.j_editar.txt_idade.setText(str(dados[2]))
            sexo = str(dados[3])

            if sexo == 'F':
                self.j_editar.btnr_f.setChecked(True)
            elif sexo == 'M':
                self.j_editar.btnr_m.setChecked(True)
            elif sexo == 'NI':
                self.j_editar.btnr_ni.setChecked(True)
            else:
                self.j_editar.btnr_ni.setChecked(True)

            # Trabalhando com datas
            # Transforma a data em uma lista [dia, mes, ano]
            lista_data = dados[4].split("/")

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
        obj_click = self.j_main.table_dados.currentIndex()
        linha = obj_click.row()
        coluna = obj_click.column()
        if linha != -1:
            dados = self.banco.loc[linha]

            opcao = QMessageBox.question(
                self.j_main, 'AVISO', f"Deseja excluír os dados de {dados[1]}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

            if opcao == QMessageBox.StandardButton.Yes:
                # delete a single row by index value 0
                self.banco = self.banco.drop(labels=linha, axis=0)
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
        elif self.j_editar.btnr_m.isChecked():
            print("Selecionou M")
            sexo = 'M'
        elif self.j_editar.btnr_ni.isChecked():
            sexo = 'NI'
        else:
            sexo = 'NI'

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
        elif self.j_add.btnr_m.isChecked():
            print("Selecionou M")
            sexo = 'M'
        elif self.j_add.btnr_ni.isChecked():
            sexo = 'NI'
        else:
            sexo = 'NI'

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
        self.model = TableModel(self.banco)
        self.j_main.table_dados.setModel(self.model)


app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec()
