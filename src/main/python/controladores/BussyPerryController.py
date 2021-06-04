#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.BussyPerryWindowWidget import *
from pruebas.BussyPerryPrueba import *
from .mixins import WindowControllerMixin


class BussyPerryController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return BussyPerryWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return BussyPerryPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbTMTA.setValue(data['sbTMTA'])
		view.sbTMTB.setValue(data['sbTMTB'])
		view.sbTMTC.setValue(data['sbTMTC'])
		view.sbTMTD.setValue(data['sbTMTD'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de BussyPerry
		"""
		view = self.view

		agFis = view.sbTMTA.value()
		agVer = view.sbTMTB.value()
		ira = view.sbTMTC.value()
		hos = view.sbTMTD.value()

		valores = (agFis, agVer, ira, hos)
		
		self.test = BussyPerryPrueba(valores)
		
		datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]
		
		if agFis == 0:
			self.addInvalidArg("Agresion Fisica")
		if agVer == 0:
			self.addInvalidArg("Agresion Verbal")
		if ira == 0:
			self.addInvalidArg("Ira")
		if hos == 0:
			self.addInvalidArg("Hostilidad")

		if len(self.invalidArgs) == 0:
			self.test.calcularPERP(datos)
			
		self.changeView()

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
