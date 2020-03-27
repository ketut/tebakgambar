#!/usr/bin/python3
#main in feature bracnh
import sys

from tebakgambar_ui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()

    a.exec_()
