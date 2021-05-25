from PyQt5 import QtCore
from vistas.StroopWindowWidget import StroopWindowWidget
from pruebas.StroopPrueba import StroopPrueba
from .mixins import WindowControllerMixin

class StroopController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return StroopWindowWidget

	def getTestClass(self):
		return StroopPrueba

	def setField(self, data):
		view = self.view
		view.sbTR.setValue(data['sbTR'])
		view.sbTA.setValue(data['sbTA'])
		view.sbO.setValue(data['sbO'])

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
		datos = [self.reporteModel.reporte['educacion'],self.reporteModel.reporte['edad']]
		
		self.test.calcularPERP(datos)
			
		self.changeView()