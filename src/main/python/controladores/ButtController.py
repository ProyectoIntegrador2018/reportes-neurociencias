#Controlador de la vista de ButtWindowWidget
from PyQt5 import QtCore
from vistas.ButtWindowWidget import ButtWindowWidget
from pruebas.ButtPrueba import ButtPrueba
from .mixins import WindowControllerMixin


class ButtController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return ButtWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return ButtPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbConflicto.setValue(data['sbConflicto'])
		view.sbRivalidad.setValue(data['sbRivalidad'])
		view.sbSuficiencia.setValue(data['sbSuficiencia'])
		view.sbCooperacion.setValue(data['sbCooperacion'])
		view.sbAgresividad.setValue(data['sbAgresividad'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Butt
		"""
		view = self.view

		CON = view.sbConflicto.value()
		RIV = view.sbRivalidad.value()
		SUF = view.sbSuficiencia.value()
		COOP = view.sbCooperacion.value()
		AGR = view.sbAgresividad.value()

		valores = [CON, RIV, SUF, COOP, AGR]
		
		self.test = ButtPrueba(valores)
		
		self.test.calcularPERP()
			
		self.changeView()