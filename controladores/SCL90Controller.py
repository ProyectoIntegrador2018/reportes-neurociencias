#Controlador de la vista de SCL90Window
from PyQt5 import QtWidgets, QtCore
from vistas.SCL90WindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.SCL90Prueba import *
from PruebaModel import *
from ControllerModel import *


class SCL90Controller(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.SCL90View = SCL90WindowWidget(mainWindow)
		self.SCL90View.pbStart.clicked.connect(self.getDatos)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.SCL90Prueba)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.SCL90View
		
		somVal = view.dsbSOM.value()
		obsVal = view.dsbOBS.value()
		intVal = view.dsbINT.value()
		depVal = view.dsbDEP.value()
		ansVal = view.dsbANS.value()
		hosVal = view.dsbHOS.value()
		fobVal = view.dsbFOB.value()
		parVal = view.dsbPAR.value()
		psiVal = view.dsbPSI.value()
		gsiVal = view.dsbGSI.value()
		pstVal = view.dsbPST.value()
		psdiVal = view.dsbPSDI.value()
		
		valores = (somVal, obsVal, intVal, depVal, ansVal, hosVal, 
			fobVal, parVal, psiVal, gsiVal, pstVal, psdiVal)

		self.SCL90Prueba = SCL90Prueba(valores)
		
		datos = self.reporteModel.reporte['genero']
		
		if somVal < 0.00 or somVal > 4.00:
			self.addInvalidArg("SOM")
		if obsVal < 0.00 or obsVal > 4.00:
			self.addInvalidArg("OBS")
		if intVal < 0.00 or intVal > 4.00:
			self.addInvalidArg("INT")
		if depVal < 0.00 or depVal > 4.00:
			self.addInvalidArg("DEP")
		if ansVal < 0.00 or ansVal > 4.00:
			self.addInvalidArg("ANS")
		if hosVal < 0.00 or hosVal > 4.00:
			self.addInvalidArg("HOS")
		if fobVal < 0.00 or fobVal > 3.95:
			self.addInvalidArg("FOB")
		if parVal < 0.00 or parVal > 4.00:
			self.addInvalidArg("PAR")
		if psiVal < 0.00 or psiVal > 3.89:
			self.addInvalidArg("PSI")
		if gsiVal < 0.08 or gsiVal > 3.86:
			self.addInvalidArg("GSI")
		if pstVal < 5 or pstVal > 90.0:
			self.addInvalidArg("PST")
		if psdiVal < 1.03 or psdiVal > 4.00:
			self.addInvalidArg("PSDI")

		if len(self.invalidArgs) == 0:
			self.SCL90Prueba.calcularPERP(datos)
			
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
		 Método que se regresa el id del menu en la vista de Fluidez Verbal
		"""
		return self.SCL90View.lWVistas

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.SCL90View.progressBar


# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
