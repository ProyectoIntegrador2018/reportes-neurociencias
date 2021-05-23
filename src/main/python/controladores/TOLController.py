from PyQt5 import QtCore
from vistas.TOLWindowWidget import TOLWindowWidget
from pruebas.TOLPrueba import TOLPrueba
from .mixins import WindowControllerMixin

class TOLController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        return TOLWindowWidget

    def getTestClass(self):
        return TOLPrueba

    def setField(self, data):
        view = self.view
        view.sbTotalCorrectos.setValue(data['sbTotalCorrectos'])
        view.sbMovimientosTotales.setValue(data['sbMovimientosTotales'])
        view.sbTiempoLatencia.setValue(data['sbTiempoLatencia'])
        view.sbTiempoEjecucion.setValue(data['sbTiempoEjecucion'])
        view.sbTiempoResolucion.setValue(data['sbTiempoResolucion'])
        view.sbVT.setValue(data['sbVT'])
        view.sbVR.setValue(data['sbVR'])

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