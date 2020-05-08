#Controlador de la vista de HopkinsWindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.HopkinsWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.HopkinsPrueba import *
from PruebaModel import *
from ControllerModel import *



class HopkinsController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.hopkinsView = HopkinsWindowWidget(mainWindow)
		self.hopkinsView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.hopkinsPrueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Hopkins
		"""
		view = self.hopkinsView
		total_recall = view.sbSpan.value()
		delayed_recall = view.sbTotal.value()

		valores = [total_recall, delayed_recall]
		self.hopkinsPrueba = HopkinsPrueba(valores)

		#toma anos de escolaridad del paciente
		datos = self.reporteModel.reporte['edad']
		
		self.hopkinsPrueba.calcularPERP(datos)
			
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
		 Método que se regresa el id del menu en la vista de Hopkins
		"""
		return self.hopkinsView.lWVistas


	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.hopkinsView.progressBar


# Pruebas unitarias
#if __name__ == "__main__":
#	import sys
#	app = QtWidgets.QApplication(sys.argv)
#	fluidezWindow = QtWidgets.QWidget()
#	fluidezVerbalController = HopkinsController(fluidezWindow)
#	fluidezWindow.show()
#	sys.exit(app.exec_())
