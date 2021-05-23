#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.EMDWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.EMDPrueba import *
from PruebaModel import *
from ControllerModel import *


class EMDController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.bpView = EMDWindowWidget(mainWindow)
		self.bpView.pbStart.clicked.connect(self.getDatos)
		self.bpView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.bpPrueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.bpPrueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de TMT
		"""
		view = self.bpView

		me = view.sbTMTA.value()
		mico = view.sbTMTB.value()
		mie = view.sbTMTC.value()
		mia = view.sbTMTD.value()
		micu = view.sbTMTE.value()
		amed = view.sbTMTF.value()
		mid = view.sbTMTG.value()
		valores = (me,mico,mie,mia,micu,amed,mid)
		
		self.bpPrueba = EMDPrueba(valores)

		#datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		#if me == 5:
		#	me = "Hola"
		if me == 0:
			self.addInvalidArg("ME")
		if mico == 0:
			self.addInvalidArg("MICO")
		if mie == 0:
			self.addInvalidArg("MIE")
		if mia == 0:
			self.addInvalidArg("MIA")
		if micu == 0:
			self.addInvalidArg("MICU")
		if amed == 0:
			self.addInvalidArg("Amotivación")
		if mid == 0:
			self.addInvalidArg("MID")

		if len(self.invalidArgs) == 0:
			self.bpPrueba.calcularPERP()

			
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
		
		if len(self.invalidArgs) == 0:
			self.invalidArgs = [arg]
		else:
			tempList = self.invalidArgs
			tempList.append(arg)
			self.invalidArgs = tempList

	def getListMenu(self):
		"""
		 Método que se regresa el id del menu en la vista de TMT
		"""
		return self.bpView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.bpView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.bpView.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
