from PyQt5 import QtCore
from vistas.FluidezVerbalWindowWidget import FluidezVerbalWindowWidget
from pruebas.FluidezVerbalPrueba import FluidezVerbalPrueba
from .mixins import WindowControllerMixin


class FluidezVerbalController(WindowControllerMixin):
	# Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		return FluidezVerbalWindowWidget

	def getTestClass(self):
		return FluidezVerbalPrueba

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.view
		palabrasConP = view.sbWords.value()
		animalesConP = view.sbAnimals.value()

		valores = (palabrasConP, animalesConP)
		
		self.test = FluidezVerbalPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion']]
		
		if palabrasConP == 0:
			self.addInvalidArg("Palabras con P")
		if animalesConP == 0:
			self.addInvalidArg("Animales con P")

		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()