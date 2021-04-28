#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.BussyPerryWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.BussyPerryPrueba import *
from PruebaModel import *
from ControllerModel import *


class BussyPerryController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.bpView = BussyPerryWindowWidget(mainWindow)
		self.bpView.pbStart.clicked.connect(self.getDatos)
		self.bpView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.bpPrueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.bpPrueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de TMT
		"""
		view = self.bpView

		agFis = view.sbTMTA.value()
		agVer = view.sbTMTB.value()
		ira = view.sbTMTC.value()
		hos = view.sbTMTD.value()

		valores = (agFis, agVer,ira,hos)
		
		self.bpPrueba = BussyPerryPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		
		if agFis == 0:
			self.addInvalidArg("Agresion Fisica")
		if agVer == 0:
			self.addInvalidArg("Agresion Verbal")
		if ira == 0:
			self.addInvalidArg("Ira")
		if hos == 0:
			self.addInvalidArg("Hostilidad")

		if len(self.invalidArgs) == 0:
			self.bpPrueba.calcularPERP(datos)
			
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
		 Método que se regresa el id del menu en la vista de TMT
		"""
		return self.bpView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.bpView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.bpView.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
