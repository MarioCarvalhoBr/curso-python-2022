# Form implementation generated from reading ui file 'c:\Users\Estudante\Desktop\Projetos Python\curso-python-2022\modulo-2\cadastro_clientes\editar.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 49, 16))
        self.label_6.setObjectName("label_6")
        self.btnr_m = QtWidgets.QRadioButton(self.centralwidget)
        self.btnr_m.setGeometry(QtCore.QRect(100, 110, 31, 20))
        self.btnr_m.setObjectName("btnr_m")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 49, 16))
        self.label_7.setObjectName("label_7")
        self.btn_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salvar.setGeometry(QtCore.QRect(174, 420, 121, 41))
        self.btn_salvar.setObjectName("btn_salvar")
        self.txt_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_idade.setGeometry(QtCore.QRect(60, 80, 61, 22))
        self.txt_idade.setObjectName("txt_idade")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 49, 16))
        self.label_3.setObjectName("label_3")
        self.cb_cor = QtWidgets.QComboBox(self.centralwidget)
        self.cb_cor.setGeometry(QtCore.QRect(20, 190, 69, 22))
        self.cb_cor.setObjectName("cb_cor")
        self.cb_cor.addItem("")
        self.cb_cor.addItem("")
        self.cb_cor.addItem("")
        self.txt_obs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_obs.setGeometry(QtCore.QRect(20, 240, 281, 171))
        self.txt_obs.setObjectName("txt_obs")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 49, 16))
        self.label_5.setObjectName("label_5")
        self.date_data_nasc = QtWidgets.QDateEdit(self.centralwidget)
        self.date_data_nasc.setGeometry(QtCore.QRect(100, 140, 110, 22))
        self.date_data_nasc.setObjectName("date_data_nasc")
        self.btnr_f = QtWidgets.QRadioButton(self.centralwidget)
        self.btnr_f.setGeometry(QtCore.QRect(60, 110, 31, 20))
        self.btnr_f.setObjectName("btnr_f")
        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(20, 420, 131, 41))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(60, 50, 241, 22))
        self.txt_nome.setObjectName("txt_nome")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 51, 21))
        self.label.setObjectName("label")
        self.txt_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cpf.setGeometry(QtCore.QRect(60, 20, 241, 22))
        self.txt_cpf.setObjectName("txt_cpf")
        self.btnr_ni = QtWidgets.QRadioButton(self.centralwidget)
        self.btnr_ni.setGeometry(QtCore.QRect(140, 110, 41, 20))
        self.btnr_ni.setObjectName("btnr_ni")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar"))
        self.label_4.setText(_translate("MainWindow", "Data de nasc."))
        self.label_6.setText(_translate("MainWindow", "OBS: "))
        self.btnr_m.setText(_translate("MainWindow", "M"))
        self.label_2.setText(_translate("MainWindow", "Idade:"))
        self.label_7.setText(_translate("MainWindow", "Cor:"))
        self.btn_salvar.setText(_translate("MainWindow", "SALVAR"))
        self.label_3.setText(_translate("MainWindow", "Sexo:"))
        self.cb_cor.setItemText(0, _translate("MainWindow", "Pardo"))
        self.cb_cor.setItemText(1, _translate("MainWindow", "Branco"))
        self.cb_cor.setItemText(2, _translate("MainWindow", "Negro"))
        self.label_5.setText(_translate("MainWindow", "CPF:"))
        self.btnr_f.setText(_translate("MainWindow", "F"))
        self.btn_cancelar.setText(_translate("MainWindow", "CANCELAR"))
        self.label.setText(_translate("MainWindow", "Nome: "))
        self.btnr_ni.setText(_translate("MainWindow", "NI"))
