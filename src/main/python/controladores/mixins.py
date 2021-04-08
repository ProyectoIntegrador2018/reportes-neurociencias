from PyQt5 import QtWidgets, QtCore
from ControllerModel import *

class WindowControllerMixin(QtWidgets.QWidget, ControllerModel):
	#Atributo empleado para realizar el cambio de vista
	switch_window = QtCore.pyqtSignal(object, object, bool)

	def __init__(self, mainWindow, reporteModel=None):
		QtWidgets.QWidget.__init__(self)
		self.view = self.getWidgetClass()(mainWindow)
		self.view.pbStart.clicked.connect(self.getDatos)
		self.view.backButton.clicked.connect(self.returnView)
		self.reporteModel = reporteModel
		self.invalidArgs = list()

	def returnView(self):
		"""
		 Método encargado de notificar los elementos que serán pasados como parámetros a la siguiente vista
		"""
		self.switch_window.emit(self.invalidArgs, self.getWidgetClass(), True)