#Controlador de la vista de LNSWindowWidget
from PyQt5 import QtWidgets, QtCore
from vistas.StroopWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.StroopPrueba import *
from PruebaModel import *
from ControllerModel import *
from .mixins import WindowControllerMixin

class StroopController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return StroopWindowWidget

	def getDatos(self):
		"""
		Método que toma los datos ingresados en la vista de LNS
		"""
		view = self.view
		P = view.sbTR.value()
		C = view.sbTA.value()
		PC = view.sbO.value()

		valores = (P, C, PC)
		
		self.test = StroopPrueba(valores)

		#toma anos de escolaridad del paciente
		datos = self.reporteModel.reporte['educacion']
		
		self.test.calcularPERP(datos)
			
		self.changeView()