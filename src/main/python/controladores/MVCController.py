from PyQt5 import QtWidgets, QtCore
from vistas.MVCWindowWidget import *
from MainWindowController import *
from pruebas.MVCPrueba import *
from PruebaModel import *
from ReporteModel import *

class MVCController(QtWidgets.QWidget):
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.MVCView = MVCWindowWidget(mainWindow)
		self.MVCView.pbStart.clicked.connect(self.getDatos)
		self.MVCView.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.MVCPrueba, True)
	
	def changeView(self):
		self.switch_window.emit(self.invalidArgs, self.MVCPrueba, False)


	def getDatos(self):
		view = self.MVCView
		MVC = view.sbMVC.value()
		MVCT = view.sbMVCT.value()

		valores = (MVC, MVCT)
		
		self.MVCPrueba = MVCPrueba(valores)
		
		self.MVCPrueba.calcularPERP()
			
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
		 Método que se regresa el id del menu en la vista de Material Verbal Complejo
		"""
		return self.MVCView.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.MVCView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		"""
		self.MVCView.pbStart.setText(text)


# Pruebas unitarias
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MVCWindow = QtWidgets.QWidget()
#     MVCController = MVCController(MVCWindow)
#     MVCWindow.show()
#     sys.exit(app.exec_())
