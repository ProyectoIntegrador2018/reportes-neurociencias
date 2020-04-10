#Controlador de la vista de FluidezVerbalWindow
from PyQt5 import QtWidgets, QtCore
from FluidezVerbalWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from FluidezVerbalPrueba import *
from PruebaModel import *


class FluidezVerbalController(QtWidgets.QWidget):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.fluidezVerbalView = FluidezVerbalWindowWidget(mainWindow)
		self.fluidezVerbalView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		print("Ando en changeView de FluidezVerbal")
		self.switch_window.emit(self.invalidArgs,self.fluidezVerbalPrueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.fluidezVerbalView
		palabrasConP = view.sbWords.value()
		animalesConP = view.sbAnimals.value()

		valores = (palabrasConP, animalesConP)
		
		self.fluidezVerbalPrueba = FluidezVerbalPrueba(valores)
		
		####Se obtienen los datos de escolaridad del reporte
		#reporteModel = ReporteModel.getReporte()
		#datos = [reporteModel.reporte['educacion']]
		datos = [21]

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

"""
# Pruebas unitarias
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fluidezWindow = QtWidgets.QWidget()
    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
    fluidezWindow.show()
    sys.exit(app.exec_())
"""