from pessoa import Pessoa

from PyQt5 import QtCore, QtGui, QtWidgets

class UiCadastro(object):

    def __init__(self):
        self.pessoa = None

    def setupUi(self, tela_cadastro):
        tela_cadastro.setObjectName("tela_cadastro")
        tela_cadastro.resize(600, 400)
        tela_cadastro.setMinimumSize(QtCore.QSize(600, 400))
        tela_cadastro.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        tela_cadastro.setFont(font)
        self.centralwidget = QtWidgets.QWidget(tela_cadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.le_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.le_nome.setMinimumSize(QtCore.QSize(400, 0))
        self.le_nome.setObjectName("le_nome")
        self.horizontalLayout_6.addWidget(self.le_nome)
        spacerItem1 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.le_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cpf.setMinimumSize(QtCore.QSize(400, 0))
        self.le_cpf.setObjectName("le_cpf")
        self.horizontalLayout_5.addWidget(self.le_cpf)
        spacerItem3 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.le_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.le_endereco.setMinimumSize(QtCore.QSize(400, 0))
        self.le_endereco.setObjectName("le_endereco")
        self.horizontalLayout_4.addWidget(self.le_endereco)
        spacerItem5 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.le_nascimento = QtWidgets.QLineEdit(self.centralwidget)
        self.le_nascimento.setMinimumSize(QtCore.QSize(400, 0))
        self.le_nascimento.setObjectName("le_nascimento")
        self.horizontalLayout.addWidget(self.le_nascimento)
        spacerItem7 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.btn_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.horizontalLayout_8.addWidget(self.btn_cadastrar)
        self.btn_voltar_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar_cadastro.setObjectName("btn_voltar_cadastro")
        self.horizontalLayout_8.addWidget(self.btn_voltar_cadastro)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        tela_cadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_cadastro)
        QtCore.QMetaObject.connectSlotsByName(tela_cadastro)


    def retranslateUi(self, tela_cadastro):
        _translate = QtCore.QCoreApplication.translate
        tela_cadastro.setWindowTitle(_translate("tela_cadastro", "Cadastro"))
        self.label_4.setText(_translate("tela_cadastro", "Nome"))
        self.label_3.setText(_translate("tela_cadastro", "CPF"))
        self.label_2.setText(_translate("tela_cadastro", "Endereço"))
        self.label.setText(_translate("tela_cadastro", "Nascimento"))
        self.btn_cadastrar.setText(_translate("tela_cadastro", "Cadastrar"))
        self.btn_voltar_cadastro.setText(_translate("tela_cadastro", "<- Voltar"))