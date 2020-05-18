#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.TMTWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.TMTPrueba import *
from PruebaModel import *
from ControllerModel import *


class TMTController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.tmtView = TMTWindowWidget(mainWindow)
		self.tmtView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.tmtPrueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de TMT
		"""
		view = self.tmtView
		tmtA = view.sbTMTA.value()
		tmtB = view.sbTMTB.value()

		valores = (tmtA, tmtB)
		
		self.tmtPrueba = TMTPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		
		if tmtA == 0:
			self.addInvalidArg("TMT A")
		if tmtB == 0:
			self.addInvalidArg("TMT B")

		if len(self.invalidArgs) == 0:
			self.tmtPrueba.calcularPERP(datos)
			
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
		return self.tmtView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.tmtView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.tmtView.pbStart.setText(text)


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
