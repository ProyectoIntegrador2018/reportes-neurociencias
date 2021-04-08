#Controlador de la vista MainWindow
import sys
import re
from PyQt5 import QtWidgets, QtCore
# from FluidezVerbalController import *
from MainWindowWithListWidget import *
from ReporteModel import *
from datetime import datetime
from ControllerModel import *


class MainWindowController(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow):
		QtWidgets.QWidget.__init__(self)
		self.mainWindow = mainWindow
		self.newInfo()

	def newInfo(self):
		self.mainWindowView = MainWindowWithListWidget(self.mainWindow)
		self.missingArguments = list()
		self.reporte = None

		generoItems = ["Femenino", "Masculino"]
		self.mainWindowView.cbSexo.addItems(generoItems)
		
		lateralidadItems = ["Diestro", "Zurdo", "Ambidiestro"]
		self.mainWindowView.cbLateralidad.addItems(lateralidadItems)
		
		self.mainWindowView.deFecha.setDate(QtCore.QDate.currentDate())
		
		self.mainWindowView.pbStart.clicked.connect(self.getDatos)
		self.mainWindowView.backButton.clicked.connect(self.returnView)

	def preventInjections(self, strVal):
		acceptedChars = r'[\w .-]*'
		return re.search(acceptedChars, strVal).group(0)

	def changeView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.missingArguments, self.reporte, False)

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.missingArguments, self.reporte, True)

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
		fechaNacimiento = vista.deFechaNacimiento.date().toString("dd/MMMM/yyyy")
		lateralidad = str(vista.cbLateralidad.currentText())
		fecha = vista.deFecha.date().toString("dd/MMMM/yyyy")
		carrera = vista.leCarrera.text()
		semestre = vista.sbSemestre.value()
		equipo = vista.leEquipo.text()
		deporte = vista.leDeporte.text()

		nombre = self.preventInjections(nombre)
		idVal = self.preventInjections(idVal)
		examinador = self.preventInjections(examinador)
		carrera = self.preventInjections(carrera)
		equipo = self.preventInjections(equipo)
		deporte = self.preventInjections(deporte)

		if(len(nombre) == 0):
			self.addMissingArg("Nombre")			
		if (len(idVal) == 0):
			self.addMissingArg("ID")
		if (len(examinador) == 0):
			self.addMissingArg("Examinador")
		if (edad == 0):
			self.addMissingArg("Edad debe ser mayor a 0")
		if (educacion == 0):
			self.addMissingArg("Educación debe ser mayor a 0")
		if (len(carrera) == 0):
			self.addMissingArg("Carrera")
		if (len(equipo) == 0):
			self.addMissingArg("Equipo")
		if (len(deporte) == 0):
			self.addMissingArg("Deporte")
		
		if len(self.missingArguments) == 0:
			reporteModel = ReporteModel(nombreExaminado = nombre, identificador = idVal, fecha = fecha, 
			genero = genero, edad = edad, fechaNacimiento = fechaNacimiento, lateralidad = lateralidad, 
			nombreExaminador = examinador, carrera = carrera, semestre = semestre, educacion = educacion, 
			equipo = equipo, deporte = deporte)

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

	def getProgressBar(self):
		"""
		 Método que se encarga de regresar el valor de la barra de progreso
		"""
		return self.mainWindowView.progressBar

	def updateButtonText(self, text):
		"""
		 Método que se encarga de actulaizar el texto del botón de la vista
		"""
		self.mainWindowView.pbStart.setText(text)
