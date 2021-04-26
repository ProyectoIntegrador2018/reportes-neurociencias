# Contolador de la vista de Torre de Londres
from PyQt5 import QtWidgets, QtCore
from vistas.TOLWindowWidget import *
from MainWindowController import *
from ReporteModel import *
from pruebas.TOLPrueba import *
from PruebaModel import *
from ControllerModel import *
from .mixins import WindowControllerMixin

class TOLController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        return TOLWindowWidget

    def getDatos(self):
        """
		Método que toma los datos ingresados en la vista de Fluidez Verbal
		"""
        view = self.view

        totalCorrectos = view.sbTotalCorrectos.value()
        movimientosTotales = view.sbMovimientosTotales.value()
        tiempoLatencia = view.sbTiempoLatencia.value()
        tiempoEjecucion = view.sbTiempoEjecucion.value()
        tiempoResolucion = view.sbTiempoResolucion.value()
        vt = view.sbVT.value()
        vr = view.sbVR.value()

        valores = (totalCorrectos, movimientosTotales,
                tiempoLatencia, tiempoEjecucion, tiempoResolucion,
                vt, vr)
        
        self.test = TOLPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]

        self.test.calcularPERP(datos)
        self.changeView()