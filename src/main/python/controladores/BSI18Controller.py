#Controlador de la vista de BSI18Window
from PyQt5 import QtWidgets, QtCore
from vistas.BSI18WindowWidget import *
from pruebas.BSI18Prueba import *
from .mixins import WindowControllerMixin


class BSI18Controller(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vistal
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return BSI18WindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return BSI18Prueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.questions[0].setValue(data['Q1'])
		view.questions[1].setValue(data['Q2'])
		view.questions[2].setValue(data['Q3'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de BSI18
		"""
		view = self.view
		# Inicia los valores y las omisiones en 0 para las 3 dimensiones
		valores = [0, 0, 0]
		omisiones = [0, 0, 0]	
		
		# Establecemos los numeros de las preguntas de las dimensiones
		ids = [[1,4,7,10,13,16], #SOM
				[2,5,8,11,14,17], #DEP
				[3,6,9,12,15,18]] #ANS

		# Cuenta el número de omisiones por dimensión
		# Suma los valores de las respuestas por dimensión
		'''for x, q in enumerate(view.questions):
			for y, i in enumerate(ids):
				if x+1 in i:

					print(x, q.value(), y, i)
					if q.value() == -1:
						omisiones[y] = omisiones[y] + 1
					else:
						valores[y] = valores[y] + int(q.value())

		'''
		valores = [dim.value() for dim in view.questions]

		# Manda los valores obtenidos para procesar la prueba
		self.test = BSI18Prueba(valores)
		
		datos = (self.reporteModel.reporte['genero'], False)#El False es por el cancer, lo voy a poner después
		
		# Verifica el número de omisiones de cada dimensión
		for x, om in enumerate(omisiones):
			if 2 < om:
				self.invalidArgs.append("Maximo 2 omisiones por dimensión")

			elif 0 < om:
				prom = valores[x]/(6.0-om)
				if prom > int(prom)+.5:
					prom = prom + 1
				else:
					prom = int(prom)
				valores[x] = 6 * prom
		
		# Verifica que ya no haya argumentos inválidos
		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()