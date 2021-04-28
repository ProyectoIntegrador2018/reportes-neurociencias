#Controlador de la vista de AbstraccionWindow
from PyQt5 import QtCore
from vistas.AbstraccionWindowWidget import AbstraccionWindowWidget
from pruebas.AbstraccionPrueba import AbstraccionPrueba
from .mixins import WindowControllerMixin

class AbstraccionController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)


	def getWidgetClass(self):
		return AbstraccionWindowWidget

	def getTestClass(self):
		return AbstraccionPrueba

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de TMT
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