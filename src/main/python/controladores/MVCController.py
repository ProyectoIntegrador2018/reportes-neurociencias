from PyQt5 import QtCore
from vistas.MVCWindowWidget import MVCWindowWidget
from pruebas.MVCPrueba import MVCPrueba
from .mixins import WindowControllerMixin

class MVCController(WindowControllerMixin):
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return MVCWindowWidget

	def getDatos(self):
		"""
        Metodo para tomar los datos ingresados en la prueba de memoria visoespacia
        """
		view = self.view
		MVC = view.sbMVC.value()
		MVCT = view.sbMVCT.value()

		valores = (MVC, MVCT)
		
		self.test = MVCPrueba(valores)
		
		self.test.calcularPERP()
			
		self.changeView()