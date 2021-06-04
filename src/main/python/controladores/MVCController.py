from PyQt5 import QtCore
from vistas.MVCWindowWidget import MVCWindowWidget
from pruebas.MVCPrueba import MVCPrueba
from .mixins import WindowControllerMixin

class MVCController(WindowControllerMixin):
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return MVCWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return MVCPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbMVC.setValue(data['sbMVC'])
		view.sbMVCT.setValue(data['sbMVCT'])

	def getDatos(self):
		"""
        Metodo para tomar los datos ingresados en la prueba de MVCC
        """
		view = self.view
		MVC = view.sbMVC.value()
		MVCT = view.sbMVCT.value()

		valores = (MVC, MVCT)
		
		self.test = MVCPrueba(valores)
		
		self.test.calcularPERP()
			
		self.changeView()