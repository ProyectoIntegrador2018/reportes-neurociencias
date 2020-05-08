#Controlador de la barra de Progreso
from PyQt5 import QtCore, QtWidgets, QtGui

class ProgressBarController(QtWidgets.QWidget):
	def __init__(self, numDePruebas):
		QtWidgets.QWidget.__init__(self)
		self.pruebasRealizadas = 0
		self.numDePruebas = numDePruebas
	
	def	setProgressBar(self, progressBar):
		progressBar.setMaximum(self.numDePruebas)
		progressBar.setValue(self.pruebasRealizadas)

	def updateProgress(self, numPrueba):
		self.pruebasRealizadas = numPrueba