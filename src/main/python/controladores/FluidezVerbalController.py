#Controlador de la vista de FluidezVerbalWindow
from PyQt5 import QtWidgets, QtCore
from vistas.FluidezVerbalWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.FluidezVerbalPrueba import *
from PruebaModel import *
from ControllerModel import *


class FluidezVerbalController(QtWidgets.QWidget, ControllerModel):
	# Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.fluidezVerbalView = FluidezVerbalWindowWidget(mainWindow)
		self.fluidezVerbalView.pbStart.clicked.connect(self.getDatos)
		self.fluidezVerbalView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.fluidezVerbalPrueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.fluidezVerbalPrueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.fluidezVerbalView
		palabrasConP = view.sbWords.value()
		animalesConP = view.sbAnimals.value()

		valores = (palabrasConP, animalesConP)
		
		self.fluidezVerbalPrueba = FluidezVerbalPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion']]
		
		if palabrasConP == 0:
			self.addInvalidArg("Palabras con P")
		if animalesConP == 0:
			self.addInvalidArg("Animales con P")

		if len(self.invalidArgs) == 0:
			self.fluidezVerbalPrueba.calcularPERP(datos)
			
		self.changeView()

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

	def getListMenu(self):
		"""
		 Método que se regresa el id del menu en la vista de Fluidez Verbal
		"""
		return self.fluidezVerbalView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.fluidezVerbalView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.fluidezVerbalView.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
