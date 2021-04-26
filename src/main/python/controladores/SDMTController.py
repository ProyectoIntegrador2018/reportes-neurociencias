from PyQt5 import QtWidgets, QtCore
from pruebas.SDMTPrueba import *
from vistas.SDMTWindowWidget import *
from ReporteModel import *
from ControllerModel import *
from .mixins import WindowControllerMixin

class SDMTController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        return SDMTWindowWidget

    def getDatos(self):
        """
		Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
        view = self.view
        sdmtVal = view.sbSDMT.value()

        valores = (sdmtVal)

        self.test = SDMTPrueba(valores)

        datos = [self.reporteModel.reporte['educacion']]

       
        self.test.calcularPERP(datos)
        
        self.changeView()