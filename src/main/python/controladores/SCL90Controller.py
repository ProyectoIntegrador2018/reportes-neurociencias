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
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.SCL90View = SCL90WindowWidget(mainWindow)
		self.SCL90View.pbStart.clicked.connect(self.getDatos)
		self.SCL90View.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()
	
	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.SCL90Prueba, True)
	
	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.SCL90Prueba, False)


	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		view = self.SCL90View
		
		somVal = float(f"{view.dsbSOM.value():.2f}")
		obsVal = float(f"{view.dsbOBS.value():.2f}")
		intVal = float(f"{view.dsbINT.value():.2f}")
		depVal = float(f"{view.dsbDEP.value():.2f}")
		ansVal = float(f"{view.dsbANS.value():.2f}")
		hosVal = float(f"{view.dsbHOS.value():.2f}")
		fobVal = float(f"{view.dsbFOB.value():.2f}")
		parVal = float(f"{view.dsbPAR.value():.2f}")
		psiVal = float(f"{view.dsbPSI.value():.2f}")
		gsiVal = float(f"{view.dsbGSI.value():.2f}")
		pstVal = float(f"{view.dsbPST.value():.2f}")
		psdiVal = float(f"{view.dsbPSDI.value():.2f}")
		
		valores = (somVal, obsVal, intVal, depVal, ansVal, hosVal, 
			fobVal, parVal, psiVal, gsiVal, pstVal, psdiVal)

		self.SCL90Prueba = SCL90Prueba(valores)
		
		datos = self.reporteModel.reporte['genero']
		if datos == 'Femenino':
			if somVal < 0.00:
				self.addInvalidArg("SOM(Min: 0.00, Max: 4.00")
			if obsVal < 0.00:
				self.addInvalidArg("OBS(Min: 0.00, Max: 3.96)")
			if intVal < 0.00:
				self.addInvalidArg("INT(Min: 0.00, Max: 3.96)")
			if depVal < 0.08:
				self.addInvalidArg("DEP(Min: 0.08, Max: 4.00)")
			if ansVal < 0.00:
				self.addInvalidArg("ANS(Min: 0.00, Max: 4.00)")
			if hosVal < 0.00:
				self.addInvalidArg("HOS(Min: 0.00, Max: 4.00)")
			if fobVal < 0.00:
				self.addInvalidArg("FOB(Min: 0.00, Max: 3.95)")
			if parVal < 0.00:
				self.addInvalidArg("PAR(Min: 0.00, Max: 4.00)")
			if psiVal < 0.00:
				self.addInvalidArg("PSI(Min: 0.00, Max: 3.96)")
			if gsiVal < 0.08:
				self.addInvalidArg("GSI(Min: 0.08, Max: 3.86)")
			if pstVal < 5.00:
				self.addInvalidArg("PST(Min: 5.00, Max: 90.00)")
			if psdiVal < 1.10:
				self.addInvalidArg("PSDI(Min: 1.10, Max: 3.92)")
		else:
			if somVal < 0.00:
				self.addInvalidArg("SOM(Min: 0.00, Max: 3.58")
			if obsVal < 0.00:
				self.addInvalidArg("OBS(Min: 0.00, Max: 4.00)")
			if intVal < 0.00:
				self.addInvalidArg("INT(Min: 0.00, Max: 3.56)")
			if depVal < 0.00:
				self.addInvalidArg("DEP(Min: 0.08, Max: 3.54)")
			if ansVal < 0.00:
				self.addInvalidArg("ANS(Min: 0.00, Max: 4.00)")
			if hosVal < 0.00:
				self.addInvalidArg("HOS(Min: 0.00, Max: 3.83)")
			if fobVal < 0.00:
				self.addInvalidArg("FOB(Min: 0.00, Max: 3.86)")
			if parVal < 0.00:
				self.addInvalidArg("PAR(Min: 0.00, Max: 3.67)")
			if psiVal < 0.00:
				self.addInvalidArg("PSI(Min: 0.00, Max: 3.60)")
			if gsiVal < 0.08:
				self.addInvalidArg("GSI(Min: 0.08, Max: 3.48)")
			if pstVal < 5.00:
				self.addInvalidArg("PST(Min: 5.00, Max: 89.00)")
			if psdiVal < 1.03:
				self.addInvalidArg("PSDI(Min: 1.10, Max: 4.00)")

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

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		 Args:
		  text: Objeto de tipo str que contiene el nuevo valor a asignar al botón presente en las pruebas
		"""
		self.SCL90View.pbStart.setText(text)

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = FluidezVerbalController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
