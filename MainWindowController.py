import sys
from PyQt5 import QtWidgets
from MainWindowView import *
from ReporteModel import *
from datetime import datetime

class MainWindowController(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindowController, self).__init__(parent)
		self.MainWindow = QtWidgets.QMainWindow()
		self.mainWindowView = MainWindowView(self.MainWindow)
		
		generoItems = ["Femenino", "Masculino"]
		self.mainWindowView.cbSexo.addItems(generoItems)
		dateTimeObj = datetime.now()
		timestampStr = dateTimeObj.strftime("%d/%b/%Y")
		self.mainWindowView.leFecha.setText(timestampStr)

		self.mainWindowView.pbStart.clicked.connect(self.getDatos)

		self.MainWindow.show()

	def getDatos(self):
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

		reporteModel = ReporteModel(nombreExaminado = nombre, identificador = idVal, fecha = fecha, 
			genero = genero, edad = edad, fechaNacimiento = fechaNacimiento, lateralidad = lateralidad, 
			nombreExaminador = examinador, carrera = carrera, semestre = semestre, educacion = educacion, 
			equipo = equipo)

		reporteModel.printReporte()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowController()
    sys.exit(app.exec_())
