#Controlador de la vista de D2WindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.D2WindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.D2Prueba import *
from PruebaModel import *
from ControllerModel import *


class D2Controller(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.d2View = D2WindowWidget(mainWindow)
		self.d2View.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.d2Prueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de D2
		"""
		view = self.d2View

		TR = view.sbTR.value()
		TA = view.sbTA.value()
		O = view.sbO.value()
		C = view.sbC.value()
		VAR = view.sbVAR.value()

		valores = [TR, TA, O, C, VAR]
		
		self.d2Prueba = D2Prueba(valores)

		#toma la edad del paciente. MUY IMPORTANTE
		datos = self.reporteModel.reporte['edad']
		
		self.d2Prueba.calcularPERP(datos)
			
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
		return self.d2View.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.d2View.progressBar

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    d2Window = QtWidgets.QWidget()
#    d2Controller = D2Controller(d2Window)
#    d2Window.show()
#    sys.exit(app.exec_())