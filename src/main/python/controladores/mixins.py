from PyQt5 import QtWidgets, QtCore
from ControllerModel import *

class WindowControllerMixin(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.view = self.getWidgetClass()(mainWindow)
		self.view.pbStart.clicked.connect(self.getDatos)
		self.view.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def emptyInvalidArgs(self):
		"""
		Método que se encarga de vacíar la lista de elementos inválidos en la vista
		"""
		self.invalidArgs = list()

	def addInvalidArg(self, arg):
		"""
		Método que se encarga de añadir a la lista de elementos inválidos, aquel parámetro especificado
		Args:
			arg: String a añadir a la lista de elementos inválidos
		"""
		
		if len(self.invalidArgs) == 0:
			self.invalidArgs = [arg]
		else:
			tempList = self.invalidArgs
			tempList.append(arg)
			self.invalidArgs = tempList

	def getProgressBar(self):
		"""
		Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.view.progressBar

	def updateButtonText(self, text):
		"""
		Método que se encarga de actulaizar el texto del botón de la vista
		Args:
			text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.view.pbStart.setText(text)
	
	def getListMenu(self):
		"""
		Método que se regresa el id del menu en la vista de Fluidez Verbal
		"""
		return self.view.lWVistas

	def returnView(self):
		"""
		Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.test, True)
	
	def changeView(self):
		"""
		Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.test, False)