#Vista default del Mensaje a desplegar.
from PyQt5 import QtCore, QtGui, QtWidgets


class ModalWindow(QtWidgets.QMessageBox):
    def __init__(self, windowTitle="", msgHeader="", msgText=""):
        super(QtWidgets.QMessageBox, self).__init__()
        self.setIcon(QtWidgets.QMessageBox.Critical)
        self.setWindowTitle(windowTitle)
        self.setText(msgHeader)
        self.setInformativeText(msgText)
        