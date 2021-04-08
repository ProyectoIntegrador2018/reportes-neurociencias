#Controlador de la vista de ButtWindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.ButtWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.ButtPrueba import *
from PruebaModel import *
from ControllerModel import *


class ButtController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.buttView = ButtWindowWidget(mainWindow)
		self.buttView.pbStart.clicked.connect(self.getDatos)
		self.buttView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.buttPrueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.buttPrueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Butt
		"""
		view = self.buttView

		CON = view.sbConflicto.value()
		RIV = view.sbRivalidad.value()
		SUF = view.sbSuficiencia.value()
		COOP = view.sbCooperacion.value()
		AGR = view.sbAgresividad.value()

		valores = [CON, RIV, SUF, COOP, AGR]
		
		self.buttPrueba = ButtPrueba(valores)
		
		self.buttPrueba.calcularPERP()
			
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
		 Método que se regresa el id del menu en la vista de Butt
		"""
		return self.buttView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.buttView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		"""
		self.buttView.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    buttWindow = QtWidgets.QWidget()
#    buttController = ButtController(buttWindow)
#    buttWindow.show()
#    sys.exit(app.exec_())