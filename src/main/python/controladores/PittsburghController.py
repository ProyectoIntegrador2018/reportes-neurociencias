from PyQt5 import QtCore
from vistas.PittsburghWindowWidget import PittsburghWindowWidget
from pruebas.PittsburghPrueba import PittsburghPrueba
from .mixins import WindowControllerMixin

class PittsburghController(WindowControllerMixin):
    switch_window = QtCore.pyqtSignal(object, object, bool)

    def getWidgetClass(self):
        """
        Metodo que regresa el objeto Widget del Controlador
        """
        return PittsburghWindowWidget

    def getTestClass(self):
        """
        Metodo que regresa el objeto Prueba del Controlador
        """
        return PittsburghPrueba

    def setField(self, data):
        """
        Metodo que que setea los valores en el Controlador
        """
        view = self.view
        view.comp1.setValue(data['comp1'])
        view.comp2.setValue(data['comp2'])
        view.comp3.setValue(data['comp3'])
        view.comp4.setValue(data['comp4'])
        view.comp5.setValue(data['comp5'])
        view.comp6.setValue(data['comp6'])
        view.comp7.setValue(data['comp7'])

    def getDatos(self):
        """
        Metodo para tomar los datos ingresados en la prueba de Pittsburgh
        """
        view = self.view

        comp1 = view.comp1.value()
        comp2 = view.comp2.value()
        comp3 = view.comp3.value()
        comp4 = view.comp4.value()
        comp5 = view.comp5.value()
        comp6 = view.comp6.value()
        comp7 = view.comp7.value()

        valores = (comp1,comp2,comp3,comp4,comp5,comp6,comp7)
        
        self.test = PittsburghPrueba(valores)

        datos = [self.reporteModel.reporte['educacion'], self.reporteModel.reporte['edad']]

        self.test.calcularPERP(datos)
        self.changeView()