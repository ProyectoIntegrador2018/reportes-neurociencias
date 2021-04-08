#Controlador de la vista de LNSWindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.StroopWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.StroopPrueba import *
from PruebaModel import *
from ControllerModel import *


class StroopController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.stroopView = StroopWindowWidget(mainWindow)
		self.stroopView.pbStart.clicked.connect(self.getDatos)
		self.stroopView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.stroopPrueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.stroopPrueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de LNS
		"""
		view = self.stroopView
		P = view.sbTR.value()
		C = view.sbTA.value()
		PC = view.sbO.value()

		valores = (P, C, PC)
		
		self.stroopPrueba = StroopPrueba(valores)

		#toma anos de escolaridad del paciente
		datos = self.reporteModel.reporte['educacion']
		
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
		 Método que se regresa el id del menu en la vista de LNS
		"""
		return self.stroopView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.stroopView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		"""
		self.stroopView.pbStart.setText(text)


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = LNSController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
