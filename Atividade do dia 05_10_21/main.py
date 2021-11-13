import sys

from Telas.stack_main import Main
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_main = Main()
    sys.exit(app.exec_())
