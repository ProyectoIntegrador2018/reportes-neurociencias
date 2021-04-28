#Controlador de la vista de BSI18Window
from PyQt5 import QtWidgets, QtCore
from vistas.BSI18WindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.BSI18Prueba import *
from PruebaModel import *
from ControllerModel import *


class BSI18Controller(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.BSI18View = BSI18WindowWidget(mainWindow)
		self.BSI18View.pbStart.clicked.connect(self.getDatos)
		self.BSI18View.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.BSI18Prueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.BSI18Prueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.BSI18View
		# Inicia los valores y las omisiones en 0 para las 3 dimensiones
		valores = [0, 0, 0]
		omisiones = [0, 0, 0]	
		
		# Establecemos los numeros de las preguntas de las dimensiones
		ids = [[1,4,7,10,13,16], #SOM
				[2,5,8,11,14,17], #DEP
				[3,6,9,12,15,18]] #ANS

		# Cuenta el número de omisiones por dimensión
		# Suma los valores de las respuestas por dimensión
		for x, q in enumerate(view.questions):
			for y, i in enumerate(ids):
				if x+1 in i:
					print(x, q.value(), y, i)
					if q.value() == -1:
						omisiones[y] = omisiones[y] + 1
					else:
						valores[y] = valores[y] + int(q.value())

		# Manda los valores obtenidos para procesar la prueba
		self.BSI18Prueba = BSI18Prueba(valores)
		
		datos = (self.reporteModel.reporte['genero'], False)#El False es por el cancer, lo voy a poner después
		
		# Verifica el número de omisiones de cada dimensión
		for x, om in enumerate(omisiones):
			if 2 < om:
				self.invalidArgs.append("Maximo 2 omisiones por dimensión")
		
		# Verifica que ya no haya argumentos inválidos
		if len(self.invalidArgs) == 0:
			self.BSI18Prueba.calcularPERP(datos)
			
		self.changeView()

	def emptyInvalidArgs(self):
		"""
		 Método que se encarga de vacíar la lista de elementos inválidos en la vista
		"""
		self.invalidArgs = list()

	def addInvalidArg(self, arg):
		"""
		 Método que se encarga de añadir a la lista de elementos inválidos, aquel parámetro especificado
		 Args:
		  arg: String a añadir a la lista de elementos inválidos
		"""
		self.invalidArgs.append(arg)
		'''
		if len(self.invalidArgs) == 0:
			self.invalidArgs = [arg]
		else:
			tempList = self.invalidArgs
			tempList.append(arg)
			self.invalidArgs = tempList
		'''

	def getListMenu(self):
		"""
		 Método que se regresa el id del menu en la vista de Fluidez Verbal
		"""
		return self.BSI18View.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.BSI18View.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actuañizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.BSI18View.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
