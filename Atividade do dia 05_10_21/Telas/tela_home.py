# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiHome(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(600, 400)
        home.setMinimumSize(QtCore.QSize(600, 400))
        home.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        home.setFont(font)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_tela_exibir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tela_exibir.setObjectName("btn_tela_exibir")
        self.gridLayout.addWidget(self.btn_tela_exibir, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_tela_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tela_cadastro.setObjectName("btn_tela_cadastro")
        self.gridLayout.addWidget(self.btn_tela_cadastro, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        home.setCentralWidget(self.centralwidget)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "home"))
        self.btn_tela_exibir.setText(_translate("home", "Exibir"))
        self.btn_tela_cadastro.setText(_translate("home", "Cadastrar"))