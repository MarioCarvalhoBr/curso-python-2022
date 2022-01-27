# pip install openpyxl
# pip install pandas
# pip install numpy
import sys
import os
import pandas as pd
import numpy as np

from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtCore import QDate,  Qt
from PyQt6.QtWidgets import QMessageBox


def get_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _TEMP
        base_path = getattr(sys, '_MEIPASS', os.getcwd())
    except Exception:
        base_path = os.path.abspath(".")

    path_absolute = os.path.join(base_path, relative_path)
    return path_absolute

# Criação dos caminhos absolutos dos arquivos
PATH_TELA_PRINCIPAL =  get_path("tela.ui")
PATH_BANCO_EXCEL =  get_path("banco.xlsx")
PATH_BANCO_EXCEL_EXPORT =  get_path("novo_banco.xlsx")
PATH_BANCO_CSV_EXPORT=  get_path("novo_banco.csv")

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

        # Conectando os eventos dos botoes
        self.j_main.tbn_calc.clicked.connect(self.main_btn_calc)
        self.j_main.tbn_salvar.clicked.connect(self.main_btn_salvar)
        self.j_main.tbn_load.clicked.connect(self.main_btn_load)

        # Criando o banco de dados
        self.banco =  None
        self.model = None
        # Mostra a janela na tela
        self.j_main.show()
    def main_btn_load(self):
        fname = QFileDialog.getOpenFileName(self, 'Abrir arquivo', 'c:\\',"Excel (*.xlsx *.xls *.csv)")
        print("fname: ", fname)
        # Criando o banco de dados
        arquivo = fname[0]
        extensao = arquivo.split(".")[1]
        if extensao == "xlsx"  or extensao =="xls":
            self.banco =  pd.read_excel(arquivo)
            # Listar o banco de dados
            self.main_listar()
        elif extensao == "csv":
            self.banco =  pd.read_csv(arquivo, sep=";")
            # Listar o banco de dados
            self.main_listar()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("AVISO")
            dlg.setText("Erro na leitura do arquivo.")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                print("OK!")
        
    def main_btn_calc(self):
        # Usar a função loc pra pegar uma linha
        pesos = self.banco.loc[0][1:].to_numpy()

        tam = len(self.banco)

        print("Linhas: ", tam)
        valores = []
        for index in range(1, tam):
            projeto = self.banco.loc[index][1:].to_numpy()
            valores.append(projeto)

        matriz = np.array(valores)

        # Multiplicou o vetor pela matriz
        resultado = matriz @ pesos

        # Concatenando o zero a lista
        escalar = np.array([0])
        coluna = np.concatenate((escalar, resultado), axis=None)

        # Criando uma coluna
        self.banco['resultados'] = coluna

        self.j_main.txt_resultado.setText(str(coluna))
        self.main_listar()

    def main_btn_salvar(self):
        self.banco.to_excel(PATH_BANCO_EXCEL_EXPORT, sheet_name="Planilha1", index=False)
        self.banco.to_csv(PATH_BANCO_CSV_EXPORT, sep=";", index=False)
        dlg = QMessageBox()
        dlg.setWindowTitle("AVISO")
        dlg.setText("Sucesso ao salvar o arquivo.")
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

    def main_listar(self):
        self.model = TableModel(self.banco)
        self.j_main.tb_dados.setModel(self.model)

app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec()