#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.TMTWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.TMTPrueba import *
from PruebaModel import *
from ControllerModel import *
from .mixins import WindowControllerMixin

class TMTController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return TMTWindowWidget

	def getDatos(self):
		"""
		Método que toma los datos ingresados en la vista de TMT
		"""
		view = self.view
		tmtA = view.sbTMTA.value()
		tmtB = view.sbTMTB.value()

		valores = (tmtA, tmtB)
		
		self.test = TMTPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		
		if tmtA == 0:
			self.addInvalidArg("TMT A")
		if tmtB == 0:
			self.addInvalidArg("TMT B")

		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()