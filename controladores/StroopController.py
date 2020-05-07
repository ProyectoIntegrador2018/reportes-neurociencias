#Controlador de la vista de StroopWindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.StroopWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.StroopPrueba import *
from PruebaModel import *
from ControllerModel import *


class StroopController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.stroopView = StroopWindowWidget(mainWindow)
		self.stroopView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.stroopPrueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de D2
		"""
		view = self.stroopView
		P = view.P.value()
		C = view.C.value()
		PC = view.PC.value()

		valores = [P, C, PC]
		
		self.stroopPrueba = StroopPrueba(valores)

		#toma la edad del paciente. MUY IMPORTANTE
		datos = self.reporteModel.reporte['edad']
		
		self.stroopPrueba.calcularPERP(datos)
			
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
		 Método que se regresa el id del menu en la vista de D2
		"""
		return self.stroopView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.stroopView.progressBar


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    d2Window = QtWidgets.QWidget()
#    d2Controller = D2Controller(d2Window)
#    d2Window.show()
#    sys.exit(app.exec_())