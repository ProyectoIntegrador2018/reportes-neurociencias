from PyQt5 import QtWidgets, QtCore
from vistas.MVCWindowWidget import *
from MainWindowController import *
from pruebas.MVCPrueba import *
from PruebaModel import *
from ReporteModel import *

class MVCController(QtWidgets.QWidget):
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.MVCView = MVCWindowWidget(mainWindow)
		self.MVCView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		self.switch_window.emit(self.invalidArgs, self.MVCPrueba)


	def getDatos(self):
		view = self.MVCView
		MVC = view.sbMVC.value()
		MVCT = view.sbMVCT.value()

		valores = (MVC, MVCT)
		
		self.MVCPrueba = MVCPrueba(valores)
		
		#validacion de datos de entrada
		if MVC == 0:
			self.addInvalidArg("MVC")
		if MVCT == 0:
			self.addInvalidArg("MVCT")

		if len(self.invalidArgs) == 0:
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


# Pruebas unitarias
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MVCWindow = QtWidgets.QWidget()
#     MVCController = MVCController(MVCWindow)
#     MVCWindow.show()
#     sys.exit(app.exec_())
