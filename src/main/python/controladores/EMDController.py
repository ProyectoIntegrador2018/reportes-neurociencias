#Controlador de la vista de TMTWindow
from PyQt5 import QtWidgets, QtCore
from vistas.EMDWindowWidget import *
from pruebas.EMDPrueba import *
from .mixins import WindowControllerMixin


class EMDController(WindowControllerMixin):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def getWidgetClass(self):
		"""
        Metodo que regresa el objeto Widget del Controlador
        """
		return EMDWindowWidget

	def getTestClass(self):
		"""
        Metodo que regresa el objeto Prueba del Controlador
        """
		return EMDPrueba

	def setField(self, data):
		"""
        Metodo que que setea los valores en el Controlador
        """
		view = self.view
		view.sbTMTA.setValue(data['sbTMTA'])
		view.sbTMTB.setValue(data['sbTMTB'])
		view.sbTMTC.setValue(data['sbTMTC'])
		view.sbTMTD.setValue(data['sbTMTD'])
		view.sbTMTF.setValue(data['sbTMTF'])
		view.sbTMTG.setValue(data['sbTMTG'])

	def getDatos(self):
		"""
		 Método que toma los datos ingresados en la vista de EMD
		"""
		view = self.view

		me = view.sbTMTA.value()
		mico = view.sbTMTB.value()
		mie = view.sbTMTC.value()
		mia = view.sbTMTD.value()
		micu = view.sbTMTE.value()
		amed = view.sbTMTF.value()
		mid = view.sbTMTG.value()
		valores = (me,mico,mie,mia,micu,amed,mid)
		
		self.test = EMDPrueba(valores)

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
			self.test.calcularPERP()

			
		self.changeView()

# Pruebas unitarias
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    fluidezWindow = QtWidgets.QWidget()
#    fluidezVerbalController = TMTController(fluidezWindow)
#    fluidezWindow.show()
#    sys.exit(app.exec_())
