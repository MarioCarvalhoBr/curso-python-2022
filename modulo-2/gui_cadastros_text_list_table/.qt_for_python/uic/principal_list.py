# Form implementation generated from reading ui file 'c:\Users\Estudante\Desktop\Projetos Python\curso-python-2022\modulo-2\cadastro_clientes\principal_list.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 350, 641, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_editar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout.addWidget(self.btn_editar)
        self.btn_excluir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_excluir.setObjectName("btn_excluir")
        self.horizontalLayout.addWidget(self.btn_excluir)
        self.list_dados = QtWidgets.QListWidget(self.centralwidget)
        self.list_dados.setGeometry(QtCore.QRect(60, 61, 641, 271))
        self.list_dados.setObjectName("list_dados")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 15, 201, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 631, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CADASTRO DE CLIENTES"))
        self.btn_add.setText(_translate("MainWindow", "Adicionar"))
        self.btn_editar.setText(_translate("MainWindow", "Editar"))
        self.btn_excluir.setText(_translate("MainWindow", "Excluir"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">CLIENTES CADASTRADOS</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">CPF | Nome | Idade | Sexo | Data_Nasc | Cor | OBS</span></p></body></html>"))