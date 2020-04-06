#Controlador de la vista de FluidezVerbalWindow
from PyQt5 import QtWidgets, QtCore
from FluidezVerbalWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from FluidezVerbalPrueba import *
from PruebaModel import *


class FluidezVerbalController(QtWidgets.QWidget):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal()

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.fluidezVerbalView = FluidezVerbalWindowWidget(mainWindow)
		self.fluidezVerbalView.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
	
	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.fluidezVerbalView
		palabrasConP = view.sbWords.value()
		animalesConP = view.sbAnimals.value()

		valores = (palabrasConP, animalesConP)
		
		fluidezVerbalPrueba = FluidezVerbalPrueba(valores)
		
		####Se obtienen los datos de escolaridad del reporte
		#reporteModel = ReporteModel.getReporte()
		#datos = [reporteModel.reporte['educacion']]
		datos = [8]

		fluidezVerbalPrueba.calcularPERP(datos)

		#reporteModel.addPrueba(fluidezVerbalPrueba)
		#reporteModel.printReporte()
		fluidezVerbalPrueba.printInfo()


"""
# Pruebas unitarias
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fluidezWindow = QtWidgets.QWidget()
    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
    fluidezWindow.show()
    sys.exit(app.exec_())
"""