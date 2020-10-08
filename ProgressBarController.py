# Controlador de la barra de Progreso
from PyQt5 import QtCore, QtWidgets, QtGui


class ProgressBarController(QtWidgets.QWidget):
    def __init__(self, numDePruebas):
        QtWidgets.QWidget.__init__(self)
        self.pruebasRealizadas = 0
        self.numDePruebas = numDePruebas
        print(self.numDePruebas)

    def setProgressBar(self, progressBar):
        """
         Método que se encarga de conectar la barra de progreso con la aqulla presente en la vista
         Args:
          progressBar: Objeto de tipo QtProgressBar que está presente en la vista de cada prueba
        """
        progressBar.setMaximum(self.numDePruebas)
        progressBar.setValue(self.pruebasRealizadas)

    def updateProgress(self, numPrueba):
        """
         Método que se encarga de actualizar el atributo de pruebasRealizadas
         Args:
          numPrueba: Valor entero que contiene la cantidad de pruebas ya registradas
        """
        self.pruebasRealizadas = numPrueba
