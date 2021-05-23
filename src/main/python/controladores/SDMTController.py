from PyQt5 import QtCore
from pruebas.SDMTPrueba import SDMTPrueba
from vistas.SDMTWindowWidget import SDMTWindowWidget
from .mixins import WindowControllerMixin

class SDMTController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        return SDMTWindowWidget

    def getTestClass(self):
        return SDMTPrueba
    
    def setField(self, data):
        view = self.view
        view.sbSDMT.setValue(data['sbSDMT'])

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