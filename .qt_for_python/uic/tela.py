# Form implementation generated from reading ui file 'c:\Users\Estudante\Desktop\Projetos Python\curso-python-2022\modulo-2\boas_vindas_gui\tela.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(257, 169)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_top = QtWidgets.QLabel(self.centralwidget)
        self.lbl_top.setGeometry(QtCore.QRect(50, 0, 131, 16))
        self.lbl_top.setObjectName("lbl_top")
        self.lbl_nome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome.setGeometry(QtCore.QRect(20, 30, 49, 16))
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(60, 30, 161, 22))
        self.txt_nome.setObjectName("txt_nome")
        self.btn_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enviar.setGeometry(QtCore.QRect(150, 60, 75, 24))
        self.btn_enviar.setObjectName("btn_enviar")
        self.lbl_resultado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_resultado.setGeometry(QtCore.QRect(20, 90, 201, 16))
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.btn_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpar.setGeometry(QtCore.QRect(60, 60, 75, 24))
        self.btn_limpar.setObjectName("btn_limpar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 257, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_top.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">DADOS DO USUÁRIO</span></p></body></html>"))
        self.lbl_nome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Nome:</span></p></body></html>"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))
        self.lbl_resultado.setText(_translate("MainWindow", "Resultado:"))
        self.btn_limpar.setText(_translate("MainWindow", "Limpar"))