from PyQt5 import QtCore
from vistas.HopkinsWindowWidget import HopkinsWindowWidget
from pruebas.HopkinsPrueba import HopkinsPrueba
from .mixins import WindowControllerMixin

class HopkinsController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return HopkinsWindowWidget

	def getTestClass(self):
		return HopkinsPrueba

	def setField(self, data):
		view = self.view
		view.sbSpan.setValue(data['sbSpan'])
		view.sbTotal.setValue(data['sbTotal'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Hopkins
		"""
		view = self.view
		total_recall = view.sbSpan.value()
		delayed_recall = view.sbTotal.value()

		valores = [total_recall, delayed_recall]
		self.test = HopkinsPrueba(valores)

		#toma anos de escolaridad del paciente
		datos = self.reporteModel.reporte['edad']
		
		self.test.calcularPERP(datos)
			
		self.changeView()
