from PyQt5 import QtCore
from vistas.FluidezVerbalWindowWidget import FluidezVerbalWindowWidget
from pruebas.FluidezVerbalPrueba import FluidezVerbalPrueba
from .mixins import WindowControllerMixin


class FluidezVerbalController(WindowControllerMixin):
	# Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return FluidezVerbalWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return FluidezVerbalPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbWords.setValue(data['sbWords'])
		view.sbAnimals.setValue(data['sbAnimals'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.view
		palabrasConP = view.sbWords.value()
		animalesConP = view.sbAnimals.value()

		valores = (palabrasConP, animalesConP)
		
		self.test = FluidezVerbalPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		
		if palabrasConP == 0:
			self.addInvalidArg("Palabras con P")
		if animalesConP == 0:
			self.addInvalidArg("Animales con P")

		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()