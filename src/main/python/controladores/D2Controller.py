#Controlador de la vista de D2WindowWidget
from PyQt5 import QtCore
from vistas.D2WindowWidget import D2WindowWidget
from pruebas.D2Prueba import D2Prueba
from .mixins import WindowControllerMixin

class D2Controller(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return D2WindowWidget

	def getTestClass(self):
		return D2Prueba

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de D2
		"""
		view = self.view

		TR = view.sbTR.value()
		TA = view.sbTA.value()
		O = view.sbO.value()
		C = view.sbC.value()
		VAR = view.sbVAR.value()

		valores = [TR, TA, O, C, VAR]
		
		self.test = D2Prueba(valores)

		#toma la edad del paciente. MUY IMPORTANTE
		datos = self.reporteModel.reporte['edad']
		
		self.test.calcularPERP(datos)
			
		self.changeView()