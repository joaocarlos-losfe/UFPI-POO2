from pessoa import Pessoa
from cadastros_pessoa import Cadastros
from Telas.tela_home import UiHome
from Telas.tela_exibir import UiExibir
from Telas.tela_cadastro import UiCadastro
from Telas.dialogs import Dialogs

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

class MainScreen(QtWidgets.QWidget):

    def setup_ui(self, Main):
        Main.setObjectName('Main')
        Main.resize(600,400)
        self.QtStack = QtWidgets.QStackedLayout()

        self.stck0 = QtWidgets.QMainWindow()
        self.stck1 = QtWidgets.QMainWindow()
        self.stck2 = QtWidgets.QMainWindow()

        self.tela_home = UiHome()
        self.tela_home.setupUi(self.stck0)

        self.tela_cadastro = UiCadastro()
        self.tela_cadastro.setupUi(self.stck1)

        self.tela_exibir = UiExibir()
        self.tela_exibir.setupUi(self.stck2)

        self.QtStack.addWidget(self.stck0) #primeira tela a ser executada
        self.QtStack.addWidget(self.stck1)
        self.QtStack.addWidget(self.stck2)

class Main(QMainWindow, MainScreen):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setup_ui(self)

        self.cadastros = Cadastros()
        self.conexoes()

    def conexoes(self):
        self.tela_home.btn_tela_cadastro.clicked.connect(self.abrir_tela_cadastro)
        self.tela_home.btn_tela_exibir.clicked.connect(self.abrir_tela_exibir)

        self.tela_cadastro.btn_voltar_cadastro.clicked.connect(self.go_to_home)
        self.tela_exibir.btn_exibir_voltar.clicked.connect(self.go_to_home)
        self.tela_cadastro.btn_cadastrar.clicked.connect(self.salvar_cadastro)
        self.tela_exibir.btn_buscar.clicked.connect(self.buscar)

    def cadastro_ok(self, pessoa:Pessoa)-> bool:
        if pessoa.get_nome == '' or pessoa.get_cpf == '' or pessoa.get_endereco == '' or pessoa.get_nascimento == '':
            return False
        else:
            return True

    def limpar_textos(self):
        self.tela_cadastro.le_nome.setText('')
        self.tela_cadastro.le_cpf.setText('')
        self.tela_cadastro.le_endereco.setText('')
        self.tela_cadastro.le_nascimento.setText('')

    def salvar_cadastro(self):
        pessoa = Pessoa(self.tela_cadastro.le_nome.text(), self.tela_cadastro.le_cpf.text(), self.tela_cadastro.le_endereco.text(), self.tela_cadastro.le_nascimento.text())

        if self.cadastro_ok(pessoa):
            self.cadastros.add_pessoa(pessoa)
            self.limpar_textos()
            print("cadastrado...")
        else:
            Dialogs.alert_mensage("Alguns campos estão vazios", "erro ao cadastrar")

    def buscar(self):
        cpf = self.tela_exibir.le_cpf.text()
        p = self.cadastros.get_pessoa(cpf)

        if p is None:
            Dialogs.alert_mensage("Pessoa não encontrada", "erro ao procurar")
        else:
            self.tela_exibir.lbl_nome.setText(p.get_nome)
            self.tela_exibir.lbl_nascimento.setText(p.get_nascimento)
            self.tela_exibir.lbl_endececo.setText(p.get_endereco)

    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_exibir(self):
        self.QtStack.setCurrentIndex(2)

    def go_to_home(self):
        self.QtStack.setCurrentIndex(0)
