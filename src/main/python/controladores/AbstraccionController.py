#Controlador de la vista de AbstraccionWindow
from PyQt5 import QtCore
from vistas.AbstraccionWindowWidget import AbstraccionWindowWidget
from pruebas.AbstraccionPrueba import AbstraccionPrueba
from .mixins import WindowControllerMixin

class AbstraccionController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)


	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return AbstraccionWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return AbstraccionPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbAbstraccion.setValue(data['sbAbstraccion'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Abstraccion
		"""
		view = self.view
		valSemAbs = view.sbAbstraccion.value()

		valores = (valSemAbs)
		
		self.test = AbstraccionPrueba(valores)
		
		datos = [self.reporteModel.reporte['edad']]
		
		if (valSemAbs < 0 or valSemAbs > 12):
			self.addInvalidArg("TMT A")

		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()