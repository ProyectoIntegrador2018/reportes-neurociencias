from PyQt5 import QtCore
from vistas.MemoriaVisoespaciaWidget import MemoriaVisoespaciaWidget
from pruebas.MemoriaVisoespaciaPrueba import MemoriaVisoespaciaPrueba
from .mixins import WindowControllerMixin

class MemoriaVisoespaciaController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        """
        Metodo que regresa el objeto Widget del Controlador
        """
        return MemoriaVisoespaciaWidget

    def getTestClass(self):
        """
        Metodo que que setea los valores en el Controlador
        """
        return MemoriaVisoespaciaPrueba

    def setField(self, data):
        """
        Metodo que que setea los valores en el Controlador
        """
        view = self.view
        view.sbDenomImg.setValue(data['sbDenomImg'])
        view.sbDenomImgT.setValue(data['sbDenomImgT'])

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de memoria visoespacia
        """
        view = self.view
        total = view.sbDenomImg.value()
        delayed = view.sbDenomImgT.value()
        
        valores = [total, delayed]

        self.test = MemoriaVisoespaciaPrueba(valores)

        datos = self.reporteModel.reporte['edad']

        self.test.calcularPERP(datos)

        self.changeView()