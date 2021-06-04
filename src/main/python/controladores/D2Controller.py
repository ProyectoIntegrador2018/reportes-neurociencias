#Controlador de la vista de D2WindowWidget
from PyQt5 import QtCore
from vistas.D2WindowWidget import D2WindowWidget
from pruebas.D2Prueba import D2Prueba
from .mixins import WindowControllerMixin

class D2Controller(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return D2WindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return D2Prueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbTR.setValue(data['sbTR'])
		view.sbTA.setValue(data['sbTA'])
		view.sbO.setValue(data['sbO'])
		view.sbC.setValue(data['sbC'])
		view.sbVAR.setValue(data['sbVAR'])

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