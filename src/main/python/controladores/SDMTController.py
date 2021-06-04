from PyQt5 import QtCore
from pruebas.SDMTPrueba import SDMTPrueba
from vistas.SDMTWindowWidget import SDMTWindowWidget
from .mixins import WindowControllerMixin

class SDMTController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        """
        Metodo que regresa el objeto Widget del Controlador
        """
        return SDMTWindowWidget

    def getTestClass(self):
        """
        Metodo que regresa el objeto Prueba del Controlador
        """
        return SDMTPrueba
    
    def setField(self, data):
        """
        Metodo que que setea los valores en el Controlador
        """
        view = self.view
        view.sbSDMT.setValue(data['sbSDMT'])

    def getDatos(self):
        """
		Método que toma los datos ingresados en la vista SDMT
		"""
        view = self.view
        sdmtVal = view.sbSDMT.value()

        valores = (sdmtVal)

        self.test = SDMTPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'],self.reporteModel.reporte['edad']]

       
        self.test.calcularPERP(datos)
        
        self.changeView()