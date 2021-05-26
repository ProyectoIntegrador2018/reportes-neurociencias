from PyQt5 import QtCore
from vistas.LNSWindowWidget import LNSWindowWidget
from pruebas.LNSPrueba import LNSPrueba
from .mixins import WindowControllerMixin


class LNSController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return LNSWindowWidget

	def getTestClass(self):
		return LNSPrueba

	def setField(self, data):
		view = self.view
		view.sbSpan.setValue(data['sbSpan'])
		view.sbTotal.setValue(data['sbTotal'])
		
	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de LNS
		"""
		view = self.view
		span = view.sbSpan.value()
		total = view.sbTotal.value()

		valores = (span, total)
		
		self.test = LNSPrueba(valores)

		#toma anos de escolaridad del paciente
		datos = (self.reporteModel.reporte['educacion'],self.reporteModel.reporte['edad'])
		
		self.test.calcularPERP(datos)
			
		self.changeView()