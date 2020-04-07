#Controlador de la vista MainWindow
import sys
from PyQt5 import QtWidgets, QtCore
from FluidezVerbalController import *
from MainWindowWithListWidget import *
from ReporteModel import *
from datetime import datetime


class MainWindowController(QtWidgets.QWidget):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object)

	def __init__(self, mainWindow):
		QtWidgets.QWidget.__init__(self)
		self.mainWindowView = MainWindowWithListWidget(mainWindow)
		self.missingArguments = list()
		self.reporte = None

		generoItems = ["Femenino", "Masculino"]
		self.mainWindowView.cbSexo.addItems(generoItems)
		dateTimeObj = datetime.now()
		timestampStr = dateTimeObj.strftime("%d/%b/%Y")
		self.mainWindowView.leFecha.setText(timestampStr)

		self.mainWindowView.pbStart.clicked.connect(self.getDatos)

	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.missingArguments, self.reporte)

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
		vista = self.mainWindowView
		nombre = vista.leName.text()
		idVal = vista.leId.text()
		examinador = vista.leExaminer.text()
		edad = vista.sbAge.value()
		educacion = vista.sbEscolaridad.value()
		genero = str(vista.cbSexo.currentText())
		fechaNacimiento = vista.leFechaNacimiento.text()
		lateralidad = vista.leLateralidad.text()
		fecha = vista.leFecha.text()
		carrera = vista.leCarrera.text()
		semestre = vista.sbSemestre.value()
		equipo = vista.leEquipo.text()

		if(len(nombre) == 0):
			self.addMissingArg("Nombre")			
		if (len(idVal) == 0):
			self.addMissingArg("ID")
		if (len(examinador) == 0):
			self.addMissingArg("Examinador")
		if (edad == 0):
			self.addMissingArg("Edad debe ser mayor a 0")
		if (len(fechaNacimiento) == 0):
			self.addMissingArg("Fecha de Nacimiento")
		if (len(lateralidad) == 0):
			self.addMissingArg("Lateralidad")
		if (len(fecha) == 0):
			self.addMissingArg("Fecha")
		if (len(carrera) == 0):
			self.addMissingArg("Carrera")
		if (len(equipo) == 0):
			self.addMissingArg("Equipo")
		
		if len(self.missingArguments) == 0:
			reporteModel = ReporteModel(nombreExaminado = nombre, identificador = idVal, fecha = fecha, 
			genero = genero, edad = edad, fechaNacimiento = fechaNacimiento, lateralidad = lateralidad, 
			nombreExaminador = examinador, carrera = carrera, semestre = semestre, educacion = educacion, 
			equipo = equipo)

			self.reporte = reporteModel

		self.changeView()
		
	def emptyMissingArgs(self):
		"""
		 Método que se encarga de vacíar la lista de elementos faltantes en la vista
		"""
		self.missingArguments = list()

	def addMissingArg(self, missingElem):
		"""
		 Método que se encarga de añadir a la lista de missingArguments el elemeno especificado.
		 Args:
		  missingElem: String con el nombre de la variable faltante. 
		"""
		if len(self.missingArguments) == 0:
			self.missingArguments = [missingElem]
		else:
			tempList = self.missingArguments
			tempList.append(missingElem)
			self.missingArguments = tempList

	def getListMenu(self):
		"""
		 Método que se encarga de regresar el valor del menú en la vista
		"""
		return self.mainWindowView.lWVistas


