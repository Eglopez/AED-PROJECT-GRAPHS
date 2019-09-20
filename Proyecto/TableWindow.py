# -*- coding: utf-8 -*-
from PyQt5 import *

class TableWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("TableWindow.ui",self)
        self.parent = parent
        self.setWindowTitle("Tabla")
        self.setFocus()
        self.table.setReadOnly(True)